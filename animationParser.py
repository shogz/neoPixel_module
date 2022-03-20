#!/usr/bin/python

import pixelCore
import neopixel

class Parser():

    file = "animations/animationtest.txt"


    def createPixelString(self, name: str, pin: str, noPixels: int, brightness: float, autoWrite: bool, colorConfig: str) -> pixelCore.PixelBlock:
        
        pixelOrder = neopixel.GRB

        if(colorConfig == 'RGB'):
            pixelOrder = neopixel.RGB
        elif (colorConfig == 'RGBW'):
            pixelOrder = neopixel.RGBW
        elif (colorConfig == 'GRBW'):
            pixelOrder = neopixel.GRBW


        pixelBlock = pixelCore.PixelBlock(hardwarePin, noPixels, bright=brightness, auto=autoWrite, order=pixelOrder)

        return pixelBlock

    def createAnimation(name:str, auto: bool, repeat:bool) -> pixelCore.AnimationBlock:
        
        return pixelCore.AnimationBlock(id, None, autostart=auto, status=pixelCore.AnimationStatus().RUNNING, startState=None)

    def parse(self, file: str):

        pixelBlocks = []
        
        lastPixelBlock: pixelCore.PixelBlock = None
        lastAnimationBlock: pixelCore.AnimationBlock(id) = None
        lastAnimationStep: pixelCore.PixelState = None

        with open(file, encoding='utf-8') as f:
            for line in f:
                
                linesplit = line.rsplit(" ")

                if(len(linesplit) > 1):

                    if(linesplit[0].strip() == "string"):
                        
                        if(len(linesplit) != 7):
                            raise SyntaxError("Mandatory Pixelstring configuration missing. Please check the String definition.")
                        else:
                            lastPixelBlock = createPixelString(linesplit[1], linesplit[2], linesplit[3], linesplit[4], linesplit[5], linesplit[6])
                            pixelBlocks.append(lastPixelBlock)
                        

                    elif(linesplit[0].strip() == "anim"):
                        
                        if(lastPixelBlock == None):
                            raise SyntaxError("Animation defined before Pixel Block")

                        lastAnimationBlock = createAnimation(linesplit[1], linesplit[2], linesplit[3])

                    else:

                        if(lastAnimationBlock == None):
                            raise SyntaxError("No animation defined to add Pixel states")

                        pixelList = linesplit[0].rsplit(",")

                        state = pixelCore.PixelState(pixelList, None, linesplit[1])
                        lastAnimationStep.setNext(state)
                        lastAnimationStep = state
                        
                        if(lastAnimationBlock.currentState == None):
                            # Set first step of the animation
                            lastAnimationBlock.setCurrentState(lastAnimationStep)

        return pixelBlocks
                        
                        
