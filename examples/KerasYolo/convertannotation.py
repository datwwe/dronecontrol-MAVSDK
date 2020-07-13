import glob
import cv2
def abc():
    list_files = glob.glob('./model_data/images/*.txt')
    write_data = ''
    for file_name in list_files:
        raw_data = ''
        with open(file_name, 'r') as f:
            raw_data = f.read()

        if raw_data != '':
            file_image = file_name.replace('txt', 'jpg')
            file_image = file_image.replace('.\\', './model_data/images/')
            write_data += file_image
            lines = raw_data.split('\n')
            for line in lines:
                words = line.split(' ')
                words = [float(num) for num in words]
                center_x = int(words[1]*640)
                center_y = int(words[2]*480)
                width = int(words[3]*640)
                height = int(words[4]*480)
                x_min = center_x - int(width/2)
                y_min = center_y - int(height/2)
                x_max = center_x + int(width/2)
                y_max = center_y + int(height/2)
                
                write_data+= ' ' + str(x_min) + ','+str(y_min)+','+ str(x_max)+','+str(y_max)+','+str(int(words[0]))
            write_data+='\n'
    with open('./model_data/train.txt','w') as f:
        f.write(write_data)

abc()

def convert_annotation(path):
    raw_data = ''
    with open(path, 'r') as f:
        raw_data = f.read()
    if raw_data != '':
        raw_data = raw_data.split(' ')
        raw_data = [float(num) for num in raw_data]
        center_x = int(raw_data[1]*640)
        center_y = int(raw_data[2]*480)
        width = int(raw_data[3]*640)
        height = int(raw_data[4]*480)
        x_min = center_x - int(width/2)
        y_min = center_y - int(height/2)
        x_max = center_x + int(width/2)
        y_max = center_y + int(height/2)
        return [x_min, y_min, x_max, y_max]