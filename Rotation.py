#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 03:27:08 2021

@author: tareque
"""







from tkinter import Toplevel, Scale, HORIZONTAL, Frame, Button, BOTTOM






import MyMenu




class Rotation:
    
    
    #declaring variables
    
    menu = MyMenu.Menu()
    
    
    def rotate(self, canvas):
        canvas.data.colourPopToHappen = False
        canvas.data.cropPopToHappen = False
        canvas.data.drawOn = False
        rotateWindow = Toplevel(canvas.data.mainWindow)
        rotateWindow.title("Rotate")
        rotateSlider = Scale(rotateWindow, from_=0, to=360, orient=HORIZONTAL)
        rotateSlider.pack()
        OkRotateFrame = Frame(rotateWindow)
        OkRotateButton = Button(OkRotateFrame, text="OK", \
                                command=lambda: self.closeRotateWindow(canvas))
        OkRotateButton.grid(row=0, column=0)
        OkRotateFrame.pack(side=BOTTOM)
        self.rotateFinished(canvas, rotateWindow, rotateSlider, 0)
    
    
    
    
    
    def rotateFinished(self, canvas, rotateWindow, rotateSlider, previousAngle):
        if canvas.data.rotateWindowClose == True:
            rotateWindow.destroy()
            canvas.data.rotateWindowClose = False
        else:
            if canvas.data.image != None and rotateWindow.winfo_exists():
                canvas.data.angleSelected = rotateSlider.get()
                if canvas.data.angleSelected != None and \
                        canvas.data.angleSelected != previousAngle:
                    canvas.data.image = \
                        canvas.data.image.rotate(float(canvas.data.angleSelected))
                    canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
                    self.menu.drawImage(canvas)
            canvas.after(200, lambda: self.rotateFinished(canvas, \
                                                     rotateWindow, rotateSlider, canvas.data.angleSelected))


    def closeRotateWindow(self, canvas):
        if canvas.data.image != None:
            self.menu.save(canvas)
            canvas.data.undoQueue.append(canvas.data.image.copy())
            canvas.data.rotateWindowClose = True


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    