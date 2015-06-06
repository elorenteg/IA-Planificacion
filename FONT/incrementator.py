#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import os
import commands
import time
import csv

# fichero con una tabla con NTAREAS, NPROGS, TIEMPO
fileData = open('datos.csv', 'w')
csvData = csv.writer(fileData, delimiter='\t')



version = raw_input("Version del problema [b,1,2,3,4]: ")
initTarea = int(raw_input("Numero de tareas: "))
initProgs = int(raw_input("Numero de programadores: "))

paquete = "Basic"
if version in ['1','2','3','4']:
    paquete = "Extension" + version
    
    
def cuenta(TP):
    dicc = {}
    for r in TP:
        ind = r.find(" ")
        tarea = r[:ind]
        prog = r[ind+1:]
        
        if prog in dicc:
            dicc[prog] = dicc[prog] + 1
        else:
            dicc[prog] = 1
            
    return dicc

def showSolution(diccTP, action):
    print action.capitalize()
    for key, value in diccTP.iteritems():
        print "  " + key + " " + action + " " + str(value) + " tareas"
    
    
def resultado(output, ntareas, nprogs):
    ini = output.find("step")
    fin = output.find("time spent")
    lista = output[ini:fin-8]
    lista = lista.split('\n')
    
    REA = []
    REV = []
    for elem in lista:
        ind = elem.find("REALIZA")
        if ind != -1:
            REA.append(elem[ind+8:].lower())
        else:
            ind = elem.find("REVISA")
            REV.append(elem[ind+7:].lower())
    #print REA
    #print REV
    
    diccREA = cuenta(REA) # numero de tareas que REALIZA cada programador. 0 si el programador no esta en el dicc
    diccREV = cuenta(REV) # numero de tareas que REVISA cada programador. 0 si el programador no esta en el dicc
    
    showSolution(diccREA, "realiza")
    showSolution(diccREV, "revisa")
        
        
        
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
    
    tiempo = str("%.3f" % (t2-t1))
    
    print "Tiempo: " + tiempo + " s"
    
    if "unsolvable" in output: # ya no tiene solucion
        posible = False
    else:
        resultado(output, initTarea, initProgs)
        csvData.writerow([initTarea, initProgs, tiempo])
    
    initTarea += 1
    initProgs += 2
        
        
    
    i += 1