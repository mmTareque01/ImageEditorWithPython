#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 02:58:02 2021

@author: tareque
"""

import tkinter.messagebox
import MyMenu



class Assets:
    
    menu = MyMenu.Menu()
    
    def getPixel(self, event, canvas):
        try:
            if canvas.data.colourPopToHappen == True and \
                    canvas.data.cropPopToHappen == False and canvas.data.image != None:
                data = []
                canvas.data.pixelx = \
                    int(round((event.x - canvas.data.imageTopX) * canvas.data.imageScale))
                canvas.data.pixely = \
                    int(round((event.y - canvas.data.imageTopY) * canvas.data.imageScale))
                pixelr, pixelg, pixelb = \
                    canvas.data.image.getpixel((canvas.data.pixelx, canvas.data.pixely))
                tolerance = 60
                for y in range(canvas.data.image.size[1]):
                    for x in range(canvas.data.image.size[0]):
                        r, g, b = canvas.data.image.getpixel((x, y))
                        avg = int(round((r + g + b) / 3.0))
                        if (abs(r - pixelr) > tolerance or
                                abs(g - pixelg) > tolerance or
                                abs(b - pixelb) > tolerance):
                            R, G, B = avg, avg, avg
                        else:
                            R, G, B = r, g, b
                        data.append((R, G, B))
                canvas.data.image.putdata(data)
                self.menu.save(canvas)
                canvas.data.undoQueue.append(canvas.data.image.copy())
                canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
                self.menu.drawImage(canvas)
        except:
            pass
        canvas.data.colourPopToHappen = False
                
        
    def colourPop(self, canvas):
        canvas.data.cropPopToHappen = False
        canvas.data.colourPopToHappen = True
        canvas.data.drawOn = False
        tkinter.messagebox.showinfo(title="Colour Pop", message="Click on a part of the image which you want in colour",
                              parent=canvas.data.mainWindow)
        if canvas.data.cropPopToHappen == False:
            canvas.data.mainWindow.bind("<ButtonPress-1>", lambda event: self.getPixel(event, canvas))









