#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

from collections import deque
import itertools

import logging
import epd2in13b_V4
import time
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)

def createImageFromOptions(question, imagename, **options):
    font20 = ImageFont.truetype('fonts/Font.ttc', 20)
    font18 = ImageFont.truetype('fonts/Font.ttc', 18)
    imageToDisplay = Image.new('1', (250, 122), 255)  # 250*122
    drawblack = ImageDraw.Draw(imageToDisplay)
    drawblack.text((125, 15), question, font = font20, fill = 0, anchor = 'mm', align = 'center')
    drawblack.line((0, 30, 250, 30), fill = 0)
    optionsKeys = iter(options)
    if len(options) == 1:
        drawblack.rectangle((50, 50, 200, 100), outline = 0)
        drawblack.text((125, 75), options[next(optionsKeys)], font = font18, fill = 0, anchor = 'mm', align = 'center')
    elif len(options) == 2:
        drawblack.rectangle((20, 50, 115, 102), outline = 0)
        drawblack.text((68, 76), options[next(optionsKeys)], font = font18, fill = 0, anchor = 'mm', align = 'center')
        drawblack.rectangle((135, 50, 230, 102), outline = 0)
        drawblack.text((182, 76), options[next(optionsKeys)], font = font18, fill = 0, anchor = 'mm', align = 'center')
    elif len(options) == 3:
        drawblack.rectangle((21, 50, 77, 102), outline = 0)
        drawblack.text((49, 76), options[next(optionsKeys)], font = font18, fill = 0, anchor = 'mm', align = 'center')
        drawblack.rectangle((97, 50, 153, 102), outline = 0)
        drawblack.text((125, 76), options[next(optionsKeys)], font = font18, fill = 0, anchor = 'mm', align = 'center')
        drawblack.rectangle((173, 50, 229, 102), outline = 0)
        drawblack.text((201, 76), options[next(optionsKeys)], font = font18, fill = 0, anchor = 'mm', align = 'center')
    elif len(options) == 4:
        drawblack.rectangle((6, 50, 61, 102), outline = 0)
        drawblack.text((33, 76), options[next(optionsKeys)], font = font18, fill = 0, anchor = 'mm', align = 'center')
        drawblack.rectangle((67, 50, 122, 102), outline = 0)
        drawblack.text((94, 76), options[next(optionsKeys)], font = font18, fill = 0, anchor = 'mm', align = 'center')
        drawblack.rectangle((128, 50, 183, 102), outline = 0)
        drawblack.text((155, 76), options[next(optionsKeys)], font = font18, fill = 0, anchor = 'mm', align = 'center')
        drawblack.rectangle((189, 50, 244, 102), outline = 0)
        drawblack.text((216, 76), options[next(optionsKeys)], font = font18, fill = 0, anchor = 'mm', align = 'center')
    else:
        
        optionsKeys = itertools.cycle(optionsKeys)
        for i in range(len(options)-2): next(optionsKeys)
        for i in range(len(options)):
            drawblack.rectangle((-26 + (62*i), 50, 26 + (62*i), 102), outline = 0)
            drawblack.text(((62*i), 76), options[next(optionsKeys)], font = font18, fill = 0, anchor = 'mm', align = 'center')
    imageToDisplay.save(imagename+".jpg", "JPEG")
    return imageToDisplay

try:
    logging.info("epd2in13b_V4 Demo")
    
    # epd = epd2in13b_V4.EPD()
    # logging.info("init and Clear")
    # epd.init()
    # epd.Clear()
    # time.sleep(1)
    
    # Drawing on the image
    logging.info("Drawing")    
    font20 = ImageFont.truetype('fonts/Font.ttc', 20)
    font18 = ImageFont.truetype('fonts/Font.ttc', 18)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...") 
    # HBlackimage = Image.new('1', (250, 122), 255)  # 250*122
    # HRYimage = Image.new('1', (250, 122), 255)  # 250*122
    # drawblack = ImageDraw.Draw(HBlackimage)
    # drawry = ImageDraw.Draw(HRYimage)
    # drawblack.text((125, 15), 'Launch in wifi mode?', font = font20, fill = 0, anchor = 'mm', align = 'center')
    # drawblack.line((0, 30, 250, 30), fill = 0)
    # # drawblack.text((120, 0), u'微雪电子', font = font20, fill = 0)    
    # drawblack.line((20, 50, 70, 100), fill = 0)
    # drawblack.line((70, 50, 20, 100), fill = 0)
    # drawblack.rectangle((20, 50, 70, 100), outline = 0)    
    # drawry.line((165, 50, 165, 100), fill = 0)
    # drawry.line((140, 75, 190, 75), fill = 0)
    # drawry.arc((140, 50, 190, 100), 0, 360, fill = 0)
    # drawry.rectangle((80, 50, 130, 100), fill = 0)
    # drawry.chord((85, 55, 125, 95), 0, 360, fill =1)
    # HBlackimage.save("drawblack.jpg", "JPEG")
    # HRYimage.save("drawry.jpg", "JPEG")
    # epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
    createImageFromOptions("Launch in wifi mode?", "oneoption", option1="Yes")
    createImageFromOptions("Launch in wifi mode?", "twooptions", option1="Yes", option2="No")
    createImageFromOptions("Launch in wifi mode?", "threeoptions", option1="Yes", option2="No", option3="Maybe")
    createImageFromOptions("Launch in wifi mode?", "fouroptions", option1="Yes", option2="No", option3="Maybe", option4="Idk")
    createImageFromOptions("Launch in wifi mode?", "fiveoptions", option1="Yes", option2="No", option3="Maybe", option4="Idk", option5="Maybe\nnot")
    createImageFromOptions("Launch in wifi mode?", "sixoptions", option1="Yes", option2="No", option3="Maybe", option4="Idk", option5="Maybe\nnot", option6="Maybe\nyes")


    time.sleep(2)
    
    # logging.info("Clear...")
    # epd.init()
    # epd.clear()
    
    # logging.info("Goto Sleep...")
    # epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13b_V4.epdconfig.module_exit(cleanup=True)
    exit()

