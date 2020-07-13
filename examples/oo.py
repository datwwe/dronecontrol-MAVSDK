#!/usr/bin/env python3

import asyncio
from mavsdk import System
import io
import time
import picamera
from PIL import Image
from async_generator import async_generator, yield_

def image_generator(camera):
    while(True):
        stream = io.BytesIO()
        camera.capture(stream, format='jpeg')
        stream.seek(0)
        image = Image.open(stream)  
        yield image


async def print_flight_mode():
    drone = System()
    await drone.connect(system_address="aa['address']")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        count =0
        for image in image_generator(camera):
            print('image' + str(count) +'.jpg')
            image.save('image' + str(count)+'.jpg','jpeg')
            count+=1
            await asyncio.sleep(1)
        


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_flight_mode())
