#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import os
import commands
import time
import csv
import sys
import os.path

if (len(sys.argv)-1 != 1) and (len(sys.argv)-1 != 2):
    print 'python executor.py <file> [--asig]'
    sys.exit()
    
ifile = sys.argv[1]

# fichero con una tabla con NTAREAS, NPROGS, TIEMPO
fileProblem = open(ifile, 'r')
fileProblem = fileProblem.read()

ind = fileProblem.find(":domain")
version = fileProblem[ind+len(":domain tareas-"):].split(")")[0]

if "ext" in version:
    version = version[3:]
    paquete = "Extension" + version
else:
    version = "b"
    paquete = "Basic"
    
ind = fileProblem.find(":objects")
objects = fileProblem[ind+len(":objects"):].split(")")[0].lstrip().split("\n")
tareas = objects[0].split(" -")[0].lstrip().split(" ")
progas = objects[1].split(" -")[0].lstrip().split(" ")
ntareas = len(tareas)
nprogs = len(progas)


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
        
def recorta(sfind):
    ind = fileProblem.find(sfind)
    dfind = fileProblem[ind:]
    ind = dfind.find(")")
    dfind = dfind[ind+2:]
    ind = dfind.find(")")
    dfind = dfind[:ind]
    return dfind
        
def showTiempo(REA, REV):
    ttotal = 0
    for elem in REA:
        ind = elem.find(" ")
        tarea = elem[:ind]
        prog = elem[ind+1:]
        
        dtarea = int(recorta("dtarea " + tarea + ") "))
        ttarea = int(recorta("ttarea " + tarea + ") "))
        hprog = int(recorta("hprog " + prog + ") "))
        cprog = int(recorta("cprog " + prog + ") "))
        
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

    print ""
    ntrabajadores = 0
    diccUnion = diccREA
    diccUnion.update(diccREV)
    for prog in diccUnion.keys(): ntrabajadores += 1
    print "Núm. trabajadores:", ntrabajadores
    
    ttotal = showTiempo(REA, REV)
    return ttotal

def showAsig(output):
    ini = output.find("step")
    fin = output.find("time spent")
    lista = output[ini:fin-8]
    lista = lista.split('\n')
    
    L = []
    for elem in lista:
        ind = elem.find("REALIZA")
        if ind != -1:
            L.append(elem[ind:].lower())
        else:
            ind = elem.find("REVISA")
            L.append(elem[ind:].lower())
    
    print ""
    print "Asignaciones"
    for acc in L:
        print "  " + acc


print "Num Tareas: " + str(ntareas)
print "Num Progra: " + str(nprogs)

if version in ['2','3','4']:
    Oflag = " -O"
else:
    Oflag = ""
    
if (version in ['3','4']) and (ntareas > nprogs):
    print ""
    print "NO HAY SOLUCION -- ntareas > nprogs"
    sys.exit()
        

t1 = time.time()
output = commands.getoutput("./Metric-FF/ff" + Oflag + " -o " + paquete+"/dominio.pddl -f " + ifile)
t2 = time.time()

tiempo = str("%.3f" % (t2-t1))

print "Tiempo: " + tiempo + " s"

if ("unsolvable" in output) or ("unknown optimization method" in output): # ya no tiene solucion
    posible = False
    print ""
    print "NO HAY SOLUCION"
else:
    ttotal = resultado(output, ntareas, nprogs)
    print ""
    print "Tiempo total: " + str(ttotal) + " h"
    
    if len(sys.argv)-1 == 2 and sys.argv[2] == '--asig':
        showAsig(output)
    
print "\n"

