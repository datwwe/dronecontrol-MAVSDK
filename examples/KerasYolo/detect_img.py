import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image, ImageDraw, ImageFont
import glob
import os
from convertannotation import convert_annotation
import cv2
from datetime import datetime
import numpy as np


def bb_intersection_over_union(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou


def convert_center_width_height_to_x_y(box):
    x_min = box['center_x'] - int(box['width']/2)
    x_max = box['center_x'] + int(box['width']/2)
    y_min = box['center_y'] - int(box['height']/2)
    y_max = box['center_y'] + int(box['height']/2)
    return {
        'x_min': x_min,
        'x_max': x_max,
        'y_min': y_min,
        'y_max': y_max,
    }


def detect_img(yolo, img):
    box_heli, box_arrow = yolo.detect_image(img)
    result = {'time': datetime.timestamp(
        datetime.now()), 'helipad': None, 'arrow': None}
    if (len(box_heli) > 0):
        width = box_heli[2] - box_heli[0]
        height = box_heli[3] - box_heli[1]
        center_x = (box_heli[2] + box_heli[0])/2
        center_y = (box_heli[3] + box_heli[1])/2
        result['helipad'] = {'center_x': center_x,
                             'center_y': center_y, 'width': width, 'height': height}
    if (len(box_arrow) > 0):
        width = box_arrow[2] - box_arrow[0]
        height = box_arrow[3] - box_arrow[1]
        center_x = (box_arrow[2] + box_arrow[0])/2
        center_y = (box_arrow[3] + box_arrow[1])/2
        result['arrow'] = {'center_x': center_x,
                           'center_y': center_y, 'width': width, 'height': height}
    return result


def draw_box(image, result):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='font/FiraMono-Medium.otf',
                    size=np.floor(3e-2 * image.size[1] + 0.5).astype('int32'))
    
    if result['helipad'] is not None:
        color = 'red'
        helipad_box = convert_center_width_height_to_x_y(result['helipad'])
        draw.rectangle(((helipad_box['x_min'], helipad_box['y_min']),
                        (helipad_box['x_max'], helipad_box['y_max'])), outline=color, width = 3)
        label = 'helipad'
        label_size = draw.textsize(label, font)
        
        
        if helipad_box['y_min'] - label_size[1] >= 0:
            text_origin = np.array([helipad_box['x_min'], helipad_box['y_min'] - label_size[1]])
        else:
            text_origin = np.array([helipad_box['x_min'], helipad_box['y_min'] + 1])
        draw.rectangle(
            [tuple(text_origin), tuple(text_origin + label_size)],
            fill=color)
        draw.text(text_origin, label, fill=(0, 0, 0), font=font)
    if result['arrow'] is not None:
        color = 'blue'
        arrow_box = convert_center_width_height_to_x_y(result['arrow'])
        draw.rectangle(((arrow_box['x_min'], arrow_box['y_min']),
                        (arrow_box['x_max'], arrow_box['y_max'])), width=3, outline=color)
        label = 'arrow'
        label_size = draw.textsize(label, font)
        
        
        if arrow_box['y_min'] - label_size[1] >= 0:
            text_origin = np.array([arrow_box['x_min'], arrow_box['y_min'] - label_size[1]])
        else:
            text_origin = np.array([arrow_box['x_min'], arrow_box['y_min'] + 1])
        draw.rectangle(
            [tuple(text_origin), tuple(text_origin + label_size)],
            fill=color)
        draw.text(text_origin, label, fill=(0, 0, 0), font=font)
        



if __name__ == '__main__':
    yolo = YOLO()
    file_names = glob.glob('./video/aaa/*.jpg')
    fourcc = cv2.VideoWriter_fourcc(*'MPEG')
    video = cv2.VideoWriter('./video/output2.avi', fourcc, 20, (640, 480))
    for file_name in file_names:
        image = Image.open(file_name)
        result = detect_img(yolo, image)
        draw_box(image, result)
        video.write(cv2.cvtColor(np.array(image.copy()), cv2.COLOR_RGB2BGR))
    video.release()
