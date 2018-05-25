"""
***************************************************************
*      lib_sen_volume                                         *
*      Version: 5.0.1 https://github.com/blockext/blockext.git*
*      Description: This library contains the necessary       *
*      functions to create the blocks corresponding to the    *
*      volume sensor of the Moway robot in Scratch.           *
*      Copyright (C) 2010  Bizintek Innova S.L.               *  
***************************************************************
"""

import blockext
from blockext import *
import sys, atexit , msvcrt
from time import sleep
sys.path.append("../lib/")
from moway_lib import *

@reporter("Volume sensor")
def volume_sensor():
    
    act_vol=moway.get_mic()

    
    return act_vol
