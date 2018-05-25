"""
***************************************************************
*      lib_sen_light                                          *
*      Version: 5.0.1 https://github.com/blockext/blockext.git*
*      Description: This library contains the necessary       *
*      functions to create the blocks corresponding to the    *
*      light sensor of the Moway robot in Scratch.            *
*      Copyright (C) 2010  Bizintek Innova S.L.               *  
***************************************************************
"""

import blockext
from blockext import *
import sys, atexit , msvcrt
sys.path.append("../lib/")
from moway_lib import *

@reporter("Light sensor")
def LightSensor():
       act_light=moway.get_light()
        
       return act_light
