(define (problem problema)
    (:domain tareas-ext4)
    (:objects 
        Convey_CriminalJustice Revise_Epilepsy Conclude_Bankruptcy Lecture_WorldMaps - tarea
        William_James Nancy_Hughes Jacqueline_Harris Elizabeth_Welch Dennis_Smith - programador
    )
    (:init
        (= (dtarea Convey_CriminalJustice) 3) (= (ttarea Convey_CriminalJustice) 4) 
        (= (dtarea Revise_Epilepsy) 3) (= (ttarea Revise_Epilepsy) 4) 
        (= (dtarea Conclude_Bankruptcy) 1) (= (ttarea Conclude_Bankruptcy) 8) 
        (= (dtarea Lecture_WorldMaps) 1) (= (ttarea Lecture_WorldMaps) 4) 
        (= (hprog William_James) 3) (= (cprog William_James) 2) (= (nprog William_James) 0) 
        (= (hprog Nancy_Hughes) 3) (= (cprog Nancy_Hughes) 2) (= (nprog Nancy_Hughes) 0) 
        (= (hprog Jacqueline_Harris) 2) (= (cprog Jacqueline_Harris) 1) (= (nprog Jacqueline_Harris) 0) 
        (= (hprog Elizabeth_Welch) 3) (= (cprog Elizabeth_Welch) 2) (= (nprog Elizabeth_Welch) 0) 
        (= (hprog Dennis_Smith) 2) (= (cprog Dennis_Smith) 1) (= (nprog Dennis_Smith) 0) 
        (= (ttotal) 0) 
        (= (ntrabajadores) 0) 
    )
    (:goal
        (forall (?t - tarea) (revisada ?t))
    )
    (:metric minimize
        (* (ttotal) (ntrabajadores))
    )
)