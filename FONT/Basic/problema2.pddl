(define (problem habilidadInsuficiente-3-1)
   (:domain tareas-basic)
   (:objects t1 t2 t3 - tarea
             p1 - programador)

    (:init
        (= (dtarea t1) 3) (= (ttarea t1) 5)
        (= (dtarea t2) 2) (= (ttarea t2) 5)
        (= (dtarea t3) 1) (= (ttarea t3) 5)
        
        (= (hprog p1) 1) (= (cprog p1) 1)
    )

    (:goal
        (forall (?t - tarea) (servida ?t))
    )
)


