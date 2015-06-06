(define (problem problema)
   (:domain tareas-ext4)
   (:objects t1 t2 t3 - tarea
             p1 p2 p3 - programador)

    (:init
        (= (dtarea t1) 1) (= (ttarea t1) 1)
        (= (dtarea t2) 1) (= (ttarea t2) 1)
        (= (dtarea t3) 1) (= (ttarea t3) 1)
        
        (= (hprog p1) 1) (= (cprog p1) 1) (= (nprog p1) 0)
        (= (hprog p2) 1) (= (cprog p2) 1) (= (nprog p2) 0)
        (= (hprog p3) 1) (= (cprog p3) 1) (= (nprog p3) 0)

        (= (ntrabajadores) 0)
        (= (ttotal) 0)
    )

    (:goal
        (forall (?t - tarea) (revisada ?t))
    )

    (:metric minimize (+ (* 0.5 (ttotal)) (* 0.5 (ntrabajadores))))
)


