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

def createImageFromButtons(appName, commandNames):
    font20 = ImageFont.truetype('fonts/Font.ttc', 20)
    font18 = ImageFont.truetype('fonts/Font.ttc', 12)
    imageToDisplay = Image.open('commandDisplayBase.jpg')  # 250*122
    drawblack = ImageDraw.Draw(imageToDisplay)
    drawblack.text((125, 15), appName, font = font20, fill = 0, anchor = 'mm', align = 'center')
    for button in commandNames:
        if button == "IT":
            drawblack.text((32, 68), commandNames[button].__name__, font = font18, fill = 0, anchor = 'mm', align = 'center')
        elif button == "IM":
            drawblack.text((32, 88), commandNames[button].__name__, font = font18, fill = 0, anchor = 'mm', align = 'center')
        elif button == "IB":
            drawblack.text((32, 108), commandNames[button].__name__, font = font18, fill = 0, anchor = 'mm', align = 'center')
        elif button == "MT":
            drawblack.text((94, 68), commandNames[button].__name__, font = font18, fill = 0, anchor = 'mm', align = 'center')
        elif button == "MM":
            drawblack.text((94, 88), commandNames[button].__name__, font = font18, fill = 0, anchor = 'mm', align = 'center')
        elif button == "MB":
            drawblack.text((94, 108), commandNames[button].__name__, font = font18, fill = 0, anchor = 'mm', align = 'center')
        elif button == "RT":
            drawblack.text((156, 68), commandNames[button].__name__, font = font18, fill = 0, anchor = 'mm', align = 'center')
        elif button == "RM":
            drawblack.text((156, 88), commandNames[button].__name__, font = font18, fill = 0, anchor = 'mm', align = 'center')
        elif button == "RB":
            drawblack.text((156, 108), commandNames[button].__name__, font = font18, fill = 0, anchor = 'mm', align = 'center')
        elif button == "PT":
            drawblack.text((220, 68), commandNames[button].__name__, font = font18, fill = 0, anchor = 'mm', align = 'center')
        elif button == "PB":
            drawblack.text((220, 108), commandNames[button].__name__, font = font18, fill = 0, anchor = 'mm', align = 'center')
    globalvars.epd.display(globalvars.epd.getbuffer(imageToDisplay))

    
    

def updateKeyboardFromPrompt(baseImage, coords, direction):
    chars = [list('ABCDEFGHIJKLM!@#$%^'),list('NOPQRSTUVWXYZ&*()-_'),list('abcdefghijklm+=~`[]'),list('nopqrstuvwxyz{}|\\:;'),list('0123456789"\'<>,.?/ ')]
    font11 = ImageFont.truetype('fonts/Font.ttc', 11)
    char = chars[coords[0]][coords[1]]
    draw = ImageDraw.Draw(baseImage)
    draw.rectangle((2+13*coords[1], 56+13*coords[0], 14+13*coords[1], 68+13*coords[0]), outline = 0,fill = 0)
    draw.text((2+13*coords[1]+7, 56+13*coords[0]+7), char, font = font11, fill = 255, anchor = 'mm', align = 'center')

    match direction:
        case 'up':
            coords = ((coords[0]+1) % 5, coords[1])
        case 'down':
            coords = ((coords[0]-1) % 5, coords[1])
        case 'left':
            coords = (coords[0], (coords[1]+1)%19)
        case 'right':
            coords = (coords[0], (coords[1]-1)%19)
    
    char = chars[coords[0]][coords[1]]
    draw.rectangle((2+13*coords[1], 56+13*coords[0], 14+13*coords[1], 68+13*coords[0]), outline = 0, fill = 255)
    draw.text((2+13*coords[1]+7, 56+13*coords[0]+7), char, font = font11, fill = 0, anchor = 'mm', align = 'center')
    globalvars.epd.displayPartial(globalvars.epd.getbuffer(baseImage))

def createNumpadFromPrompt(question):
    font11 = ImageFont.truetype('fonts/Font.ttc', 11)
    imageToDisplay = Image.open('np.jpg')  
    draw = ImageDraw.Draw(imageToDisplay)
    draw.text((125, 15), question, font = font11, fill = 0, anchor = 'mm', align = 'center')
    globalvars.epd.display(globalvars.epd.getbuffer(imageToDisplay))


def createImageFromOptions(question, options):
    font20 = ImageFont.truetype('fonts/Font.ttc', 20)
    font18 = ImageFont.truetype('fonts/Font.ttc', 12)
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

