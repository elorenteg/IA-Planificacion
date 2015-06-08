(define (problem problema)
    (:domain tareas-ext3)
    (:objects 
        manage_gods handle_epilepsy involve_epilepsy further_stategovt enhance_tickets clarify_hubblespacetelescope tend_liveradio cause_stockcertificates update_dinosaurs enforce_english - tarea
        lisa_roberts - programador
    )
    (:init
        (= (dtarea manage_gods) 3) (= (ttarea manage_gods) 6) 
        (= (dtarea handle_epilepsy) 2) (= (ttarea handle_epilepsy) 1) 
        (= (dtarea involve_epilepsy) 2) (= (ttarea involve_epilepsy) 9) 
        (= (dtarea further_stategovt) 3) (= (ttarea further_stategovt) 3) 
        (= (dtarea enhance_tickets) 2) (= (ttarea enhance_tickets) 9) 
        (= (dtarea clarify_hubblespacetelescope) 3) (= (ttarea clarify_hubblespacetelescope) 4) 
        (= (dtarea tend_liveradio) 1) (= (ttarea tend_liveradio) 4) 
        (= (dtarea cause_stockcertificates) 3) (= (ttarea cause_stockcertificates) 9) 
        (= (dtarea update_dinosaurs) 2) (= (ttarea update_dinosaurs) 5) 
        (= (dtarea enforce_english) 1) (= (ttarea enforce_english) 7) 
        (= (hprog lisa_roberts) 3) (= (cprog lisa_roberts) 1) (= (nprog lisa_roberts) 0) 
        (= (ttotal) 0) 
    )
    (:goal
        (forall (?t - tarea) (revisada ?t))
    )
    (:metric minimize
        (ttotal)
    )
)