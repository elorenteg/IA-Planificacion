(define (problem problema)
(:domain dominio)
(:objects 
t1 t2 t3 t4 - tarea
p1 p2 p3 - programador
)
(:init
(= (dtarea t1) 2)(= (ttarea t1) 8)
(= (dtarea t2) 2)(= (ttarea t2) 7)
(= (dtarea t3) 1)(= (ttarea t3) 6)
(= (dtarea t4) 2)(= (ttarea t4) 7)
(= (hprog p1) 2)(= (cprog p1) 1)(= (tprog p1) 0)
(= (hprog p2) 1)(= (cprog p2) 1)(= (tprog p2) 0)
(= (hprog p3) 1)(= (cprog p3) 1)(= (tprog p3) 0)
)
(:goal
(forall (?t - tarea) (servida ?t))
)
