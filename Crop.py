#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 03:19:06 2021

@author: tareque
"""


import tkinter.messagebox
import MyMenu


class Crop:
    
    #declaring variables
    menu = MyMenu.Menu()
    
    
    def crop(self, canvas):     #this is the main function of this class, reat of them are assets
        canvas.data.colourPopToHappen = False
        canvas.data.drawOn = False
        canvas.data.cropPopToHappen = True
        tkinter.messagebox.showinfo(title="Crop", \
                                    message="Draw cropping rectangle and press Enter", \
                              parent=canvas.data.mainWindow)
        if canvas.data.image != None:
            canvas.data.mainWindow.bind("<ButtonPress-1>", \
                                        lambda event: self.startCrop(event, canvas))
            canvas.data.mainWindow.bind("<B1-Motion>", \
                                        lambda event: self.drawCrop(event, canvas))
            canvas.data.mainWindow.bind("<ButtonRelease-1>", \
                                        lambda event: self.endCrop(event, canvas))
                

    def startCrop( self, event, canvas):
        if canvas.data.endCrop == False and canvas.data.cropPopToHappen == True:
            canvas.data.startCropX = event.x
            canvas.data.startCropY = event.y
            
            
        
    def drawCrop(self, event, canvas):
        if canvas.data.endCrop == False and canvas.data.cropPopToHappen == True:
            canvas.data.tempCropX = event.x
            canvas.data.tempCropY = event.y
            canvas.create_rectangle(canvas.data.startCropX, \
                                    canvas.data.startCropY,
                                    canvas.data.tempCropX, \
                                    canvas.data.tempCropY, fill="red", stipple="gray75", width=0)
                
            
            
    def endCrop(self, event, canvas):
        if canvas.data.cropPopToHappen == True:
            canvas.data.endCrop = True
            canvas.data.endCropX = event.x
            canvas.data.endCropY = event.y
            canvas.create_rectangle(canvas.data.startCropX, \
                                    canvas.data.startCropY,
                                    canvas.data.endCropX, \
                                    canvas.data.endCropY, fill="green", stipple="gray75", width=0)
            canvas.data.mainWindow.bind("<Return>", \
                                        lambda event: self.performCrop(event, canvas))


    def performCrop(self, event, canvas):
        canvas.data.image = \
            canvas.data.image.crop( \
                (int(round((canvas.data.startCropX - canvas.data.imageTopX) * canvas.data.imageScale)),
                 int(round((canvas.data.startCropY - canvas.data.imageTopY) * canvas.data.imageScale)),
                 int(round((canvas.data.endCropX - canvas.data.imageTopX) * canvas.data.imageScale)),
                 int(round((canvas.data.endCropY - canvas.data.imageTopY) * canvas.data.imageScale))))
        canvas.data.endCrop = False
        canvas.data.cropPopToHappen = False
        self.menu.save(canvas)
        canvas.data.undoQueue.append(canvas.data.image.copy())
        canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
        self.menu.drawImage(canvas)  
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            