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
    print ""
    print action.capitalize()
    for key, value in diccTP.iteritems():
        print "  " + key + " " + action + " " + str(value) + " tareas"
        
def recorta(prob,sfind):
    ind = prob.find(sfind)
    dfind = prob[ind:]
    ind = dfind.find(")")
    dfind = dfind[ind+2:]
    ind = dfind.find(")")
    dfind = dfind[:ind]
    return dfind
        
def showTiempo(REA, REV):
    prob = open("problema.pddl", "r")
    prob = prob.read()
    
    #print prob
    ttotal = 0
    for elem in REA:
        ind = elem.find(" ")
        tarea = elem[:ind]
        prog = elem[ind+1:]
        
        dtarea = int(recorta(prob, "dtarea " + tarea + ") "))
        ttarea = int(recorta(prob, "ttarea " + tarea + ") "))
        hprog = int(recorta(prob, "hprog " + prog + ") "))
        cprog = int(recorta(prob, "cprog " + prog + ") "))
        
        if dtarea <= hprog:
            ttotal += ttarea
        else:
            ttotal += ttarea + 2
            
        if cprog == 1:
            ttotal += 1
        else:
            ttotal += 2
            
    return ttotal
    
    
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
    if len(REV) > 0:
        showSolution(diccREV, "revisa")
    
    ttotal = showTiempo(REA, REV)
    return ttotal
    
        
        
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
        print "NO HAY SOLUCION"
    else:
        ttotal = resultado(output, initTarea, initProgs)
        csvData.writerow([initTarea, initProgs, tiempo, ttotal])
        print ""
        print "Tiempo total: " + str(ttotal) + " h"
        
    print "\n"
    
    initTarea += incT
    initProgs += incP
        
        
    
    i += 1