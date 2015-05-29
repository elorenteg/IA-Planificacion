(define (problem problema)
    (:domain tareas-ext3)
    (:objects 
        t1 t2 t3 t4 - tarea
        p1 p2 p3 p4 p5 - programador
    )
    (:init
        (= (dtarea t1) 3) (= (ttarea t1) 1) 
        (= (dtarea t2) 1) (= (ttarea t2) 7) 
        (= (dtarea t3) 2) (= (ttarea t3) 10) 
        (= (dtarea t4) 2) (= (ttarea t4) 4) 
        (= (hprog p1) 3) (= (cprog p1) 1) (= (tprog p1) 0) (= (nprog p1) 0) 
        (= (hprog p2) 3) (= (cprog p2) 2) (= (tprog p2) 0) (= (nprog p2) 0) 
        (= (hprog p3) 1) (= (cprog p3) 2) (= (tprog p3) 0) (= (nprog p3) 0) 
        (= (hprog p4) 3) (= (cprog p4) 2) (= (tprog p4) 0) (= (nprog p4) 0) 
        (= (hprog p5) 1) (= (cprog p5) 1) (= (tprog p5) 0) (= (nprog p5) 0) 
    )
    (:goal
        (forall (?t - tarea) (revisada ?t))
    )
    (:minimize
        
    )
)