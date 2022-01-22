#!/usr/bin/python

import neopixel
import board
from enum import Enum
import time

#import RPi.GPIO as GPIO

class AnimationStatus(Enum):
    RUNNING=0
    STOPPED=1
    CLEARED=2

class TransitionType(Enum): 
    DELAY=0

class Transition():

    def __init__(self, duration, transitionType=TransitionType.DELAY):

        self.duration = duration
        self.transitionType = transitionType


class PixelState():
    
    def __init__(self, pixelList, next, transition):

        # PixelList is a Tupel with the first element beeing the index of the Neopixel that configured, and the second element beeing an RGB or RGBW tupel
        self.pixelList = pixelList
        self.next = next
        self.transition = transition

    def setNext(self, next):
        self.next = next


class AnimationBlock():

    def __init__(self, id, accessToken = None, autostart = True, status = AnimationStatus.RUNNING, startState = None):
        
        self.id = id
        self.accessToken = accessToken
        self.autostart = autostart
        self.currentState = startState

        self.status = status

        self.lastUpdate = time.perf_counter()

        self.setPixelStates()

    def setAccessToken(self, accessToken):
        self.accessToken = accessToken

    def setCurrentState(self, newState):
        self.currentState = newState
        self.setPixelStates()

    def checkSwitchCondition(self):

        if(self.currentState.transition is None):
            return False

        if(self.currentState.transition.transitionType == TransitionType.DELAY):
            
            now = time.perf_counter()
            if(now - self.lastUpdate >= self.currentState.transition.duration):
                return True
           
        return False
    
    def setPixelStates(self):

        if(self.accessToken is None):
            print("No Access Token is configured to write to a chain of Neopixels!");
            if(self.currentState is not None):
                print(self.currentState.pixelList)
            return;

        if(self.status != AnimationStatus.STOPPED):
            
            for pix in self.currentState.pixelList:
                index, values = pix
                #print("Index: {}, Value:{}".format(index, values))
                self.accessToken[index] = values

    def next(self):

        if(self.checkSwitchCondition()):
            print("Animation: " + self.id)
            self.currentState = self.currentState.next
            self.setPixelStates()
            self.lastUpdate = time.perf_counter()


class PixelBlock():
    
    animationBlocks = []
    stopped = True

    def __init__(self, hardwarePin, noPixels, bright=0.2, auto=True, order=neopixel.RGB):

        self.pixels = neopixel.NeoPixel(hardwarePin, noPixels, brightness=bright, auto_write=auto, pixel_order=order)
        self.auto_write = auto
        
    def addAnimationBlock(self, animationBlock):
        animationBlock.accessToken = self.pixels
        self.animationBlocks.append(animationBlock)

    def runAnimations(self):


        for anim in self.animationBlocks:

            anim.setPixelStates()

        if(not self.auto_write):
            self.pixels.show()


        while(not self.stopped):
            
            for anim in self.animationBlocks:

                anim.next()

            if(not self.auto_write):
                self.pixels.show()

    def stopAll(self):
        self.stopped = True

    def startAll(self):
        self.stopped = False
        self.runAnimations()


def main():

    print("Starting config")
    
    block1State3 = PixelState([(0, (0,50,0)), (1, (0,0,0)), (2, (0,0,0)), (3, (0,0,0)), (4, (0,0,0)), (5, (0,50,0))], None, Transition(0.25))
    block1State2 = PixelState([(0, (0,0,0)), (1, (0,50,0)), (2, (0,0,0)), (3, (0,0,0)), (4, (0,50,0)), (5, (0,0,0))], block1State3, Transition(0.25))
    block1State1 = PixelState([(0, (0,0,0)), (1, (0,0,0)), (2, (0,50,0)), (3, (0,50,0)), (4, (0,0,0)), (5, (0,0,0))], block1State2, Transition(0.25))

    block1State3.setNext(block1State1)

    animBlock1 = AnimationBlock("ANIM 1")    
    animBlock1.setCurrentState(block1State1)

    #block2State2 = PixelState([(6, (0,0,0)), (7, (0,0,255))], None, Transition(0.5))
    #block2State1 = PixelState([(6, (0,0,255)), (7, (0,0,0))], block2State2, Transition(0.5))

    #block2State2.setNext(block2State1)
    
    #animBlock2 = AnimationBlock("ANIM 2")    
    #animBlock2.setCurrentState(block2State1)

    #block3State2 = PixelState([(10, (255,0,0))], None, Transition(0.25))
    #block3State1 = PixelState([(10, (0,0,0))], block3State2, Transition(0.75))

    #block3State2.setNext(block3State1)
    
    #animBlock3 = AnimationBlock("ANIM 3")    
    #animBlock3.setCurrentState(block3State1)

    #block4State2 = PixelState([(12, (0,0,255))], None, Transition(0.75))
    #block4State1 = PixelState([(12, (0,0,0))], block4State2, Transition(0.1))

    #block4State2.setNext(block4State1)
    
    #animBlock4 = AnimationBlock("ANIM 4")    
    #animBlock4.setCurrentState(block4State1)


    pixelBlock = PixelBlock(board.D12 , 15, 0.2, True, neopixel.RGB)

    pixelBlock.addAnimationBlock(animBlock1)
    #pixelBlock.addAnimationBlock(animBlock2)
    #pixelBlock.addAnimationBlock(animBlock3)    
    #pixelBlock.addAnimationBlock(animBlock4)

    print("Config done")

    pixelBlock.startAll()


#main()