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

geoBTN = pixelCore.PixelState([(4, (255,100,0))], None, None)

geoBTNAnim = pixelCore.AnimationBlock("GEO_BTN_ANIM")    
geoBTNAnim.setCurrentState(geoBTN)

metBTN = pixelCore.PixelState([(5, (255,100,0))], None, None)

metBTNAnim = pixelCore.AnimationBlock("MET_BTN_ANIM")    
metBTNAnim.setCurrentState(metBTN)

bioBTN = pixelCore.PixelState([(6, (255,100,0))], None, None)

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

powerAnimState = pixelCore.PixelState([(10, (255,0,0)), (11, (0,255,0)), (12, (0,255,0)), (13, (0,255,0))], None, None)

powerAnim = pixelCore.AnimationBlock("POWER_ANIM")    
powerAnim.setCurrentState(powerAnimState)

abgd2State1 = pixelCore.PixelState([(14, (255,0,0)), (15, (255,0,0)), (16, (0,255,0)), (17, (0,0,0)), (18, (0,0,0)), (19, (0,0,0))], None, pixelCore.Transition(0.25))
abgd2State2 = pixelCore.PixelState([(14, (255,0,0)), (15, (255,0,0)), (16, (0,0,0)), (17, (0,255,0)), (18, (0,0,0)), (19, (0,0,0))], None, pixelCore.Transition(0.25))
abgd2State3 = pixelCore.PixelState([(14, (255,0,0)), (15, (255,0,0)), (16, (0,0,0)), (17, (0,0,0)), (18, (0,255,0)), (19, (0,0,0))], None, pixelCore.Transition(0.25))
abgd2State4 = pixelCore.PixelState([(14, (255,0,0)), (15, (255,0,0)), (16, (0,0,0)), (17, (0,0,0)), (18, (0,0,0)), (19, (0,255,0))], None, pixelCore.Transition(0.25))

abdg2Anim = pixelCore.AnimationBlock("ABDG_2_ANIM")    
abdg2Anim.setCurrentState(abgd2State1)

abgd2State1.setNext(abgd2State2)
abgd2State2.setNext(abgd2State3)
abgd2State3.setNext(abgd2State4)
abgd2State4.setNext(abgd2State1)

scanHeadStaticState = pixelCore.PixelState([(20, (255,0,0)), (21, (255,0,0)), (22, (255,0,0)), (25, (255,255,0)), (26, (255,255,0)), (27, (255,255,0)), (36, (255,255,0)), (37, (0,255,0)), (38, (0,255,0)), (39, (0,255,0)), (40, (0,255,0))], None, None)

scanHeadStatic = pixelCore.AnimationBlock("SCAN_HEAD_STATIC")    
scanHeadStatic.setCurrentState(scanHeadStaticState)

scanHeadToggle1 = pixelCore.PixelState([(23, (0,255,0)), (24, (0,0,0))], None, pixelCore.Transition(0.25))
scanHeadToggle2 = pixelCore.PixelState([(23, (0,0,0)), (24, (0,255,0))], None, pixelCore.Transition(0.25))

scanHeadToggle1.setNext(scanHeadToggle2)
scanHeadToggle2.setNext(scanHeadToggle1)

scanHeadToggleAnim = pixelCore.AnimationBlock("SCAN_HEAD_TOGGLE")    
scanHeadToggleAnim.setCurrentState(powerAnimState)

centerScanBar1 = pixelCore.PixelState([(28, (0,0,0)), (29, (0,0,0)), (30, (0,0,0)), (31, (0,255,0)), (32, (0,255,0)), (33, (0,0,0)), (34, (0,0,0)), (35, (0,0,0))], None, pixelCore.Transition(0.25))
centerScanBar2 = pixelCore.PixelState([(28, (0,0,0)), (29, (0,0,0)), (30, (0,255,0)), (31, (0,0,0)), (32, (0,0,0)), (33, (0,255,0)), (34, (0,0,0)), (35, (0,0,0))], None, pixelCore.Transition(0.25))
centerScanBar3 = pixelCore.PixelState([(28, (0,0,0)), (29, (0,255,0)), (30, (0,0,0)), (31, (0,0,0)), (32, (0,0,0)), (33, (0,0,0)), (34, (0,255,0)), (35, (0,0,0))], None, pixelCore.Transition(0.25))
centerScanBar4 = pixelCore.PixelState([(28, (0,255,0)), (29, (0,0,0)), (30, (0,0,0)), (31, (0,0,0)), (32, (0,0,0)), (33, (0,0,0)), (34, (0,0,0)), (35, (0,255,0))], None, pixelCore.Transition(0.25))

centerScanBar1.setNext(centerScanBar2)
centerScanBar2.setNext(centerScanBar3)
centerScanBar3.setNext(centerScanBar4)
centerScanBar4.setNext(centerScanBar1)

centerScanBarAnim = pixelCore.AnimationBlock("CENTER_SCAN_BAR_ANIM")    
centerScanBarAnim.setCurrentState(centerScanBar1)


pixelBlock = pixelCore.PixelBlock(board.D12 , 52, 0.2, False, neopixel.GRB)

pixelBlock.addAnimationBlock(abdgAnim)
pixelBlock.addAnimationBlock(geoBTNAnim)
pixelBlock.addAnimationBlock(metBTNAnim)
pixelBlock.addAnimationBlock(bioBTNAnim)
pixelBlock.addAnimationBlock(stateAnim)
pixelBlock.addAnimationBlock(powerAnim)
pixelBlock.addAnimationBlock(abdg2Anim)
#pixelBlock.addAnimationBlock(scanHeadStatic)
pixelBlock.addAnimationBlock(scanHeadToggleAnim)
#pixelBlock.addAnimationBlock(centerScanBarAnim)

pixelBlock.startAll()