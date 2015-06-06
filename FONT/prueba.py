#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import pylab as pl
import csv

ifile = open('datos.csv', "r")
reader = csv.reader(ifile, delimiter='\t')
RATIO = []
TIEMP = []
for row in reader:
    
    ntareas = row[0]
    nprogs = row[1]
    tiempo = row[2]
    rat = int(ntareas)/int(nprogs)
    TIEMP.append(tiempo)
    RATIO.append(rat)
    print ntareas + " -- " + nprogs + " -- " + tiempo + " -- " + str(rat)

pl.figure(figsize=(8, 6), dpi=80) # Create a figure of size 8x6 inches, 80 dots per inch
pl.subplot(1, 1, 1) # Create a new subplot from a grid of 1x1

ratio = [4,5]
tiempo = [1,2]
pl.plot(RATIO,TIEMP, marker='o')

#pl.xlim(-4.0, 4.0) # Set x limits
#pl.xticks(np.linspace(-4, 4, 9, endpoint=True)) # Set x ticks
#pl.ylim(-1.0, 1.0) # Set y limits
#pl.yticks(np.linspace(-1, 1, 5, endpoint=True)) # Set y ticks


pl.xlabel('Ratio ntareas/nprogs')
pl.ylabel('Tiempo de ejecucion (s)')
pl.title('Tiempo segun el ratio ntareas/nprogs')

pl.savefig("graph1.png", dpi=72) # Save figure using 72 dots per inch
pl.show() # Show result on screen