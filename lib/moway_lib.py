import sys, os
from ctypes import *
sys.path.append("../lib/")

#import libmoway library depending on the OS
if os.name == 'nt':
        if sizeof(c_voidp) == 8:
                moway = cdll.LoadLibrary("../lib/libmowayx64.dll")
        else:
                moway = cdll.LoadLibrary("../lib/libmoway.dll")
elif os.uname()[1] == "raspberrypi":
	moway = cdll.LoadLibrary('../lib/libmoway_PI.so')

else:
	if sizeof(c_voidp) == 8:
        	moway = cdll.LoadLibrary('../lib/libmowayamd64.so')
	else:
		moway = cdll.LoadLibrary('../lib/libmoway.so')

#define float return in acceleromter functions
moway.get_accel_X.restype = c_float
moway.get_accel_Y.restype = c_float
moway.get_accel_Z.restype = c_float

#define exit function
def exit_mow():
        moway.close_moway()
        moway.exit_moway()

#Actions Movement
CMD_GO  	    = 0xE1
CMD_BACK            = 0xE2
CMD_GOLEFT          = 0xE3
CMD_GORIGHT         = 0xE4
CMD_BACKLEFT        = 0xE6
CMD_BACKRIGHT	    = 0xE5
CMD_STOP            = 0xE7
CMD_ROTATELEFT      = 0xE8
CMD_ROTATERIGHT     = 0xE9
CMD_GO_SIMPLE       = 0xEA
CMD_BACK_SIMPLE     = 0xEB
CMD_LEFT_SIMPLE     = 0xEC
CMD_RIGHT_SIMPLE    = 0xED
CMD_TURN_AROUND     = 0xEE
CMD_RESET_DIST      = 0xEF

#Actions LEDs
CMD_FRONTLEDON      = 0xA0
CMD_FRONTLEDOFF     = 0xA4
CMD_GREENLEDON      = 0xA2
CMD_GREENLEDOFF     = 0xA6
CMD_BRAKELEDON      = 0xA1
CMD_BRAKELEDOFF     = 0xA5
CMD_REDLEDON        = 0xA3
CMD_REDLEDOFF       = 0xA7
CMD_FRONTBLINK      = 0xA8
CMD_BRAKEBLINK      = 0xA9
CMD_GREENBLINK      = 0xAA
CMD_REDBLINK        = 0xAB
CMD_LEDSON          = 0xAC
CMD_LEDSOFF         = 0xAD
CMD_LEDSBLINK       = 0xAE

# Actions Sound
CMD_BUZZERON        = 0xC0
CMD_BUZZEROFF       = 0xC1
CMD_MELODYCHARGE    = 0xC2
CMD_MELODYFAIL      = 0xC3

#Actions Complex
CMD_LINE_FOLLOW_L   = 0x91
CMD_LINE_FOLLOW_R   = 0x92
CMD_PUSH            = 0x95

#rotation-axis
WHEEL               = 0x00
CENTER              = 0x01
