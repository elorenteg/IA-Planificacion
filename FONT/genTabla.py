#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import pylab as pl
import matplotlib.cm as cm
import numpy as np
import csv
import glob

version = raw_input("Version del problema [b,1,2,3,4]: ")
initTarea = raw_input("Numero de tareas: ")
initProgs = raw_input("Numero de programadores: ")
filesData = sorted(glob.glob("Tablas/datos-"+version+"-"+initTarea+"-"+initProgs+"*"))

pl.figure(figsize=(15, 10), dpi=80) # Create a figure of size 8x6 inches, 80 dots per inch
colors = iter(cm.rainbow(np.linspace(0,1,len(filesData)*6)))

for f in filesData:
    nameFile = f
    
    f = f.split('.')[0]
    f = f.split('-')
    v = f[1]
    iniT = f[2]
    iniP = f[3]
    incT = f[4]
    incP = f[5]
    print v + " -- " + iniT + " -- " + iniP + " -- " + incT + " -- " + incP

    ifile = open(nameFile, "r")
    reader = csv.reader(ifile, delimiter='\t')
    RATIO = []
    TIEMP = []
    TTOTA = []
    NTARE = []
    NPROG = []
    for row in reader:
        ntareas = row[0]
        nprogs = row[1]
        tiempo = row[2]
        ttotal = row[3]
        rat = int(ntareas)/int(nprogs)
        TIEMP.append(tiempo)
        RATIO.append(rat)
        TTOTA.append(ttotal)
        NTARE.append(ntareas)
        NPROG.append(nprogs)
        #print ntareas + " -- " + nprogs + " -- " + tiempo + " -- " + str(rat)

    

    pl.subplot(3, 2, 1)
    pl.plot(range(1,len(TIEMP)+1),TIEMP, marker='o', label='inc nt('+str(incT)+') np('+str(incP)+')', color=next(colors))
    pl.grid(True)
    pl.xlabel('Num. de ejecucion')
    pl.ylabel('Tiempo de ejecucion (s)')
    pl.title('Tiempo de ejecucion segun incrementamos el tamano')
    pl.legend(loc='best', fancybox=True)
    pl.subplot(3, 2, 2)
    pl.plot(range(1,len(TTOTA)+1),TTOTA, marker='o', label='inc nt('+str(incT)+') np('+str(incP)+')', color=next(colors))
    pl.grid(True)
    pl.xlabel('Num. de ejecucion')
    pl.ylabel('Tiempo de realizacion (h)')
    pl.title('Tiempo de realizacion segun incrementamos el tamano')
    pl.legend(loc='best', fancybox=True)
    pl.subplot(3, 2, 3)
    pl.plot(NTARE,TIEMP, marker='o', label='inc nt('+str(incT)+') np('+str(incP)+')', color=next(colors))
    pl.grid(True)
    pl.xlabel('Num. de tareas')
    pl.ylabel('Tiempo de ejecucion (s)')
    pl.title('Tiempo de realizacion segun el numero de tareas')
    pl.legend(loc='best', fancybox=True)
    pl.subplot(3, 2, 4)
    pl.plot(NTARE,TTOTA, marker='o', label='inc nt('+str(incT)+') np('+str(incP)+')', color=next(colors))
    pl.grid(True)
    pl.xlabel('Num. de tareas')
    pl.ylabel('Tiempo de realizacion (h)')
    pl.title('Tiempo de realizacion segun el numero de tareas')
    pl.legend(loc='best', fancybox=True)
    pl.subplot(3, 2, 5)
    pl.plot(NPROG,TIEMP, marker='o', label='inc nt('+str(incT)+') np('+str(incP)+')', color=next(colors))
    pl.grid(True)
    pl.xlabel('Num. de programadores')
    pl.ylabel('Tiempo de ejecucion (s)')
    pl.title('Tiempo de ejecucion segun el numero de programadores')
    pl.legend(loc='best', fancybox=True)
    pl.subplot(3, 2, 6)
    pl.plot(NPROG,TTOTA, marker='o', label='inc nt('+str(incT)+') np('+str(incP)+')', color=next(colors))
    pl.grid(True)
    pl.xlabel('Num. de programadores')
    pl.ylabel('Tiempo de realizacion (h)')
    pl.title('Tiempo de realizacion segun el numero de programadores')
    pl.legend(loc='best', fancybox=True)
    
    pl.tight_layout()


pl.savefig("graph.png", dpi=72) # Save figure using 72 dots per inch
pl.show() # Show result on screen