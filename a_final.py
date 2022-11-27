from wisdom import *
import asyncio
from mavsdk import System
import time
from mavsdk.offboard import (OffboardError, PositionNedYaw)
import sys
import cv2 
from mavsdk.offboard import (OffboardError, PositionNedYaw)
from mask_rcnn import *

# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(connect_dac())
#     loop.run_until_complete(takeoff_dac())
#     loop.run_until_complete(mission_dac())
#     loop.run_until_complete(land_dac())
global drone
drone = System()


async def run():
    await connect_dac(drone, 14550)

    #Mission Import
    mission_import_data = await drone.mission_raw.import_qgroundcontrol_mission("/home/satz/centuriton/small_mission.plan")
    print(f"{len(mission_import_data.mission_items)} mission items imported")
    await drone.mission.set_return_to_launch_after_mission(True)
    #Mission Upload
    await drone.mission_raw.upload_mission(mission_import_data.mission_items)
    print("Mission uploaded")        
    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break
    #Mission ARM and START
    print("-- Arming")
    await drone.action.arm()
    print("-- Starting mission")
    await drone.mission.start_mission()

    while True:
        #OBTAIN TUPLE
        pxlCoord = objdet() #add import
        x = pxlCoord[0]
        y = pxlCoord[1]
        x_mid = 640
        y_mid = 360
        if x>=x_mid*0.5 and x<=x_mid*1.5 and y>=y_mid*0.5 and y<=y_mid*1.5:
            await interrupt_dac(x,y)

async def interrupt_dac(x,y):
    await drone.mission.pause_mission()
    await save_snapshot_actuation()
    await drone.mission.start_mission()

async def save_snapshot_actuation():
    #Actuate any servos or controls for Payload Delivery here.
    ret, frame = cv2.VideoCapture(0).read()
    t = time.strftime("%H_%M_%S", time.localtime())
    print("Snapshot taken")
                    



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())