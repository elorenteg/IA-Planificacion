(define (problem problema)
   (:domain tareas-ext4)
   (:objects t1 t2 t3 - tarea
             p1 p2 p3 p4 p5 - programador)

    (:init
        (= (dtarea t1) 3) (= (ttarea t1) 2)
        (= (dtarea t2) 1) (= (ttarea t2) 7)
        (= (dtarea t3) 2) (= (ttarea t3) 9)
        
        (= (hprog p1) 2) (= (cprog p1) 2) (= (nprog p1) 0)
        (= (hprog p2) 3) (= (cprog p2) 1) (= (nprog p2) 0)
        (= (hprog p3) 2) (= (cprog p3) 2) (= (nprog p3) 0)
        (= (hprog p4) 3) (= (cprog p4) 1) (= (nprog p4) 0)
        (= (hprog p5) 3) (= (cprog p5) 2) (= (nprog p5) 0)

        (= (ntrabajadores) 0)
        (= (ttotal) 0)
    )

    (:goal
        (forall (?t - tarea) (revisada ?t))
    )

    (:metric minimize (+ (* 0.5 (ttotal)) (* 0.5 (ntrabajadores))))
)