(define (problem optimoSegunCalidad-3-2)
   (:domain tareas-ext2)
   (:objects t1 t2 t3 - tarea
             p1 p2 - programador)

    (:init
        (= (dtarea t1) 1) (= (ttarea t1) 5)
        (= (dtarea t2) 1) (= (ttarea t2) 5)
        (= (dtarea t3) 1) (= (ttarea t3) 5)
        
        (= (hprog p1) 1) (= (cprog p1) 1)
        (= (hprog p2) 1) (= (cprog p2) 2)
        
        (= (ttotal) 0)
    )

    (:goal
        (forall (?t - tarea) (revisada ?t))
    )

    (:metric minimize (ttotal))
)


