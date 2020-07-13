#!/usr/bin/env python3

import asyncio
from mavsdk import System
import json
with open('./connect.json','r') as f:
    aa = json.load(f)


async def print_flight_mode():
    drone = System()
    await drone.connect(system_address=aa['address'])
    print(aa['address'])

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break
    print('ahihi')
    async for flight_mode in drone.telemetry.flight_mode():
        print("FlightMode:", flight_mode)
    print('abc')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_flight_mode())
