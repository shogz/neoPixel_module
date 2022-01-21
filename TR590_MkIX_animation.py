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

geoBTN = pixelCore.PixelState([(4, (255,150,0))], None, None)

geoBTNAnim = pixelCore.AnimationBlock("GEO_BTN_ANIM")    
geoBTNAnim.setCurrentState(geoBTN)

metBTN = pixelCore.PixelState([(5, (255,150,0))], None, None)

metBTNAnim = pixelCore.AnimationBlock("MET_BTN_ANIM")    
metBTNAnim.setCurrentState(metBTN)

bioBTN = pixelCore.PixelState([(6, (255,150,0))], None, None)

bioBTNAnim = pixelCore.AnimationBlock("BIO_BTN_ANIM")    
bioBTNAnim.setCurrentState(bioBTN)

stateAnim1 = pixelCore.PixelState([(7, (0,0,0)), (8, (0,255,0)), (9, (0,0,0))], None, pixelCore.Transition(0.25))
stateAnim2 = pixelCore.PixelState([(7, (255,0,0)), (8, (0,0,0)), (9, (0,0,0))], None, pixelCore.Transition(0.10))
stateAnim3 = pixelCore.PixelState([(7, (0,0,0)), (8, (0,0,0)), (9, (0,255,0))], None, pixelCore.Transition(0.10))

stateAnim1.setNext(stateAnim2)
stateAnim2.setNext(stateAnim3)
stateAnim3.setNext(stateAnim1)

stateAnim = pixelCore.AnimationBlock("STATE_ANIM")    
stateAnim.setCurrentState(stateAnim1)

pixelBlock = pixelCore.PixelBlock(board.D12 , 15, 0.2, True, neopixel.GRB)

pixelBlock.addAnimationBlock(abdgAnim)
pixelBlock.addAnimationBlock(geoBTNAnim)
pixelBlock.addAnimationBlock(metBTNAnim)
pixelBlock.addAnimationBlock(bioBTNAnim)
pixelBlock.addAnimationBlock(stateAnim)

pixelBlock.startAll()