
import asyncio
from mavsdk import System
from mavsdk.geofence import Point, Polygon
import time



#Primary requirments 


#necessary functions 
async def connect_dac(drone, port = 14550):
    print("Waiting for drone to connect...")
    await drone.connect(system_address=f"udp://:{port}")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

#Takeoff
async def takeoff_dac(drone):
    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()

# async def missionImportUploadStart_dac(path = "quadrangle_search_grid.plan"):

#     print_mission_progress_task = asyncio.ensure_future(
#     print_mission_progress(drone))
#     running_tasks = [print_mission_progress_task]
#     termination_task = asyncio.ensure_future(
#         observe_is_in_air(drone, running_tasks))


#     mission_import_data = await drone.mission_raw.import_qgroundcontrol_mission(path)
#     print(f"{len(mission_import_data.mission_items)} mission items imported")
#     await drone.mission_raw.upload_mission(mission_import_data.mission_items)
#     print("Mission uploaded")        

#     await drone.mission.set_return_to_launch_after_mission(True)
#     print("-- Arming")
#     await drone.action.arm()

#     print("-- Starting mission")
#     await drone.mission.start_mission()

#     await termination_task


# async def print_mission_progress(drone):
#     async for mission_progress in drone.mission.mission_progress():
#         print(f"Mission progress: "
#               f"{mission_progress.current}/"
#               f"{mission_progress.total}")


# async def observe_is_in_air(drone, running_tasks):
#     """ Monitors whether the drone is flying or not and
#     returns after landing """

#     was_in_air = False

#     async for is_in_air in drone.telemetry.in_air():
#         if is_in_air:
#             was_in_air = is_in_air

#         if was_in_air and not is_in_air:
#             for task in running_tasks:
#                 task.cancel()
#                 try:
#                     await task
#                 except asyncio.CancelledError:
#                     pass
#             await asyncio.get_event_loop().shutdown_asyncgens()

#             return



async def land_dac(drone):
         await drone.action.land()





async def geofence_dac(drone):
            print("Fetching home location coordinates...")
            async for terrain_info in drone.telemetry.home():
                latitude = terrain_info.latitude_deg
                longitude = terrain_info.longitude_deg
                break

            await asyncio.sleep(1)

            # Define your geofence boundary
            p1 = Point(latitude - 0.0001, longitude - 0.0001)
            p2 = Point(latitude + 0.0001, longitude - 0.0001)
            p3 = Point(latitude + 0.0001, longitude + 0.0001)
            p4 = Point(latitude - 0.0001, longitude + 0.0001)

            # Create a polygon object using your points
            polygon = Polygon([p1, p2, p3, p4], Polygon.FenceType.INCLUSION)

            # Upload the geofence to your vehicle
            print("Uploading geofence...")
            await drone.geofence.upload_geofence([polygon])

            print("Geofence uploaded!")
    #interrupt if geofence is touched

            async for position in drone.telemetry.position():
                curnt_lat = position.latitude_deg
                curnt_lon = position.longitude_deg

            if curnt_lat > latitude - 0.0001 and curnt_lon> longitude - 0.0001:
                land_dac()
            elif curnt_lat > latitude + 0.0001 and curnt_lon> longitude - 0.0001:
                land_dac()
            elif curnt_lat > latitude + 0.0001 and curnt_lon> longitude + 0.0001:
                land_dac()
            elif curnt_lat > latitude + 0.0001 and curnt_lon> longitude + 0.0001:
                land_dac()


    

            
              


    
    

    
    # async def run():

    #     drone = System()
    #     await drone.connect(system_address="udp://:14540")
    #     print("Next connect")
    #     #await drone.connect(system_address="tcp://:4560")
    #     print("Connected")
    #     status_text_task = asyncio.ensure_future(print_status_text(drone))

    #     print("Waiting for drone to connect...")
    #     async for state in drone.core.connection_state():
    #         if state.is_connected:
    #             print(f"-- Connected to drone!")
    #             break

    #     print("Waiting for drone to have a global position estimate...")
    #     async for health in drone.telemetry.health():
    #         if health.is_global_position_ok and health.is_home_position_ok:
    #             print("-- Global position estimate OK")
    #             break

    #     print("-- Arming")
    #     await drone.action.arm()

    #     print("-- Taking off")
    #     await drone.action.takeoff()





        # await asyncio.sleep(10)

        # print("-- Landing")
        # await drone.action.land()

        # status_text_task.cancel()



    # async def print_status_text(drone):
    #     try:
    #         async for status_text in drone.telemetry.status_text():
    #             print(f"Status: {status_text.type}: {status_text.text}")
    #     except asyncio.CancelledError:
    #         return


    # if __name__ == "__main__":
    #     loop = asyncio.get_event_loop()
    #     loop.run_until_complete(run())





   