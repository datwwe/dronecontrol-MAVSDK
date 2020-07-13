#!/usr/bin/env python3

import asyncio
from mavsdk import System

import json
with open('./connect.json','r') as f:
    aa = json.load(f)
async def run():

    drone = System()
    await drone.connect(system_address=aa['address'])

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    # print("Waiting for drone to have a global position estimate...")
    # async for health in drone.telemetry.health():
    #     if health.is_global_position_ok:
    #         print("Global position estimate ok")
    #         break

    print("-- Arming")
    await drone.action.arm()
    await asyncio.sleep(5)
    await drone.action.set_takeoff_altitude(5.0)
        
    # async for flight_mode in drone.telemetry.flight_mode():
    #     print("FlightMode:", flight_mode)
    # await asyncio.sleep(1)
    print("-- Taking off")
    await drone.action.takeoff()

    await asyncio.sleep(20)
    
    print("-- Landing")
    await drone.action.land()

    await asyncio.sleep(20)

    print('-- Disarming')
    await drone.action.disarm()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
