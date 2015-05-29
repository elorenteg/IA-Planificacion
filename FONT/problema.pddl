(define (problem problema)
    (:domain tareas-ext3)
    (:objects 
        t1 t2 t3 t4 t5 t6 t7 t8 t9 t10 - tarea
        p1 p2 p3 p4 p5 p6 p7 p8 - programador
    )
    (:init
        (= (dtarea t1) 1) (= (ttarea t1) 7) 
        (= (dtarea t2) 3) (= (ttarea t2) 8) 
        (= (dtarea t3) 3) (= (ttarea t3) 1) 
        (= (dtarea t4) 1) (= (ttarea t4) 3) 
        (= (dtarea t5) 3) (= (ttarea t5) 3) 
        (= (dtarea t6) 2) (= (ttarea t6) 2) 
        (= (dtarea t7) 1) (= (ttarea t7) 5) 
        (= (dtarea t8) 1) (= (ttarea t8) 7) 
        (= (dtarea t9) 2) (= (ttarea t9) 7) 
        (= (dtarea t10) 3) (= (ttarea t10) 4) 
        (= (hprog p1) 3) (= (cprog p1) 1) (= (tprog p1) 0) (= (nprog p1) 0) 
        (= (hprog p2) 3) (= (cprog p2) 2) (= (tprog p2) 0) (= (nprog p2) 0) 
        (= (hprog p3) 2) (= (cprog p3) 2) (= (tprog p3) 0) (= (nprog p3) 0) 
        (= (hprog p4) 3) (= (cprog p4) 2) (= (tprog p4) 0) (= (nprog p4) 0) 
        (= (hprog p5) 3) (= (cprog p5) 2) (= (tprog p5) 0) (= (nprog p5) 0) 
        (= (hprog p6) 1) (= (cprog p6) 2) (= (tprog p6) 0) (= (nprog p6) 0) 
        (= (hprog p7) 1) (= (cprog p7) 2) (= (tprog p7) 0) (= (nprog p7) 0) 
        (= (hprog p8) 1) (= (cprog p8) 1) (= (tprog p8) 0) (= (nprog p8) 0) 
        (= (ttotal) 0) 
    )
    (:goal
        (forall (?t - tarea) (revisada ?t))
    )
    (:metric minimize
        (ttotal)
    )
)