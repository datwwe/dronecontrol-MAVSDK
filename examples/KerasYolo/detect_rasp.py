#!/usr/bin/env python3

import asyncio
from mavsdk import System
import io
import time
import picamera
from PIL import Image
from detect_img import detect_img
from yolo import YOLO
import math
from datetime import datetime
import json
from mavsdk import (OffboardError, PositionNedYaw)
with open('/home/pi/Downloads/MAVSDK-Python/examples/connect.json','r') as f:
    aa = json.load(f)
    
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
        return {
            'actual_delta_x':actual_delta_x,
            'actual_delta_y':actual_delta_y,
            'angle': angle,
            'time': datetime.now().strftime("%a,  %d %b %Y %H:%M:%S")
        }
    return None
async def print_flight_mode(yolo, helipad_edge, image_width, image_height ):
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
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, 0.0, 0.0))

    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return
    print("-- Setting initial setpoint")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -10.0, 0.0))
    await asyncio.sleep(7)

    with picamera.PiCamera() as camera:
        total_x =0
        total_y =0
        camera.resolution = (640, 480)
        camera.start_preview()
        count =0
        results = []
        for image in image_generator(camera):
            print('image' + str(count) +'.jpg')
            image.save('./video/test' + str(count)+'.jpg','jpeg')
            # image = Image.open('./video/outputframe2.jpg')
            
            result = detect_img(yolo,image)
            result = calculate_distance(result, helipad_edge, image_width, image_height)
            print(result)
            if result is not None:
                results.append(result)
                total_x += result['actual_delta_x']
                total_y += -result['actual_delta_y']
                print(result)   
                count+=1
                # print("-- Setting initial setpoint")
                # await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -10.0, 0.0))
                # await asyncio.sleep(5)

                height = -10.0
                if count==1:
                    height = -5.0
                elif count == 2:
                    height = 0.0
            
                print("-- Go {}m North, {}m East, 0m Down within local coordinate system".format(-result['actual_delta_y'],result['actual_delta_x']))
                await drone.offboard.set_position_ned(PositionNedYaw(total_y, total_x, height , 0.0))
                await asyncio.sleep(8)
                if count ==2:
                    print(count)
                    break

        print('Saved to results_pos_{}.json'.format(datetime.now().strftime("%a,  %d %b %Y %H:%M:%S")))
        with open('results_pos_{}.json'.format(datetime.now().strftime("%a,  %d %b %Y %H:%M:%S")),'w') as f:
            json.dump({'results':results},f)


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
        await asyncio.sleep(5)

        await drone.action.disarm()
            
            # if count ==3:
            #     break
        


if __name__ == "__main__":
    yolo = YOLO()
    HELIPAD_EDGE = 0.566
    IMAGE_WIDTH = 640
    IMAGE_HEGIHT = 480
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_flight_mode(yolo, HELIPAD_EDGE, IMAGE_WIDTH,IMAGE_HEGIHT))
