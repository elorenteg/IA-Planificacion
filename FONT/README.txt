Inteligencia Artificial - Planificación

* DOCS:
   * informe.pdf
   
* FONT:
    * Metric-FF
        * ff
    * Basic
        * dominio.pddl                    --> dominio del problema para cada versión
        * problema.pddl / problema2.pddl  --> juegos de prueba no triviales para cada versión
    * Extension1
        * dominio.pddl
        * problema.pddl / problema2.pddl
    * Extension2
        * dominio.pddl
        * problema.pddl / problema2.pddl
    * Extension3
        * dominio.pddl
        * problema.pddl / problema2.pddl
    * Extension4
        * dominio.pddl
        * problema.pddl / problema2.pddl
        
        

Para ejecutar el codigo hay que hacer

* Linux: ./Metric-FF/ff -o <version>/dominio.pddl -f <version>/problema.pddl
         ./Metric-FF/ff -O -o <version>/dominio.pddl -f <version>/problema.pddl (si se quiere optimizar)
         
         
Para ejecutar los generadores de problemas:

* generator.py --> Generador de un solo problema
    python generator.py <version> <ntareas> <nprogs>
    
* incrementator.py --> Generador de varios problemas de forma incremental
    python incrementator.py
    
* genTabla.py --> Genera tablas con los datos de incrementator.py
    python genTabla.py