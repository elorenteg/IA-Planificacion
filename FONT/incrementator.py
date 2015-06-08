#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import os
import commands
import time
import csv



version = raw_input("Version del problema [b,1,2,3,4]: ")
initTarea = int(raw_input("Numero de tareas: "))
initProgs = int(raw_input("Numero de programadores: "))
incT = int(raw_input("Incremento de tareas: "))
incP = int(raw_input("Incremento de programadores: "))


# fichero con una tabla con NTAREAS, NPROGS, TIEMPO
fileData = open("Tablas/datos-"+version+"-"+str(initTarea)+"-"+str(initProgs)+"-"+str(incT)+"-"+str(incP)+".csv", 'w')
csvData = csv.writer(fileData, delimiter='\t')
        
        
posible = True
i = 1
while posible:
    print "#" + str(i) + " ----------------------------------------------------------------------------- "
    os.system("python generator.py " + version + " " + str(initTarea) + " " + str(initProgs))
    
    output = commands.getoutput("python executor.py Generator/problema.pddl")
    print output
    
    if "NO HAY SOLUCION" in output:
        posible = False
    else:
        ind = output.find("Tiempo: ")
        tejec = output[ind+len("Tiempo: "):].split(" ")[0]
        ind = output.find("Tiempo total: ")
        ttotal = output[ind+len("Tiempo total: "):].split(" ")[0]
        csvData.writerow([initTarea, initProgs, tejec, ttotal])
    
    initTarea += incT
    initProgs += incP
        
        
    
    i += 1