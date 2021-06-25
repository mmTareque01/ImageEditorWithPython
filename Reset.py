#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 03:43:07 2021

@author: tareque
"""





import MyMenu


class Reset:
    menu = MyMenu.Menu()
    def reset(self, canvas):
        canvas.data.colourPopToHappen = False
        canvas.data.cropPopToHappen = False
        canvas.data.drawOn = False
        if canvas.data.image != None:
            canvas.data.image = canvas.data.originalImage.copy()
            self.menu.save(canvas)
            canvas.data.undoQueue.append(canvas.data.image.copy())
            canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
            self.menu.drawImage(canvas)