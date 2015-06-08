(define (problem asignacionUnica-4-4)
   (:domain tareas-ext3)
   (:objects t1 t2 t3 t4 - tarea
             p1 p2 p3 p4 - programador)

    (:init
        (= (dtarea t1) 1) (= (ttarea t1) 2)
        (= (dtarea t2) 2) (= (ttarea t2) 3)
        (= (dtarea t3) 3) (= (ttarea t3) 5)
        (= (dtarea t4) 3) (= (ttarea t4) 6)
        
        (= (hprog p1) 3) (= (cprog p1) 1) (= (nprog p1) 0)
        (= (hprog p2) 1) (= (cprog p2) 2) (= (nprog p2) 0)
        (= (hprog p3) 2) (= (cprog p3) 2) (= (nprog p3) 0)
        (= (hprog p4) 1) (= (cprog p4) 1) (= (nprog p4) 0)

        (= (ttotal) 0)
    )

    (:goal
        (forall (?t - tarea) (revisada ?t))
    )

    (:metric minimize (ttotal))
)


