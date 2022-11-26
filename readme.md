# Autonomous UAV applications using Deep learning algorithms for search and rescue operations
# Team Drone-a-Charyas 


__To install JMAVsim simulator and PX4 Firmware SITL (Software in the loop)__

***we use JMAVsim and PX4 hand in hand to simulate a real world drone with an actual connection string in form of a UDP port and control this using MAVSDK-python Run these commands for dependencies on cli for ubuntu 20.04***


issue `make px4_sitl_default jmavsim`  to start SITL in head mode after installing pre-requuisites from `https://docs.px4.io/main/en/dev_setup/dev_env.html`

__To install mavlink router for controlling drone and port forwarding from either raspberry-pi and localhost to throw its output so mission progressi s viewable on a ground station__

follow instructions from `https://github.com/mavlink-router/mavlink-router`


__to install MAVSDK-PYTHON library for drone control and AI integration with drone navigation with autonomy__


`pip3 install mavsdk`



__Mask_RCNN Model that is integrated with MAVSDK that shakes hand with drone navigation and generates interrupts based on objects detected on the ground and navigates the drone accordingly__


*other Dependencies for running Mask_RCNN model in hand with GUI preview*

`pip install PIL`
`pip install torchvision`
`pip install detecto`


*The mask_RCNN model uses a python executable file for running the model on new data live from the webcam feed, using this data i.e comparing the pixel location of image and pixel location of object we leverage the drone navigation usign mavsdk-python library and forward a UDP port to view, simulate 
the same in a real world-likeenvoirment*

execute python file by issuing `


__deployment of our AI deep learning model on raspberry-pi 3b+__

***Run these commands for dependencies on cli for debian***

`pip install opencv-contrib-python`
`pip install tensorflow`


*make sure camera is connected by issuing*`lsusb` *simultanesoly,*
*connect all peripherals required*
*makes use of tensorflowlite for raspberry-pi as it is a edge device and cannot handle the usual tensorflow used on  generic PC's

use this to issue execution `python TFLite_detection_webcam.py --modeldir=TFLite_model`






