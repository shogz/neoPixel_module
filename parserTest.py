#!/usr/bin/python

file = "somefilename"
lines = []

with open(file, 'r') as anims:
    lines = anims.readlines()

for line in lines:
