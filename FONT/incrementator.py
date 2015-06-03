#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import os
import commands


version = raw_input("Version del problema [b,1,2,3,4]: ")
initTarea = int(raw_input("Numero de tareas: "))
initProgs = int(raw_input("Numero de programadores: "))

posible = True
i = 1
while posible:
    print "#" + str(i) + " ----------------------------------------------------------------------------- "
    print "Num Tareas: " + str(initTarea)
    print "Num Progra: " + str(initProgs)
    os.system("python generator.py " + version + " " + str(initTarea) + " " + str(initProgs))
    
    output = commands.getoutput("./Metric-FF/ff -o Basic/dominio.pddl -f problema.pddl")
    print output
    
    initTarea += 1
    initProgs += 2
    if "unsolvable" in output:
        posible = False
        
    
    i += 1