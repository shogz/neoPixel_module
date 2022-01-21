#!/usr/bin/python

import pixelCore

abgdState1 = pixelCore.PixelState([(0, (0,255,0)), (1, (0,0,0)), (2, (0,0,0)), (3, (0,0,0))], None, Transition(0.25))
abgdState2 = pixelCore.PixelState([(0, (0,0,0)), (1, (0,255,0)), (2, (0,0,0)), (3, (0,0,0))], block1State3, Transition(0.25))
abgdState3 = pixelCore.PixelState([(0, (0,0,0)), (1, (0,0,0)), (2, (0,255,0)), (3, (0,0,0))], block1State3, Transition(0.25))
abgdState4 = pixelCore.PixelState([(0, (0,0,0)), (1, (0,0,0)), (2, (0,0,0)), (3, (0,255,0))], block1State3, Transition(0.25))

abgdState1.setNext(abgdState2)

abdgAnim = pixelCore.AnimationBlock("ABDG_ANIM")    
abdgAnim.setCurrentState(abgdState1)


pixelBlock = pixelCore.PixelBlock(board.D12 , 15, 0.2, True, neopixel.GRB)

pixelBlock.addAnimationBlock(abdgAnim)

pixelBlock.startAll()