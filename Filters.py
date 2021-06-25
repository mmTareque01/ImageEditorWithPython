#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 03:33:51 2021

@author: tareque
"""


from tkinter import Toplevel, HORIZONTAL, Scale, Frame, Button, BOTTOM
from PIL import ImageOps
import MyMenu






class Filters:
    
    menu = MyMenu.Menu()
    
    
    def covertGray(self, canvas):
        canvas.data.colourPopToHappen = False
        canvas.data.cropPopToHappen = False
        canvas.data.drawOn = False
        if canvas.data.image != None:
            data = []
            for col in range(canvas.data.image.size[1]):
                for row in range(canvas.data.image.size[0]):
                    r, g, b = canvas.data.image.getpixel((row, col))
                    avg = int(round((r + g + b) / 3.0))
                    R, G, B = avg, avg, avg
                    data.append((R, G, B))
            canvas.data.image.putdata(data)
            self.menu.save(canvas)
            canvas.data.undoQueue.append(canvas.data.image.copy())
            canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
            self.menu.drawImage(canvas)


    def sepia(self, canvas):
        canvas.data.colourPopToHappen = False
        canvas.data.cropPopToHappen = False
        canvas.data.drawOn = False
        if canvas.data.image != None:
            sepiaData = []
            for col in range(canvas.data.image.size[1]):
                for row in range(canvas.data.image.size[0]):
                    r, g, b = canvas.data.image.getpixel((row, col))
                    avg = int(round((r + g + b) / 3.0))
                    R, G, B = avg + 100, avg + 50, avg
                    sepiaData.append((R, G, B))
            canvas.data.image.putdata(sepiaData)
            self.menu.save(canvas)
            canvas.data.undoQueue.append(canvas.data.image.copy())
            canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
            self.menu.drawImage(canvas)


    def invert(self, canvas):
        canvas.data.colourPopToHappen = False
        canvas.data.cropPopToHappen = False
        canvas.data.drawOn = False
        if canvas.data.image != None:
            canvas.data.image = ImageOps.invert(canvas.data.image)
            self.menu.save(canvas)
            canvas.data.undoQueue.append(canvas.data.image.copy())
            canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
            self.menu.drawImage(canvas)
    
    
    def solarize(self, canvas):
        canvas.data.colourPopToHappen = False
        canvas.data.cropPopToHappen = False
        solarizeWindow = Toplevel(canvas.data.mainWindow)
        solarizeWindow.title("Solarize")
        solarizeSlider = Scale(solarizeWindow, from_=0, to=255, orient=HORIZONTAL)
        solarizeSlider.pack()
        OkSolarizeFrame = Frame(solarizeWindow)
        OkSolarizeButton = Button(OkSolarizeFrame, text="OK", \
                                  command=lambda: self.closeSolarizeWindow(canvas))
        OkSolarizeButton.grid(row=0, column=0)
        OkSolarizeFrame.pack(side=BOTTOM)
        self.performSolarize(canvas, solarizeWindow, solarizeSlider, 255)
    
    
    def performSolarize(self, canvas, solarizeWindow, solarizeSlider, previousThreshold):
        if canvas.data.solarizeWindowClose == True:
            solarizeWindow.destroy()
            canvas.data.solarizeWindowClose = False
    
        else:
            if solarizeWindow.winfo_exists():
                sliderVal = solarizeSlider.get()
                threshold_ = 255 - sliderVal
                if canvas.data.image != None and threshold_ != previousThreshold:
                    canvas.data.image = ImageOps.solarize(canvas.data.image, \
                                                          threshold=threshold_)
                    canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
                    self.menu.drawImage(canvas)
                canvas.after(200, lambda: self.performSolarize(canvas, \
                                                          solarizeWindow, solarizeSlider, threshold_))
    
    
    def closeSolarizeWindow(self, canvas):
        if canvas.data.image != None:
            self.menu.save(canvas)
            canvas.data.undoQueue.append(canvas.data.image.copy())
            canvas.data.solarizeWindowClose = True
    
    
    def posterize(self, canvas):
        canvas.data.colourPopToHappen = False
        canvas.data.cropPopToHappen = False
        canvas.data.drawOn = False
        posterData = []
        if canvas.data.image != None:
            for col in range(canvas.data.imageSize[1]):
                for row in range(canvas.data.imageSize[0]):
                    r, g, b = canvas.data.image.getpixel((row, col))
                    if r in range(32):
                        R = 0
                    elif r in range(32, 96):
                        R = 64
                    elif r in range(96, 160):
                        R = 128
                    elif r in range(160, 224):
                        R = 192
                    elif r in range(224, 256):
                        R = 255
                    if g in range(32):
                        G = 0
                    elif g in range(32, 96):
                        G = 64
                    elif g in range(96, 160):
                        G = 128
                    elif r in range(160, 224):
                        g = 192
                    elif r in range(224, 256):
                        G = 255
                    if b in range(32):
                        B = 0
                    elif b in range(32, 96):
                        B = 64
                    elif b in range(96, 160):
                        B = 128
                    elif b in range(160, 224):
                        B = 192
                    elif b in range(224, 256):
                        B = 255
                    posterData.append((R, G, B))
            canvas.data.image.putdata(posterData)
            self.menu.save(canvas)
            canvas.data.undoQueue.append(canvas.data.image.copy())
            canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
            self.menu.drawImage(canvas)
            
            
            
            
            
            
            
            
            
            
            
