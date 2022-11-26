#Tensorflowlite Deployment on raspberry-pi 3b+
*Run these commands for dependencies on cli for debian

`pip install opencv-contrib-python`
`pip install tensorflow`

make sure camera is connected by issuing `lsusb` simultanesoly,
connect all peripherals required

use this to issue execution `python TFLite_detection_webcam.py --modeldir=TFLite_model`

