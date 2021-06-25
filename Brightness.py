#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 03:30:47 2021

@author: tareque
"""


from tkinter import Toplevel, Scale, HORIZONTAL, Frame, Button, BOTTOM
import MyMenu


class Brightness:
    
    menu = MyMenu.Menu()
    
    def closeBrightnessWindow(self, canvas):
        if canvas.data.image != None:
            self.menu.save(canvas)
            canvas.data.undoQueue.append(canvas.data.image.copy())
            canvas.data.brightnessWindowClose = True


    def changeBrightness(self, canvas, brightnessWindow, brightnessSlider, \
                         previousVal):
        if canvas.data.brightnessWindowClose == True:
            brightnessWindow.destroy()
            canvas.data.brightnessWindowClose = False
    
        else:
            if canvas.data.image != None and brightnessWindow.winfo_exists():
                sliderVal = brightnessSlider.get()
                scale = (sliderVal - previousVal) / 100.0
                canvas.data.image = canvas.data.image.point(
                    lambda i: i + int(round(i * scale)))
                canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
                self.menu.drawImage(canvas)
                canvas.after(200,
                             lambda: self.changeBrightness(canvas, brightnessWindow,
                                                      brightnessSlider, sliderVal))


    def brightness(self, canvas):
        canvas.data.colourPopToHappen = False
        canvas.data.cropPopToHappen = False
        canvas.data.drawOn = False
        brightnessWindow = Toplevel(canvas.data.mainWindow)
        brightnessWindow.title("Brightness")
        brightnessSlider = Scale(brightnessWindow, from_=-100, to=100,
                                 orient=HORIZONTAL)
        brightnessSlider.pack()
        OkBrightnessFrame = Frame(brightnessWindow)
        OkBrightnessButton = Button(OkBrightnessFrame, text="OK",
                                    command=lambda: self.closeBrightnessWindow(canvas))
        OkBrightnessButton.grid(row=0, column=0)
        OkBrightnessFrame.pack(side=BOTTOM)
        self.changeBrightness(canvas, brightnessWindow, brightnessSlider, 0)
        brightnessSlider.set(0)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        