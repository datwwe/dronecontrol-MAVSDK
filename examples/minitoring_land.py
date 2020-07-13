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
import json
from datetime import datetime
from mavsdk import (OffboardError, VelocityBodyYawspeed)
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
        d = math.sqrt(actual_delta_x*actual_delta_x + actual_delta_y*actual_delta_y)

        return {
            'actual_delta_x':actual_delta_x,
            'actual_delta_y':actual_delta_y,
            'angle': angle,
            'd': d,
            'time': datetime.now().strftime("%a,  %d %b %Y %H:%M:%S"),
            'area': helipad['width']*helipad['height']
        }
    return None
async def print_flight_mode(yolo, helipad_edge, image_width, image_height ):
    drone = System()
    await drone.connect(system_address=aa['address'])
    lines = []
    VECLOCITY_MAX = 1
    VECLOCITY_DOWN = 1

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
    await asyncio.sleep(6)

    print("-- Holding")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))

    with picamera.PiCamera() as camera:
        d = None
        angle = None
        results = []
        camera.resolution = (640, 480)
        camera.start_preview()
        count =0
        count_no_box = 0
        for image in image_generator(camera):
            print('image' + str(count) +'.jpg')
            # image.save('./video/test' + str(count)+'.jpg','jpeg')
            # image = Image.open('./video/outputframe2.jpg')
            
            result = detect_img(yolo,image)
            result = calculate_distance(result, helipad_edge, image_width, image_height)
            print(result)
            count+=1
            if result is not None:
                lines.append("Detected an helipad {} meters away from an angle of {} degrees".format(result['d'], result['angle']))
                print("Detected an helipad {} meters away from an angle of {} degrees".format(result['d'], result['angle']))
                count_no_box = 0
                results.append(result)
                if result['d'] >=0.1:
                    if d is None:
                        VECLOCITY = min(VECLOCITY_MAX, result['d'] * 0.25)
                        vy = (-result['actual_delta_y'] + 0.07) * VECLOCITY / result['d']
                        vx = (result['actual_delta_x']+0.005) * VECLOCITY / result['d']
                        print("-- Go {}m/s ahead, {}m/s right, {}m/s down ".format(vy,vx,VECLOCITY_DOWN))
                        lines.append("Go in the direction of {} degrees with veclocity of {} m/s".format(result['angle'], VECLOCITY))
                        await drone.offboard.set_velocity_body(VelocityBodyYawspeed(vy, vx, VECLOCITY_DOWN, 0.0))
                        d = result['d']
                        angle = result['angle']

                    else:
                        if result['d'] < d+ 0. and result['angle'] >= angle - 15 and result['angle']<=angle +15 :
                            d = result['d']
                            angle = result['angle']
                            VECLOCITY = VECLOCITY *0.9
                            VECLOCITY_DOWN = VECLOCITY_DOWN *0.9
                            lines.append("Keeping direction")
                            print("--Keeping direction")
                        else:
                            print("-- Holding")
                            lines.append("Wrong direction hold to get new command")
                            print("Wrong direction hold to get new command")
                            d = None
                            angle = None
                            VECLOCITY = VECLOCITY *0.7
                            VECLOCITY_DOWN = VECLOCITY_DOWN *0.7
                            await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
                            await asyncio.sleep(0.5)
                else:
                    if  result['area']/(480*640) < 0.5:
                        await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, -0.5, 0.0))
                        
                    else:
                        break
            else:
                await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
                await asyncio.sleep(0.8)
                count_no_box +=1
            if count_no_box ==3: 
                break

        lines.append("In landing condition 10 cm, Land")
        print('Saved to results_monitoring_{}.txt'.format(datetime.now().strftime("%a,  %d %b %Y %H:%M:%S")))
        with open('results_monitoring_{}.txt'.format(datetime.now().strftime("%a,  %d %b %Y %H:%M:%S")),'w') as f:
            f.writelines(lines)
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
