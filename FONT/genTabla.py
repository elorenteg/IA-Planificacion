#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import pylab as pl
import csv
import glob

version = raw_input("Version del problema [b,1,2,3,4]: ")
initTarea = raw_input("Numero de tareas: ")
initProgs = raw_input("Numero de programadores: ")
filesData = sorted(glob.glob("datos-"+version+"-"+initTarea+"-"+initProgs+"*"))

pl.figure(figsize=(15, 6), dpi=80) # Create a figure of size 8x6 inches, 80 dots per inch

for f in filesData:
    nameFile = f
    ind = f.find('-')
    f = f[ind+1:]
    ind = f.find('-')
    v = f[:ind]
    f = f[ind+1:]
    ind = f.find('-')
    iniT = f[:ind]
    f = f[ind+1:]
    ind = f.find('-')
    iniP = f[:ind]
    f = f[ind+1:]
    ind = f.find('-')
    incT = f[:ind]
    f = f[ind+1:]
    ind = f.find('.')
    incP = f[:ind]
    
    print v + " -- " + iniT + " -- " + iniP + " -- " + incT + " -- " + incP

    ifile = open(nameFile, "r")
    reader = csv.reader(ifile, delimiter='\t')
    RATIO = []
    TIEMP = []
    TTOTA = []
    for row in reader:
        ntareas = row[0]
        nprogs = row[1]
        tiempo = row[2]
        ttotal = row[3]
        rat = int(ntareas)/int(nprogs)
        TIEMP.append(tiempo)
        RATIO.append(rat)
        TTOTA.append(ttotal)
        #print ntareas + " -- " + nprogs + " -- " + tiempo + " -- " + str(rat)

    
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