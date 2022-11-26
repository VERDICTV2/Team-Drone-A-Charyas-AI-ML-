# Autonomous UAV applications using Deep learning algorithms for search and rescue operations
# Team Drone-a-Charyas 


__To install Jmavsim and Px4 SITL (Software in the loop)__

***Run these commands for dependencies on cli for ubuntu 20.04***

followed instructions to make and build PX4 env on ubuntu from 
`https://docs.px4.io/main/en/simulation/jmavsim`



__To install mavlink router for controlling drone and port forwarding frrom either raspberry-pi and localhost 

follow instructions from `https://github.com/mavlink-router/mavlink-router`



__to install MAVSDK-PYTHON library for drone control and AI integration with drone navigation with autonomy__


`pip3 install mavsdk`



__Mask_RCNN Model that is integrated with MAVSDK that shakes hand with drone navigation and generates interrupts based on objects detected on the ground and navigates the drone accordingly__










__deployment of our AI deep learning model on raspberry-pi 3b+__

***Run these commands for dependencies on cli for debian***

`pip install opencv-contrib-python`
`pip install tensorflow`


*make sure camera is connected by issuing*`lsusb` *simultanesoly,*
*connect all peripherals required*
*makes use of tensorflowlite for raspberry-pi as it is a edge device and cannot handle the usual tensorflow used on  generic PC's

use this to issue execution `python TFLite_detection_webcam.py --modeldir=TFLite_model`






