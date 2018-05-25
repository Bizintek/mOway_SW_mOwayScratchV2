import blockext
from blockext import *
import sys, atexit , msvcrt
from time import sleep

sys.path.append("../lib/")
sys.path.append("blocks_scratch_interface")

from moway_lib import *

from lib_sen_leds import *
from lib_sen_obstac import *
from lib_sen_line import *
from lib_sen_light import *
from lib_mot_moway import *
from lib_accel_moway import *
from lib_speaker_moway import *
from lib_sen_light import *
from lib_sen_volume import *


if __name__ == "__main__":
    blockext.run("Moway", "ufo", 1234)
