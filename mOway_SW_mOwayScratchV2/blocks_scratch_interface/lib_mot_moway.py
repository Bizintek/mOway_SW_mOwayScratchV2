"""
***************************************************************
*      lib_mot_moway                                          *
*      Version: 5.0.1 https://github.com/blockext/blockext.git*
*      Description: This library contains the necessary       *
*      functions to create in Scratch the blocks              *
*      corresponding to the movement of the Moway Robot.      *
*      Copyright (C) 2010  Bizintek Innova S.L.               *  
***************************************************************
"""
import blockext
from blockext import *
import sys, atexit , msvcrt
from time import sleep
sys.path.append("../lib/")
from moway_lib import *

menu("Direction", ["Forward", "Backward"])
menu("Rotation",["Left","Right"])
menu("Type",["Central","Wheel"])

@command("Indefined stright line Speed %n %m.Direction")
def IndefinedLine( Speed=50, Direction="Forward"):
       d_Direction={"Forward":CMD_GO_SIMPLE,"Backward":CMD_BACK_SIMPLE}
       moway.set_speed(Speed)
       moway.command_moway(d_Direction[Direction],0)       
       

@command("Stop Moway")
def MowayStop():
       moway.command_moway(CMD_STOP,0)

@command("Straight line Speed %n Distance(cm) %n %m.Direction")
def StraightLine( Speed=50, Distance=5, Direction="Forward" ):
    d_Direction={"Forward":CMD_GO,"Backward":CMD_BACK}
    Distance=Distance*10   
    moway.set_distance(Distance)
    moway.set_speed(Speed)
    moway.command_moway(d_Direction[Direction],0)
    moway.wait_mot_end(0)

    return
        

@command ("Simple rotation. Speed %n %m.Rotation %m.Type") 
def SimpleRotation(Speed=50,Rotation="Left", Type="Central"):
     d_Type={"Central":CENTER,"Wheel":WHEEL}
     d_Rotation={"Left":CMD_LEFT_SIMPLE,"Right":CMD_RIGHT_SIMPLE} 
     moway.set_speed(Speed)
     moway.set_rotation_axis(d_Type[Type])
     moway.command_moway(d_Rotation[Rotation])
     moway.wait_mot_end(0)
     
     return


@command ("Angle rotation Speed %n %m.Rotation %m.Type  Angle %n") 
def AngleRotation(Speed=50,Rotation="Left", Type="Central", Angle=45):

       
     d_Type={"Central":CENTER,"Wheel":WHEEL}
     d_Rotation={"Left":CMD_ROTATELEFT,"Right":CMD_ROTATERIGHT}
     

     moway.set_speed(Speed) 
     moway.set_rotation(Angle)
     moway.set_rotation_axis(d_Type[Type])
     moway.command_moway(d_Rotation[Rotation])
     moway.wait_mot_end(0)
     

     
     return

@command("Push")
def Push():
       
       moway.command_moway(CMD_PUSH,0)
       return

@command ("Turn over Speed %n %m.Type")
def TurnOver(Speed=50,Type="Central"):
       d_Type={"Central":CENTER,"Wheel":WHEEL}
       moway.set_rotation_axis(d_Type[Type])
       moway.set_speed(Speed)
       moway.command_moway(CMD_TURN_AROUND,0)
       moway.wait_mot_end(0)

