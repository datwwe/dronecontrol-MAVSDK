#!/usr/bin/env python3

from time import gmtime, strftime
import asyncio
from mavsdk import System
import io
import time
import picamera
from PIL import Image
from detect_img import detect_img
from yolo import YOLO
import math
import json
from mavsdk import (OffboardError, VelocityBodyYawspeed)
with open('/home/pi/Downloads/MAVSDK-Python/examples/connect.json','r') as f:
    aa = json.load(f)
VECLOCITY = 1.5


def image_generator(camera):
    while(True):
        stream = io.BytesIO()
        camera.capture(stream, format='jpeg')
        stream.seek(0)
        image = Image.open(stream)  
        yield image



def calculate_distance(result, helipad_edge, image_width, image_height):
    image_center_x = int(image_width/2)
    iamge_center_y = int(image_height/2)
    helipad = result['helipad']
    if helipad is not None:
        delta_x = helipad['center_x'] - image_center_x
        delta_y = helipad['center_y'] - iamge_center_y
        size = max(helipad['width'], helipad['height'])
        ratio = helipad_edge / size
        actual_delta_x = delta_x * ratio
        actual_delta_y = delta_y * ratio
        angle =math.degrees(math.atan(delta_y/delta_x))
        d = math.sqrt(actual_delta_x*actual_delta_x + actual_delta_y*actual_delta_y)

        return {
            'actual_delta_x':actual_delta_x,
            'actual_delta_y':actual_delta_y,
            'angle': angle,
            'd': d
        }
    return None
async def print_flight_mode(yolo, helipad_edge, image_width, image_height ):
    strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    drone = System()
    await drone.connect(system_address=aa['address'])
    
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break
    # async for flight_mode in drone.telemetry.flight_mode():
    #     print("FlightMode:{}|||||||||".format(flight_mode))
    #     if str(flight_mode) == "HOLD":
    #         await asyncio.sleep(10)
    #         break
   
    print("-- Arming")
    await drone.action.arm()
    await asyncio.sleep(4)


    # await drone.action.set_takeoff_altitude(5.0)
    # print("-- Taking off")
    # await drone.action.takeoff()
    # await asyncio.sleep(9)

    print("-- Setting initial setpoint")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))

    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return
    print("--Climbing up m/s, while turning  deg/s in  second")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, -3.0, 0.0))
    await asyncio.sleep(5)

    print("-- Holding")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))

    with picamera.PiCamera() as camera:
        total_x =0
        total_y =0
        camera.resolution = (640, 480)
        camera.start_preview()
        count =0
        for image in image_generator(camera):
            print('image' + str(count) +'.jpg')
            image.save('./video/test' + str(count)+'.jpg','jpeg')
            # image = Image.open('./video/outputframe2.jpg')
            
            result = detect_img(yolo,image)
            result = calculate_distance(result, helipad_edge, image_width, image_height)
            count+=1
            if result is not None:
                if (result['d']>=0.2):
                    vy = -result['actual_delta_y'] * VECLOCITY / result['d']
                    vx = result['actual_delta_x'] * VECLOCITY / result['d']
                    print("-- Go {}m ahead, {}m East, 0m right within local coordinate system".format(vy,vx))
                    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(vy, vx, 1.0, 0.0))
                    await asyncio.sleep(0.2)
                    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
                    await asyncio.sleep(0.5)
                else:
                    break
        print(result)
        print("-- Stopping offboard")
        try:
            await drone.offboard.stop()
            await asyncio.sleep(3)
            

        except OffboardError as error:
            print(f"Stopping offboard mode failed with error code: {error._result.result}")
            # print('--Landing')
            # await drone.action.land()
            # await asyncio.sleep(10)

        print('--Landing')
        await drone.action.land()
        await asyncio.sleep(15)

        await drone.action.disarm()
            
            # if count ==3:
            #     break
        


if __name__ == "__main__":
    yolo = YOLO()
    HELIPAD_EDGE = 0.562
    IMAGE_WIDTH = 640
    IMAGE_HEGIHT = 480
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_flight_mode(yolo, HELIPAD_EDGE, IMAGE_WIDTH,IMAGE_HEGIHT))
