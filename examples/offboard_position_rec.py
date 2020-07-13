#!/usr/bin/env python3

"""
Caveat when attempting to run the examples in non-gps environments:

`drone.offboard.stop()` will return a `COMMAND_DENIED` result because it
requires a mode switch to HOLD, something that is currently not supported in a
non-gps environment.
"""

import asyncio
import json
with open('./connect.json','r') as f:
    aa = json.load(f)
from mavsdk import System
from mavsdk import (OffboardError, PositionNedYaw)


async def run():
    """ Does Offboard control using position NED coordinates. """

    drone = System()
    await drone.connect(system_address=aa['address'])

    print("-- Arming")
    await drone.action.arm()
    await drone.action.set_takeoff_altitude(5.0)
    await drone.action.set_maximum_speed(0.5)

    print("--Taking off")
    await drone.action.takeoff()
    await asyncio.sleep(8)

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

    print("-- Go 0m North, 0m East, -5m Down within local coordinate system")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -5.0, 0.0))
    await asyncio.sleep(5)

    print("-- Go 5m North, 0m East, -5m Down within local coordinate system, turn to face East")
    await drone.offboard.set_position_ned(PositionNedYaw(10.0, 10.0, -5.0, 0.0))
    await asyncio.sleep(15)

    # print("-- Go 5m North, 5m East, -5m Down within local coordinate system")
    # await drone.offboard.set_position_ned(PositionNedYaw(5.0, 5.0, -5.0, 0.0))
    # await asyncio.sleep(5)

    # print("-- Go 5m North, 5m East, -5m Down within local coordinate system")
    # await drone.offboard.set_position_ned(PositionNedYaw(0.0, 5.0, -5.0, 0.0))
    # await asyncio.sleep(5)

    print("-- Go 0m North, 0m East, -5m Down within local coordinate system")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -5.0, 0.0))
    await asyncio.sleep(15)

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
        await asyncio.sleep(10)

        print("--Landing")
        await drone.action.land()
        await asyncio.sleep(12)

        print("--Disarming")
        await drone.action.disarm()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: {error._result.result}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
