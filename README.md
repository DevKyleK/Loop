# LoopStack
Loop is a system built on the M5Stack for people to use as a "mini" operating system it includes games and apps submitted by the community and is constantly being updated

# How to add your apps...

Lets get started:
  - Submit a request on our github containing the following

> [APP TITLE]
> [APP LISTING]
> [APP VERSION]
> [APP OWNER]
> [APP CODE]

Heres an example:
> ```sh
> [APP TITLE] Text Example
> [APP LISTING GAMES/ART/UTILITY/MANAGE/OTHER/TESTS] Tests  
> [APP VERSION] 0.1
> [APP OWNER] ImKyleJK
> [APP CODE] 
> 
> from m5stack import *
> from m5ui import *
> from uiflow import *
> setScreenColor(0x222222)
> label0 = M5TextBox(142, 104, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0) 
> ```
