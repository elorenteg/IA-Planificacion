(define (problem problema)
   (:domain tareas-ext4)
   (:objects t1 t2 t3 t4 t5 - tarea
             p1 p2 p3 p4 p5 p6 p7 p8 - programador)

    (:init
        (= (dtarea t1) 1) (= (ttarea t1) 7)
        (= (dtarea t2) 2) (= (ttarea t2) 9)
        (= (dtarea t3) 3) (= (ttarea t3) 10)
        (= (dtarea t4) 3) (= (ttarea t4) 2)
        (= (dtarea t5) 3) (= (ttarea t5) 0)
        
        (= (hprog p1) 2) (= (cprog p1) 1) (= (nprog p1) 0)
        (= (hprog p2) 2) (= (cprog p2) 2) (= (nprog p2) 0)
        (= (hprog p3) 2) (= (cprog p3) 1) (= (nprog p3) 0)
        (= (hprog p4) 3) (= (cprog p4) 2) (= (nprog p4) 0)
        (= (hprog p5) 3) (= (cprog p5) 2) (= (nprog p5) 0)
        (= (hprog p6) 2) (= (cprog p6) 1) (= (nprog p6) 0)
        (= (hprog p7) 2) (= (cprog p7) 1) (= (nprog p7) 0)
        (= (hprog p8) 3) (= (cprog p8) 1) (= (nprog p8) 0)


        (= (ntrabajadores) 0)
        (= (ttotal) 0)
    )

    (:goal
        (forall (?t - tarea) (revisada ?t))
    )

    (:metric minimize (+ (* 0.2 (ttotal)) (* 0.8 (ntrabajadores))))
)