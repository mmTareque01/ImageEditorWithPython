#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 03:46:45 2021

@author: tareque
"""




from tkinter import *

from collections import *
import Crop
import Rotation
import Brightness
import Assets
import Mirror
import Flip
import Reset
import MyMenu
import Moving
import Filters

class Initializer:
    
    crop = Crop.Crop()
    rotation = Rotation.Rotation()
    brightness = Brightness.Brightness()
    assets = Assets.Assets()
    mirror = Mirror.Mirror()
    flip = Flip.Flip()
    reset = Reset.Reset()
    menu = MyMenu.Menu()
    moving = Moving.Moving()
    filters = Filters.Filters()
    
    
    def init(self, root, canvas):
        self.buttonsInit(root, canvas)
        self.menuInit(root, canvas)
        canvas.data.image = None
        canvas.data.angleSelected = None
        canvas.data.rotateWindowClose = False
        canvas.data.brightnessWindowClose = False
        canvas.data.brightnessLevel = None
        canvas.data.histWindowClose = False
        canvas.data.solarizeWindowClose = False
        canvas.data.posterizeWindowClose = False
        canvas.data.colourPopToHappen = False
        canvas.data.cropPopToHappen = False
        canvas.data.endCrop = False
        canvas.data.drawOn = True
    
        canvas.data.undoQueue = deque([], 10)
        canvas.data.redoQueue = deque([], 10)
        canvas.pack()
    
    
    def buttonsInit(self, root, canvas):
        backgroundColour = "white"
        buttonWidth = 14
        buttonHeight = 2
        toolKitFrame = Frame(root)
        cropButton = Button(toolKitFrame, text="Crop",
                            background=backgroundColour, \
                            width=buttonWidth, height=buttonHeight, \
                            command=lambda: self.crop.crop(canvas))
        cropButton.grid(row=0, column=0)
        rotateButton = Button(toolKitFrame, text="Rotate", \
                              background=backgroundColour, \
                              width=buttonWidth, height=buttonHeight, \
                              command=lambda: self.rotation.rotate(canvas))
        rotateButton.grid(row=1, column=0)
        brightnessButton = Button(toolKitFrame, text="Brightness", \
                                  background=backgroundColour, \
                                  width=buttonWidth, height=buttonHeight, \
                                  command=lambda: self.brightness.brightness(canvas))
        brightnessButton.grid(row=2, column=0)
        colourPopButton = Button(toolKitFrame, text="Colour Pop", \
                                 background=backgroundColour, \
                                 width=buttonWidth, height=buttonHeight, \
                                 command=lambda: self.assets.colourPop(canvas))
        colourPopButton.grid(row=4, column=0)
        mirrorButton = Button(toolKitFrame, text="Mirror", \
                              background=backgroundColour, \
                              width=buttonWidth, height=buttonHeight, \
                              command=lambda: self.mirror.mirror(canvas))
        mirrorButton.grid(row=5, column=0)
        flipButton = Button(toolKitFrame, text="Flip", \
                            background=backgroundColour, \
                            width=buttonWidth, height=buttonHeight, \
                            command=lambda: self.flip.flip(canvas))
        flipButton.grid(row=6, column=0)
        resetButton = Button(toolKitFrame, text="Reset", \
                             background=backgroundColour, width=buttonWidth, \
                             height=buttonHeight, command=lambda: self.reset.reset(canvas))
        resetButton.grid(row=9, column=0)
        toolKitFrame.pack(side=LEFT)
    
    
    def menuInit(self, root, canvas):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=lambda: self.menu.newImage(canvas))
        filemenu.add_command(label="Save", command=lambda: self.menu.save(canvas))
        filemenu.add_command(label="Save As", command=lambda: self.menu.saveAs(canvas))
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)
        ## Edit pull-down Menu
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo   Ctrl+Z", command=lambda: self.moving.undo(canvas))
        editmenu.add_command(label="Redo   Ctrl+Y", command=lambda: self.moving.redo(canvas))
        menubar.add_cascade(label="Edit", menu=editmenu)
        root.config(menu=menubar)
        ## Filter pull-down Menu
        filtermenu = Menu(menubar, tearoff=0)
        filtermenu.add_command(label="Black and White",
                               command=lambda: self.filters.covertGray(canvas))
        filtermenu.add_command(label="Sepia",
                               command=lambda: self.filters.sepia(canvas))
        filtermenu.add_command(label="Invert",
                               command=lambda: self.filters.invert(canvas))
        filtermenu.add_command(label="Solarize",
                               command=lambda: self.filters.solarize(canvas))
        filtermenu.add_command(label="Posterize",
                               command=lambda: self.filters.posterize(canvas))
        menubar.add_cascade(label="Filter", menu=filtermenu)
        root.config(menu=menubar)
    
    
    def run(self):
        root = Tk()
        root.title("Image Editor")
        canvasWidth = 500
        canvasHeight = 500
        canvas = Canvas(root, width=canvasWidth, height=canvasHeight, \
                        background="gray")
    
        class Struct: pass
    
        canvas.data = Struct()
        canvas.data.width = canvasWidth
        canvas.data.height = canvasHeight
        canvas.data.mainWindow = root
        self.init(root, canvas)
        root.bind("<Control-z>", lambda event: self.moving.undo(canvas))
        root.bind("<Control-y>", lambda event: self.moving.redo(canvas))
        root.mainloop()

    