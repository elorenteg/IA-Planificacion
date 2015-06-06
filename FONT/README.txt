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

* Linux: ./Metric-FF/ff -o ver/dominio.pddl -f ver/problema.pddl
         ./Metric-FF/ff -O -o ver/dominio.pddl -f ver/problema.pddl (si se quiere optimizar)
         
         ver puede ser cualquiera de las versiones