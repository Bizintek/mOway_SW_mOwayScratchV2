"""
***************************************************************
*      lib_sen_line                                           *
*      Version: 5.0.1 https://github.com/blockext/blockext.git*
*      Description: This library contains the necessary       *
*      functions to create the blocks corresponding to the    *
*      line sensors of the Moway robot in Scratch.            *
*      Copyright (C) 2010  Bizintek Innova S.L.               *  
***************************************************************
"""

import blockext
from blockext import *
import sys, atexit , msvcrt
sys.path.append("../lib/")
from moway_lib import *

menu("Line",["Left","Right"])

@command("Follow line %m.Line")
def LineF(Line="Left"):
 
       
       moway.set_rotation_axis(WHEEL)
       d_Line={"Right":CMD_LINE_FOLLOW_R,"Left":CMD_LINE_FOLLOW_L}
       moway.command_moway(d_Line[Line],0)

       return
