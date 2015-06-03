#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import os
import commands
import time


version = raw_input("Version del problema [b,1,2,3,4]: ")
initTarea = int(raw_input("Numero de tareas: "))
initProgs = int(raw_input("Numero de programadores: "))

paquete = "Basic"
if version in ['1','2','3','4']:
    paquete = "Extension" + version

posible = True
i = 1
while posible:
    print "#" + str(i) + " ----------------------------------------------------------------------------- "
    print "Num Tareas: " + str(initTarea)
    print "Num Progra: " + str(initProgs)
    os.system("python generator.py " + version + " " + str(initTarea) + " " + str(initProgs))
    
    t1 = time.time()
    output = commands.getoutput("./Metric-FF/ff -o " + paquete+"/dominio.pddl -f problema.pddl")
    t2 = time.time()
    #print output
    print "Tiempo: " + str("%.3f" % (t2-t1)) + " s"
    
    initTarea += 1
    initProgs += 2
    if "unsolvable" in output:
        posible = False
        
    
    i += 1