#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 03:43:55 2021

@author: tareque
"""



from PIL import ImageOps
import MyMenu

class Mirror:
    menu = MyMenu.Menu()
    def mirror(self, canvas):
        canvas.data.colourPopToHappen = False
        canvas.data.cropPopToHappen = False
        canvas.data.drawOn = False
        if canvas.data.image != None:
            canvas.data.image = ImageOps.mirror(canvas.data.image)
            self.menu.save(canvas)
            canvas.data.undoQueue.append(canvas.data.image.copy())
            canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
            self.menu.drawImage(canvas)
