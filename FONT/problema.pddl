(define (problem problema)
    (:domain tareas-basic)
    (:objects 
        Enforce_InternetWebsite Entertain_KidsSites Tabulate_JohnWayne Conciliate_Basketball - tarea
        Barbara_Owens Juan_Mccoy Jessica_Fuller Kimberly_Sims William_Hill - programador
    )
    (:init
        (= (dtarea Enforce_InternetWebsite) 2) (= (ttarea Enforce_InternetWebsite) 4) 
        (= (dtarea Entertain_KidsSites) 2) (= (ttarea Entertain_KidsSites) 7) 
        (= (dtarea Tabulate_JohnWayne) 1) (= (ttarea Tabulate_JohnWayne) 9) 
        (= (dtarea Conciliate_Basketball) 2) (= (ttarea Conciliate_Basketball) 10) 
        (= (hprog Barbara_Owens) 3) (= (cprog Barbara_Owens) 1) 
        (= (hprog Juan_Mccoy) 3) (= (cprog Juan_Mccoy) 2) 
        (= (hprog Jessica_Fuller) 2) (= (cprog Jessica_Fuller) 2) 
        (= (hprog Kimberly_Sims) 3) (= (cprog Kimberly_Sims) 2) 
        (= (hprog William_Hill) 2) (= (cprog William_Hill) 1) 
    )
    (:goal
        (forall (?t - tarea) (servida ?t))
    )
)