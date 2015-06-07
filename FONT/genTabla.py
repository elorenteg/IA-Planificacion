#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import pylab as pl
import csv

ifile = open('datos.csv', "r")
reader = csv.reader(ifile, delimiter='\t')
RATIO = []
TIEMP = []
TTOTA = []
incT = 0
incP = 0
calculado = False
for row in reader:
    ntareas = row[0]
    nprogs = row[1]
    tiempo = row[2]
    ttotal = row[3]
    rat = int(ntareas)/int(nprogs)
    TIEMP.append(tiempo)
    RATIO.append(rat)
    TTOTA.append(ttotal)
    print ntareas + " -- " + nprogs + " -- " + tiempo + " -- " + str(rat)
    
    if incT == 0:
        incT = int(ntareas)
        incP = int(nprogs)
    elif not calculado:
        incT = int(ntareas) - incT
        incP = int(nprogs) - incP
        calculado = True

pl.figure(figsize=(15, 6), dpi=80) # Create a figure of size 8x6 inches, 80 dots per inch
pl.subplot(1, 2, 1) # Create a new subplot from a grid of 1x1

pl.plot(range(1,len(TIEMP)+1),TIEMP, marker='o', label='inc nt('+str(incT)+') np('+str(incP)+')')
pl.grid(True)
pl.xlabel('Num. de ejecucion')
pl.ylabel('Tiempo de ejecucion (s)')
pl.title('Tiempo segun incrementamos el tamano')
pl.legend()
pl.subplot(1, 2, 2)
pl.plot(range(1,len(TTOTA)+1),TTOTA, marker='o', label='inc nt('+str(incT)+') np('+str(incP)+')')
pl.grid(True)
pl.xlabel('Num. de ejecucion')
pl.ylabel('Tiempo de realizacion (h)')
pl.title('Tiempo segun incrementamos el tamano')
pl.legend()


pl.savefig("graph.png", dpi=72) # Save figure using 72 dots per inch
pl.show() # Show result on screen