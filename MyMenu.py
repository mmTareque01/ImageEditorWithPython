#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 03:37:43 2021

@author: tareque
"""
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from PIL import ImageOps
import imghdr
from collections import *





class Menu:
    def saveAs(self, canvas):
        if canvas.data.image != None:
            filename = tkinter.filedialog.asksaveasfilename(defaultextension=".jpg")
            im = canvas.data.image
            im.save(filename)
    
    
    def save(self, canvas):
        if canvas.data.image != None:
            im = canvas.data.image
            im.save(canvas.data.imageLocation)
    
    
    def newImage(self, canvas):
        imageName = filedialog.askopenfilename()
        filetype = ""
        try:
            filetype = imghdr.what(imageName)
        except:
            tkinter.messagebox.showinfo(title="Image File", \
                                  message="Choose an Image File!", parent=canvas.data.mainWindow)
        if filetype in ['jpeg', 'bmp', 'png', 'tiff']:
            canvas.data.imageLocation = imageName
            im = Image.open(imageName)
            canvas.data.image = im
            canvas.data.originalImage = im.copy()
            canvas.data.undoQueue.append(im.copy())
            canvas.data.imageSize = im.size
            canvas.data.imageForTk = self.makeImageForTk(canvas)
            self.drawImage(canvas)
        else:
            tkinter.messagebox.showinfo(title="Image File", \
                                  message="Choose an Image File!", parent=canvas.data.mainWindow)
    
    
    
    def makeImageForTk(self, canvas):
        im = canvas.data.image
        if canvas.data.image != None:
            imageWidth = canvas.data.image.size[0]
            imageHeight = canvas.data.image.size[1]
            if imageWidth > imageHeight:
                resizedImage = im.resize((canvas.data.width, \
                                          int(round(float(imageHeight) * canvas.data.width / imageWidth))))
                canvas.data.imageScale = float(imageWidth) / canvas.data.width
            else:
                resizedImage = im.resize((int(round(float(imageWidth) * canvas.data.height / imageHeight)), \
                                          canvas.data.height))
                canvas.data.imageScale = float(imageHeight) / canvas.data.height
            canvas.data.resizedIm = resizedImage
            return ImageTk.PhotoImage(resizedImage)
    
    
    def drawImage(self, canvas):
        if canvas.data.image != None:
            canvas.create_image(canvas.data.width / 2.0 - canvas.data.resizedIm.size[0] / 2.0,
                                canvas.data.height / 2.0 - canvas.data.resizedIm.size[1] / 2.0,
                                anchor=NW, image=canvas.data.imageForTk)
            canvas.data.imageTopX = int(round(canvas.data.width / 2.0 - canvas.data.resizedIm.size[0] / 2.0))
            canvas.data.imageTopY = int(round(canvas.data.height / 2.0 - canvas.data.resizedIm.size[1] / 2.0))
    
        