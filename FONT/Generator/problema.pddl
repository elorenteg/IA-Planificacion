(define (problem problema)
    (:domain tareas-ext4)
    (:objects 
        license_maillists defend_moon formulate_movies influence_montecristogoldmine present_investing uncover_findpeople purchase_lotto accommodate_astronomy translate_kidssites refine_alzheimers - tarea
        marilyn_cunningham - programador
    )
    (:init
        (= (dtarea license_maillists) 2) (= (ttarea license_maillists) 9) 
        (= (dtarea defend_moon) 1) (= (ttarea defend_moon) 2) 
        (= (dtarea formulate_movies) 2) (= (ttarea formulate_movies) 2) 
        (= (dtarea influence_montecristogoldmine) 2) (= (ttarea influence_montecristogoldmine) 7) 
        (= (dtarea present_investing) 3) (= (ttarea present_investing) 6) 
        (= (dtarea uncover_findpeople) 1) (= (ttarea uncover_findpeople) 4) 
        (= (dtarea purchase_lotto) 2) (= (ttarea purchase_lotto) 10) 
        (= (dtarea accommodate_astronomy) 2) (= (ttarea accommodate_astronomy) 3) 
        (= (dtarea translate_kidssites) 1) (= (ttarea translate_kidssites) 5) 
        (= (dtarea refine_alzheimers) 1) (= (ttarea refine_alzheimers) 5) 
        (= (hprog marilyn_cunningham) 2) (= (cprog marilyn_cunningham) 1) (= (nprog marilyn_cunningham) 0) 
        (= (ttotal) 0) 
        (= (ntrabajadores) 0) 
    )
    (:goal
        (forall (?t - tarea) (revisada ?t))
    )
    (:metric minimize
        (+ (* 0.2 (ttotal)) (* 0.8 (ntrabajadores)))
    )
)