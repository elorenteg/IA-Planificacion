Inteligencia Artificial - Planificación

* DOCS:
   * informe.pdf
   
* FONT:
    * Metric-FF
        * ff
    * Basic
        * dominio.pddl                    --> dominio del problema para cada versión
        * problema.pddl / problema2.pddl  --> juegos de prueba no triviales para cada versión
        * problema.txt  / problema2.txt   --> salidas de los juegos de prueba para cada versión
    * Extension1
        * dominio.pddl
        * problema.pddl / problema2.pddl
        * problema.txt  / problema2.txt
    * Extension2
        * dominio.pddl
        * problema.pddl / problema2.pddl
        * problema.txt  / problema2.txt
    * Extension3
        * dominio.pddl
        * problema.pddl / problema2.pddl
        * problema.txt  / problema2.txt
    * Extension4
        * dominio.pddl
        * problema.pddl / problema2.pddl
        * problema.txt  / problema2.txt
    * Tablas
        * datos-*.csv                     --> tablas de recogidas de datos cuyas columnas son [ntareas, nprogs, tejec, ttotal]
        * genTablas.py                    --> genera tablas con los datos de incrementator.py
        * graph-*.png                     --> graficas para ver el tejec y ttotal
    * Generator
        * problema.pddl                   --> problema generado por generator.py
    * generator.py                        --> generador de un solo problema
    * executor.py                         --> ejecuta un problema
    * incrementator.py                    --> generador de varios problemas de forma incremental
        
        

Para ejecutar el codigo hay que hacer

* Linux: ./Metric-FF/ff -o <version>/dominio.pddl -f <version>/problema.pddl
         ./Metric-FF/ff -O -o <version>/dominio.pddl -f <version>/problema.pddl (si se quiere optimizar)
         
         
Para ejecutar los generadores de problemas:

    python generator.py <version> <ntareas> <nprogs>
    
    python executor.py <problema> [--asig] --> El flag --asig muestra la asignación dada por el FF
    
    python incrementator.py
    
    python genTabla.py
