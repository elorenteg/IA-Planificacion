(define (problem problema)
    (:domain tareas-basic)
    (:objects 
        officiate_bankruptcy cause_statehomepages interact_science assist_heroes - tarea
        carol_andrews ryan_garrett amanda_armstrong ryan_gardner marie_wagner - programador
    )
    (:init
        (= (dtarea officiate_bankruptcy) 2) (= (ttarea officiate_bankruptcy) 5) 
        (= (dtarea cause_statehomepages) 1) (= (ttarea cause_statehomepages) 4) 
        (= (dtarea interact_science) 2) (= (ttarea interact_science) 8) 
        (= (dtarea assist_heroes) 1) (= (ttarea assist_heroes) 3) 
        (= (hprog carol_andrews) 3) (= (cprog carol_andrews) 1) 
        (= (hprog ryan_garrett) 1) (= (cprog ryan_garrett) 2) 
        (= (hprog amanda_armstrong) 3) (= (cprog amanda_armstrong) 1) 
        (= (hprog ryan_gardner) 2) (= (cprog ryan_gardner) 1) 
        (= (hprog marie_wagner) 2) (= (cprog marie_wagner) 1) 
    )
    (:goal
        (forall (?t - tarea) (servida ?t))
    )
)