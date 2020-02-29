# encoding :utf-8
import os
from PIL import Image
import time

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

adb='/Users/bondsam/Desktop/platform-tools/adb'

def pull_screenshot(num):
    os.system(adb+' shell screencap -p /sdcard/screenshot'+num+'.png')
    os.system(adb+' pull /sdcard/screenshot'+num+'.png '+'/Users/bondsam/Desktop/game/screenshot'+num+'.png')
    os.system(adb+' shell rm /sdcard/screenshot'+num+'.png')
    #time.sleep(0.1)
    print('pull success!')

#time.sleep(2)
white = (255,255,255)
pixel = [(137,1060), (400,1160), (680,1160), (950,1160)]


while (True):

    pull_screenshot('1')
    im = Image.open('/Users/bondsam/Desktop/game/screenshot1.png')
    rgb_im = im.convert('RGB')
    res = [rgb_im.getpixel(pixel[0]), rgb_im.getpixel(pixel[1]), rgb_im.getpixel(pixel[2]), rgb_im.getpixel(pixel[3])]

    if res[0] != white:
    	os.system(adb+' shell input tap 137 1260')
    	print('position 0 tapped')
    	#time.sleep(0.05)
    	continue
    elif res[1] != white:
    	os.system(adb+' shell input tap 400 1260')
    	print('position 1 tapped')
    	#time.sleep(0.05)
    	continue
    elif res[2] != white:
    	os.system(adb+' shell input tap 680 1260')
    	print('position 2 tapped')
    	#time.sleep(0.05)
    	continue
    elif res[3] != white:
    	os.system(adb+' shell input tap 950 1260')
    	print('position 3 tapped')
    	#time.sleep(0.05)
    	continue


