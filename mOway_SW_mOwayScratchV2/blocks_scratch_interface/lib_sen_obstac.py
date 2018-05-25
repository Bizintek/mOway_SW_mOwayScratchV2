"""
***************************************************************
*      lib_sen_obstac                                         *
*      Version: 5.0.1 https://github.com/blockext/blockext.git*
*      Description: This library contains the necessary       *
*      functions to create the blocks corresponding to the    *
*      obstacle sensors of the Moway robot in Scratch.        *
*      Copyright (C) 2010  Bizintek Innova S.L.               *  
***************************************************************
"""


import blockext
from blockext import *
import sys, atexit , msvcrt
from time import sleep
sys.path.append("../lib/")
from moway_lib import *

menu("ObstSens",["LeftSide","LeftCenter","RightSide","RightCenter"])

@reporter("Right side obstacle sensors")
def RightSideObs():
       
       return moway.get_obs_side_right()

@reporter("Right center obstacle sensors")
def RightCenterObs():
       

       return moway.get_obs_center_right()

@reporter("Left side obstacle sensors")
def LeftSideObs():
       
       return moway.get_obs_side_left()

@reporter("Left center obstacle sensors")
def LeftCenterObs():
       
       
       return moway.get_obs_center_left()
