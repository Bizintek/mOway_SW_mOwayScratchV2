"""
***************************************************************
*      lib_speaker_moway                                      *
*      Version: 5.0.1 https://github.com/blockext/blockext.git*
*      Description: This library contains the necessary       *
*      functions to create the blocks corresponding to the    *
*      Speaker of the Moway robot in Scratch.                 *
*      Copyright (C) 2010  Bizintek Innova S.L.               *  
***************************************************************
"""


import blockext
from blockext import *
import sys, atexit , msvcrt
from time import sleep
sys.path.append("../lib/")
from moway_lib import *

menu("Speak",["On","Off"])
menu ("Track",["Song 1","Song 2"])


@command("Sound %m.Speak")
def Sound(Speak="Off"):
       d_Sound={"On":CMD_BUZZERON ,"Off":CMD_BUZZEROFF }
       moway.command_moway(d_Sound[Speak],0)
       return

@command("Sing %m.Track")
def Singer(Track="Song 1"):
       d_Singer={"Song 1":CMD_MELODYCHARGE,"Song 2":CMD_MELODYFAIL}
       moway.command_moway(d_Singer[Track],0)
       return
