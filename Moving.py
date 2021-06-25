#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 03:40:50 2021

@author: tareque
"""


import MyMenu

class Moving:
    
    menu = MyMenu.Menu()
    
    def undo(self, canvas):
        if len(canvas.data.undoQueue) > 0:
            lastImage = canvas.data.undoQueue.pop()
            canvas.data.redoQueue.appendleft(lastImage)
        if len(canvas.data.undoQueue) > 0:
            canvas.data.image = canvas.data.undoQueue[-1]
        self.menu.save(canvas)
        canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
        self.menu.drawImage(canvas)
    
    
    def redo(self, canvas):
        if len(canvas.data.redoQueue) > 0:
            canvas.data.image = canvas.data.redoQueue[0]
        self.menu.save(canvas)
        if len(canvas.data.redoQueue) > 0:
            lastImage = canvas.data.redoQueue.popleft()
            canvas.data.undoQueue.append(lastImage)
        canvas.data.imageForTk = self.menu.makeImageForTk(canvas)
        self.menu.drawImage(canvas)
