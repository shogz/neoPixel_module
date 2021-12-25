#!/usr/bin/python

import neopixel
from enum import Enum
import time


class PixelBlock():
    
    animationBlocks = []

    def __init__(self, hardwarePin, noPixel, brightness=0.2, auto_write=True, pixel_order=neopixel.RGB):

        self.pixels = neopixel.NeoPixel(hardwarePin, noPixels, brightness, auto_write, pixel_order)
        
    def addAnimationBlock(animationBlock: AnimationBlock):
        self.animationBlocks.append(animationBlock)

    def runAnimations():

        while(not stopped):
            
            for anim in self.animationBlocks:

                anim.setPixelStates()

            if(not auto_write):
                self.pixels.show()

        

class AnimationBlock():

    def __init__(self, id = "", accessToken:NeoPixel = None, autostart: bool = True, status:AnimationStatus = AnimationStatus.RUNNING, startState: PixelState = None):
        
        self.id = id
        self.accessToken = accessToken
        self.autostart = autostart
        self.currentState = startState

        self.status = status

        self.lastUpdate = time.perf_counter_ns()

        setPixelStates()

    def next():

        if(checkSwitchCondition()):
            currentState = currentState.next

    def checkSwitchCondition():

        if(self.currentState.transition.transitionType == TransitionType.DELAY):
            
            if(time.perf_counter_ns() - lastUpdate >= currentState.transition.duration):
                return True
           
        return False
    
    def setPixelStates():

        if(status != AnimationStatus().STOPPED):

            for pix in currentState.pixelList:

                self.accessToken[pix(1)] = pix(2)

class PixelState():
    
    def __init__(self, pixelList, next, transition):

        # PixelList is a Tupel with the first element beeing the index of the Neopixel that configured, and the second element beeing an RGB or RGBW tupel
        self.pixelList = pixelList
        self.next = next
        self.transition = transition

class Transition():

    def __init__(self, duration, transitionType=TransitionType.DELAY):

        self.duration = duration
        self.transitionType = transitionType

class AnimationStatus(Enum):
    RUNNING=0
    STOPPED=1
    CLEARED=2

class TransitionType(Enum()): 
    DELAY=0