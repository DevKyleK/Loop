#######################
#   Loader Example 1  #
#######################
# Code Version 0.0.0  #
#######################
# _                   #
#| | ___   ___  _ __  #
#| |/ _ \ / _ \| '_ \ #
#| | (_) | (_) | |_) |#
#|_|\___/ \___/| .__/ #
#              |_|    #
#######################
from m5stack import *
from m5ui import *
from uiflow import *
import time

setScreenColor(0x222222)





bar2 = M5Rect(155, 90, 10, 60, 0xFFFFFF, 0xFFFFFF)
bar1 = M5Rect(130, 105, 10, 30, 0xFFFFFF, 0xFFFFFF)
bar3 = M5Rect(180, 105, 10, 30, 0xFFFFFF, 0xFFFFFF)


bar1.show()
bar2.show()
bar3.show()
bar1.setBgColor(0x000000)
bar2.setBgColor(0x000000)
bar3.setBgColor(0x000000)
wait(1)
bar1.setBgColor(0xffffff)
wait(1)
bar2.setBgColor(0xffffff)
wait(1)
bar3.setBgColor(0xffffff)
