#!/usr/bin/python

import neopixel
import pixelCore
import board

abgdState1 = pixelCore.PixelState([(0, (0,255,0)), (1, (0,0,0)), (2, (0,0,0)), (3, (0,0,0))], None, pixelCore.Transition(0.25))
abgdState2 = pixelCore.PixelState([(0, (0,0,0)), (1, (0,255,0)), (2, (0,0,0)), (3, (0,0,0))], None, pixelCore.Transition(0.25))
abgdState3 = pixelCore.PixelState([(0, (0,0,0)), (1, (0,0,0)), (2, (0,255,0)), (3, (0,0,0))], None, pixelCore.Transition(0.25))
abgdState4 = pixelCore.PixelState([(0, (0,0,0)), (1, (0,0,0)), (2, (0,0,0)), (3, (0,255,0))], None, pixelCore.Transition(0.25))

abgdState1.setNext(abgdState2)
abgdState2.setNext(abgdState3)
abgdState3.setNext(abgdState4)
abgdState4.setNext(abgdState1)

abdgAnim = pixelCore.AnimationBlock("ABDG_ANIM")    
abdgAnim.setCurrentState(abgdState1)

geoBTN = pixelCore.PixelState([(4, (0,255,0))], None, None)


pixelBlock = pixelCore.PixelBlock(board.D12 , 15, 0.2, True, neopixel.GRB)

pixelBlock.addAnimationBlock(abdgAnim)

pixelBlock.startAll()