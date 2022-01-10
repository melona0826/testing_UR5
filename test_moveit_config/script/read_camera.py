#!/usr/bin/env python

import sys, time
import numpy as np
from scipy.ndimage import filters
import cv2
import roslib
import rospy
print('openCV version : ' , cv2.__version__)

from sensor_msgs.msg import CompressedImage

class image_read :
    def __init__(self) :
        self.subscriber = rospy.Subscriber("/test_ur/camera1/image_raw/compressed" , CompressedImage, self.callback, queue_size = 1)

    def callback(self, ros_data) :
        np_arr = np.fromstring(ros_data.data, np.uint8)
        image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        resized_image = cv2.resize(image_np, (320, 240) , interpolation = cv2.INTER_NEAREST)
        cv2.namedWindow("testing" , cv2.WINDOW_NORMAL)
        cv2.imshow('testing' , resized_image)
        cv2.waitKey(2)

def main(args) :
    src_img = image_read()
    rospy.init_node('image_read' , anonymous = True)
    try :
        rospy.spin()
    except KeyboardInterrupt :
        print("Shutting down !")
        cv2.destoryAllWindows()

if __name__ == '__main__' :
    main(sys.argv)
