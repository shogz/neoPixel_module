#!/usr/bin/python

import neopixel
from enum import Enum
import time

import RPi.GPIO as GPIO

class PixelBlock():
    
    animationBlocks = []
    stopped = True

    def __init__(self, hardwarePin, noPixel, brightness=0.2, auto_write=True, pixel_order=neopixel.RGB):

        self.pixels = neopixel.NeoPixel(hardwarePin, noPixels, brightness, auto_write, pixel_order)
        
    def addAnimationBlock(animationBlock: AnimationBlock):
        self.animationBlocks.append(animationBlock)

    def runAnimations():

        while(not self.stopped):
            
            for anim in self.animationBlocks:

                anim.setPixelStates()
                anim.next()

            if(not auto_write):
                self.pixels.show()

    def stopAll():
        self.stopped = True

    def startAll():
        self.stopped = False
        runAnimations()

class AnimationBlock():

    def __init__(self, id, accessToken:NeoPixel = None, autostart: bool = True, status:AnimationStatus = AnimationStatus.RUNNING, startState: PixelState = None):
        
        self.id = id
        self.accessToken = accessToken
        self.autostart = autostart
        self.currentState = startState

        self.status = status

        self.lastUpdate = time.perf_counter_ns()

        setPixelStates()

    def setAccessToken(accessToken:NeoPixel):
        self.accessToken = accessToken

    def setCurrentState(newState: PixelState):
        self.currentState = newState
        setPixelStates

    def next():

        if(checkSwitchCondition()):
            currentState = currentState.next
            self.lastUpdate = time.perf_counter_ns()

    def checkSwitchCondition():

        if(self.currentState.transition.transitionType == TransitionType.DELAY):
            
            if((time.perf_counter_ns()) - lastUpdate >= self.currentState.transition.duration):
                return True
           
        return False
    
    def setPixelStates():

        if(self.accessToken is None):
            print("No Access Token is configured to write to a chain of Neopixels!");
            return;

        if(status != AnimationStatus().STOPPED):

            for pix in currentState.pixelList:

                self.accessToken[pix(1)] = pix(2)

class PixelState():
    
    def __init__(self, pixelList, next: PixelState, transition):

        # PixelList is a Tupel with the first element beeing the index of the Neopixel that configured, and the second element beeing an RGB or RGBW tupel
        self.pixelList = pixelList
        self.next = next
        self.transition = transition

    def setNext(next: PixelState):
        self.next = next

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


def main():
    
    block1State3 = PixelState([(0, (0,255,0)), (1, (0,0,0)), (2, (0,0,0)), (3, (0,0,0)), (4, (0,0,0)), (5, (0,255,0))], None, Transition(250))
    block1State2 = PixelState([(0, (0,0,0)), (1, (0,255,0)), (2, (0,0,0)), (3, (0,0,0)), (4, (0,255,0)), (5, (0,0,0))], block1State3, Transition(250))
    block1State1 = PixelState([(0, (0,0,0)), (1, (0,0,0)), (2, (0,255,0)), (3, (0,255,0)), (4, (0,0,0)), (5, (0,0,0))], block1State2, Transition(250))

    block1State3.setNext(block1State1)

    animBlock1 = AnimationBlock("ANIM 1")    
    animBlock1.setCurrentState(block1State1)

    block2State2 = PixelState([(6, (0,0,0)), (7, (0,0,255))], None, Transition(500))
    block2State1 = PixelState([(6, (0,0,255)), (7, (0,0,0))], block2State1, Transition(500))

    block2State2.setNext(block2State1)
    
    animBlock2 = AnimationBlock("ANIM 2")    
    animBlock2.setCurrentState(block2State1)

    block3State2 = PixelState([(8, (255,0,0))], None, Transition(250))
    block3State1 = PixelState([(8, (0,0,0))], block3State1, Transition(750))

    block3State2.setNext(block3State1)
    
    animBlock3 = AnimationBlock("ANIM 3")    
    animBlock3.setCurrentState(block3State1)

    block4State2 = PixelState([(8, (0,0,255))], None, Transition(750))
    block4State1 = PixelState([(8, (0,0,0))], block4State1, Transition(100))

    block4State2.setNext(block4State1)
    
    animBlock4 = AnimationBlock("ANIM 4")    
    animBlock4.setCurrentState(block4State1)


    pixelBlock = PixelBlock(10, 10);

    pixelBlock.addAnimationBlock(animBlock1)
    pixelBlock.addAnimationBlock(animBlock2)
    pixelBlock.addAnimationBlock(animBlock3)    
    pixelBlock.addAnimationBlock(animBlock4)

    pixelBlock.startAll()

