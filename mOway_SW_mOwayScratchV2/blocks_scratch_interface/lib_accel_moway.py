"""
***************************************************************
*      lib_accel_moway                                        *
*      Version: 5.0.1 https://github.com/blockext/blockext.git*
*      Description: This library contains the necessary       *
*      functions to create the blocks corresponding to the    *
*      Moway robot accelerometer in Scratch.                  *
*      Copyright (C) 2010  Bizintek Innova S.L.               *  
***************************************************************
"""

import blockext
from blockext import *
import sys, atexit , msvcrt
from time import sleep
sys.path.append("../lib/")
from moway_lib import *

@reporter("X axis")
def x_axis():
       return moway.get_accel_X()
@reporter("Y axis")
def y_axis():
       return moway.get_accel_Y()
@reporter("Z axis")
def z_axis():
       return moway.get_accel_Z()

