(define (problem problema)
   (:domain tareas-ext1)
   (:objects t1 t2 t3 - tarea
             p1 p2 - programador)

    (:init
        (= (dtarea t1) 3) (= (ttarea t1) 1)
        (= (dtarea t2) 3) (= (ttarea t2) 1)
        (= (dtarea t3) 3) (= (ttarea t3) 1)
        
        (= (hprog p1) 2) (= (cprog p1) 1)
        (= (hprog p2) 2) (= (cprog p2) 1)
    )

    (:goal
        (forall (?t - tarea) (revisada ?t))
    )
)

