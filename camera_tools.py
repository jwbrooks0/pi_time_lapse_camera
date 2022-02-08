#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 09:18:37 2021

@author: pi
"""

## how to enable preview over vnc
# https://www.youtube.com/watch?v=dbBWyeHbGs0

import time
from time import sleep
from picamerax import PiCamera

def print_camera_settings(camera):
    # https://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera._get_camera_settings
    print('gain, analog \t\t' ,camera.analog_gain)
    print('gain, digital \t\t' ,camera.digital_gain)
    print('iso \t\t\t' ,camera.iso)
    print('bright \t\t\t' ,camera.brightness)
    print('contrast \t\t' ,camera.contrast)
    print('zoom \t\t\t' ,camera.zoom)
    print('exp comp \t\t' ,camera.exposure_compensation)
    print('exp mode \t\t' ,camera.exposure_mode)
    print('exp speed (us) \t\t' ,camera.exposure_speed)
    print('frame rate \t\t' ,camera.framerate)# videos and preview frame rate
    print('resolution \t\t' ,camera.resolution)
    print('rotation \t\t' ,camera.rotation)
    print('saturation \t\t' ,camera.saturation)
    print('sensor mode \t\t' ,camera.sensor_mode)
    print('sharpness \t\t' ,camera.sharpness)
    print('shutter speed (us) \t' ,camera.shutter_speed)


def time_str():
    return time.strftime("%Y%m%d_%H%M%S")


def time_lapse(camera,sleep_time_sec=60,num_captures=1000):
    
    for i in range(num_captures):
        filename=time_str()+'.png'
        camera.capture(filename)
        print('Captured %s' % filename)
        sleep(sleep_time_sec)
        
def create_camera(resolution=(1024, 768), iso=100):
    
    camera = PiCamera()
    camera.resolution = resolution
    camera.iso = iso
    
    return camera

def open_preview_window(camera):
    camera.start_preview()
    