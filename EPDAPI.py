#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

from collections import deque
import itertools
import globalvars
import logging
import epd2in13_V4
import time
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)

def createKeyboardFromPrompt(question):
    font11 = ImageFont.truetype('fonts/Font.ttc', 11)
    imageToDisplay = Image.open('kb.jpg')  # 250*122
    draw = ImageDraw.Draw(imageToDisplay)
    draw.text((125, 15), question, font = font11, fill = 0, anchor = 'mm', align = 'center')
    globalvars.epd.displayPartBaseImage(globalvars.epd.getbuffer(imageToDisplay))
    return imageToDisplay
    

def updateKeyboardFromPrompt(baseImage, coords):
    chars = [list('ABCDEFGHIJKLM!@#$%^'),list('NOPQRSTUVWXYZ&*()-_'),list('abcdefghijklm+=~`[]'),list('nopqrstuvwxyz{}|\\:;'),list('0123456789"\'<>,.?/ ')]
    font11 = ImageFont.truetype('fonts/Font.ttc', 11)
    char = chars[coords[0]][coords[1]]
    coords = (2+13*coords[1], 56+13*coords[0], 14+13*coords[1], 68+13*coords[0])
    draw = ImageDraw.Draw(baseImage)
    draw.text((coords[0]+7, coords[1]+7), char, font = font11, fill = 255, anchor = 'mm', align = 'center')
    draw.rectangle(coords, outline = 0,fill = 0)
    globalvars.epd.displayPartial(globalvars.epd.getbuffer(baseImage))



def createImageFromOptions(question, options):
    font20 = ImageFont.truetype('fonts/Font.ttc', 20)
    font18 = ImageFont.truetype('fonts/Font.ttc', 18)
    imageToDisplay = Image.new('1', (250, 122), 255)  # 250*122
    drawblack = ImageDraw.Draw(imageToDisplay)
    drawblack.text((125, 15), question, font = font20, fill = 0, anchor = 'mm', align = 'center')
    drawblack.line((0, 30, 250, 30), fill = 0)
    optionsKeys = iter(options)
    if len(options) == 1:
        drawblack.rectangle((50, 50, 200, 100), outline = 0)
        drawblack.text((125, 75), next(optionsKeys), font = font18, fill = 0, anchor = 'mm', align = 'center')
    elif len(options) == 2:
        drawblack.rectangle((20, 50, 115, 102), outline = 0)
        drawblack.text((68, 76), next(optionsKeys), font = font18, fill = 0, anchor = 'mm', align = 'center')
        drawblack.rectangle((135, 50, 230, 102), outline = 0)
        drawblack.text((182, 76), next(optionsKeys), font = font18, fill = 0, anchor = 'mm', align = 'center')
    elif len(options) == 3:
        drawblack.rectangle((21, 50, 77, 102), outline = 0)
        drawblack.text((49, 76), next(optionsKeys), font = font18, fill = 0, anchor = 'mm', align = 'center')
        drawblack.rectangle((97, 50, 153, 102), outline = 0)
        drawblack.text((125, 76), next(optionsKeys), font = font18, fill = 0, anchor = 'mm', align = 'center')
        drawblack.rectangle((173, 50, 229, 102), outline = 0)
        drawblack.text((201, 76), next(optionsKeys), font = font18, fill = 0, anchor = 'mm', align = 'center')
    elif len(options) == 4:
        drawblack.rectangle((6, 50, 61, 102), outline = 0)
        drawblack.text((33, 76), next(optionsKeys), font = font18, fill = 0, anchor = 'mm', align = 'center')
        drawblack.rectangle((67, 50, 122, 102), outline = 0)
        drawblack.text((94, 76), next(optionsKeys), font = font18, fill = 0, anchor = 'mm', align = 'center')
        drawblack.rectangle((128, 50, 183, 102), outline = 0)
        drawblack.text((155, 76), next(optionsKeys), font = font18, fill = 0, anchor = 'mm', align = 'center')
        drawblack.rectangle((189, 50, 244, 102), outline = 0)
        drawblack.text((216, 76), next(optionsKeys), font = font18, fill = 0, anchor = 'mm', align = 'center')
    else:
        
        optionsKeys = itertools.cycle(optionsKeys)
        for i in range(len(options)-2): next(optionsKeys)
        for i in range(len(options)):
            drawblack.rectangle((-26 + (62*i), 50, 26 + (62*i), 102), outline = 0)
            drawblack.text(((62*i), 76), next(optionsKeys), font = font18, fill = 0, anchor = 'mm', align = 'center')
    globalvars.epd.display(globalvars.epd.getbuffer(imageToDisplay))
    return imageToDisplay

try:
    pass
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V4.epdconfig.module_exit(cleanup=True)
    exit()

