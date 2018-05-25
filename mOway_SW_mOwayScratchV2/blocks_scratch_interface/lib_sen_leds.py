"""
***************************************************************
*      lib_sen_leds                                           *
*      Version: 5.0.1 https://github.com/blockext/blockext.git*
*      Description: This library contains the necessary       *
*      functions to create in Scratch the blocks              *
*      corresponding to the LEDs of the Moway robot.          *
*      Copyright (C) 2010  Bizintek Innova S.L.               *  
***************************************************************
"""

import blockext
from blockext import *
import sys, atexit , msvcrt
from time import sleep
sys.path.append("../lib/")
from moway_lib import *

menu("LedTop", ["Off", "Red", "Green","Blink Red","Blink Green"])
menu("LedFrontal", ["Off", "On","Blink"])
menu("LedBrake", ["Off", "On","Blink"])
menu("BroadcastAll", ["Off", "On","Blink"])

@command("Top leds %m.LedTop")
def LedTop_colour(LedTop="Off"):
       

    if LedTop=="Off":
        moway.command_moway(CMD_GREENLEDOFF,0)
        moway.command_moway(CMD_REDLEDOFF,0)
        
    if LedTop=="Red":
      
        moway.command_moway(CMD_GREENLEDOFF,0)
        moway.command_moway(CMD_REDLEDON,0)
        
    if LedTop=="Green":
      
        moway.command_moway(CMD_GREENLEDON,0)
        moway.command_moway(CMD_REDLEDOFF,0)
    if LedTop=="Blink Red":
        moway.command_moway(CMD_GREENLEDOFF,0)
        moway.command_moway(CMD_REDLEDOFF,0)
        moway.command_moway(CMD_REDBLINK,0)
    if LedTop=="Blink Green":
        moway.command_moway(CMD_GREENLEDOFF,0)
        moway.command_moway(CMD_REDLEDOFF,0)
        moway.command_moway(CMD_GREENBLINK,0)

    time.sleep(0.1)        
    return {
        "Off": "0",
        "Red": "1",
        "Green": "2",
    }[LedTop]

@command("Frontal light %m.LedFrontal")
def LedFrontal_state(LedFrontal="Off"):
       
   if LedFrontal=="Off":
        moway.command_moway(CMD_FRONTLEDOFF,0)
        
        
   if LedFrontal=="On":
      
        moway.command_moway(CMD_FRONTLEDON,0)
        
   if LedFrontal=="Blink":
        moway.command_moway(CMD_FRONTLEDOFF,0)
        moway.command_moway(CMD_FRONTBLINK,0)
        
   time.sleep(0.1)       
         
   return {
        "Off": "0",
        "On": "1",
        
   }[LedFrontal]

@command("Breaks %m.LedBrake")
def LedBrake_state(LedBrake="Off"):
  
    if LedBrake=="Off":
        moway.command_moway(CMD_BRAKELEDOFF,0)
        
        
    if LedBrake=="On":
      
        moway.command_moway(CMD_BRAKELEDON,0)

    if LedBrake=="Blink":
        moway.command_moway(CMD_BRAKELEDOFF,0)
        moway.command_moway(CMD_BRAKEBLINK,0)
        
     
    time.sleep(0.1)     
    return {
        "Off": "0",
        "On": "1",
        
    }[LedBrake]

@command("All %m.BroadcastAll")
def Broadcast_all(BroadcastAll="Off"):

     moway.command_moway(CMD_LEDSOFF,0)
     if BroadcastAll=="Off":
            moway.command_moway(CMD_LEDSOFF,0)
     if BroadcastAll=="On":
            moway.command_moway(CMD_LEDSON,0)
     if BroadcastAll=="Blink":
             moway.command_moway(CMD_LEDSBLINK,0)

     time.sleep(0.1)
     return {
        "Off": "0",
        "On": "1",
        "Blink": "2",
        
     }[BroadcastAll]
