#!/usr/bin/env python3


import asyncio
import math 
import json
from mavsdk import System
from mavsdk import (OffboardError, VelocityBodyYawspeed)

with open('/home/pi/Downloads/MAVSDK-Python/examples/connect.json','r') as f:
    aa = json.load(f)


async def run():
    """ Does Offboard control using velocity body coordinates. """

    drone = System()
    await drone.connect(system_address=aa['address'])

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    print("-- Arming")
    await drone.action.arm()
    await asyncio.sleep(7)

    print("-- Setting initial setpoint")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
    # await asyncio.sleep(5)

    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: \
              {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return
    
    
    print("--Climbing up m/s, while turning  deg/s in  second")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, -3.0, 0.0))
    await asyncio.sleep(6)


    # print("--Going foward 1 m/s, while turning {turn} deg/s in {t} second")
    # await drone.offboard.set_velocity_body(VelocityBodyYawspeed(-2.0, -2.0, 0.0, 0.0))
    # await asyncio.sleep(5)

    # print("-- Turn clock-wise and climb")
    # await drone.offboard.set_velocity_body(
    #     VelocityBodyYawspeed(0.0, 0.0, -1.0, 60.0))
    # await asyncio.sleep(5)

    # print("-- Turn back anti-clockwise")
    # await drone.offboard.set_velocity_body(
    #     VelocityBodyYawspeed(0.0, 0.0, 0.0, -60.0))
    # await asyncio.sleep(5)

    # print("-- Wait for a bit")
    # await drone.offboard.set_velocity_body(
    #     VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
    # await asyncio.sleep(2)

    print("-- Fly a circle")
    await drone.offboard.set_velocity_body(
        VelocityBodyYawspeed(3.0, 0.0, 0.0, 40.0))
    await asyncio.sleep(25)

    # print("-- Wait for a bit")
    # await drone.offboard.set_velocity_body(
    #     VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
    # await asyncio.sleep(5)

    # print("-- Fly a circle sideways")
    # await drone.offboard.set_velocity_body(
    #     VelocityBodyYawspeed(0.0, -5.0, 0.0, 30.0))
    # await asyncio.sleep(15)

    print("-- Wait for a bit")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
    await asyncio.sleep(8)

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: \
              {error._result.result}")

    print("--Landing")
    await drone.action.land()
    await asyncio.sleep(15)

    print('--Disarming')
    await drone.action.disarm()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
