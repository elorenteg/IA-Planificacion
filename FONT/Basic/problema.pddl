(define (problem problema)
   (:domain tareas-basic)
   (:objects t1 t2 t3 - tarea
             p1 p2 p3 - programador)

    (:init
        (= (dtarea t1) 1) (= (ttarea t1) 1)
        (= (dtarea t2) 1) (= (ttarea t2) 1)
        (= (dtarea t3) 1) (= (ttarea t3) 1)
        
        (= (hprog p1) 1) (= (cprog p1) 1)
        (= (hprog p2) 1) (= (cprog p2) 1)
        (= (hprog p3) 1) (= (cprog p3) 1)
    )

    (:goal
        (forall (?t - tarea) (servida ?t))
    )
)


