#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
import sys

ntareas = sys.argv[1]
nprogs = sys.argv[2]
file = open("problema.pddl", "w")
print randint(2,9)

def create_objects(letra, tipo, max):
    for i in range(1,int(max)+1):
        file.write(letra + str(i) + " ")
    file.write("- " + tipo + "\n")
    
def init_tarea(max):
    for i in range(1,int(max)+1):
        ti = "t" + str(i)
        file.write("(= (dtarea " + ti + ") " + str(randint(1,3)) + ")")
        file.write("(= (ttarea " + ti + ") " + str(randint(1,10)) + ")")
        file.write("\n")

def init_programador(max):
    for i in range(1,int(max)+1):
        pi = "p" + str(i)
        file.write("(= (hprog " + pi + ") " + str(randint(1,3)) + ")")
        file.write("(= (cprog " + pi + ") " + str(randint(1,2)) + ")")
        file.write("(= (tprog " + pi + ") " + str(0) + ")")
        file.write("\n")


def create_problem():
    print("Creating new problem file")
    
    file.write("(define (problem problema)\n")
    file.write("(:domain dominio)\n")
    
    
    file.write("(:objects \n")
    create_objects("t","tarea",ntareas)
    create_objects("p","programador",nprogs)
    file.write(")\n")
    
    file.write("(:init\n")
    init_tarea(ntareas)
    init_programador(nprogs)
    file.write(")\n")

    file.write("(:goal\n")
    file.write("(forall (?t - tarea) (servida ?t))\n")
    file.write(")\n")
    
    file.close()
    
    

create_problem()