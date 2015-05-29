(define (domain tareas-ext2)
    (:requirements :adl :typing :strips :fluents)
    (:types
        tarea programador - object
    )
    
    (:predicates
        (servida ?t - tarea)
        (servida_por ?t - tarea ?p - programador)

        (por_revisar_1 ?t - tarea)
        (por_revisar_2 ?t - tarea)
        (revisada ?t - tarea)
    )
    
    (:functions
        (dtarea ?t - tarea)
        (ttarea ?t - tarea)
        
        (hprog ?p - programador)
        (cprog ?p - programador)
        (tprog ?p - programador)
        
        (ttotal)
    )
    
    (:action realiza
        :parameters (?t - tarea ?p - programador)
        :precondition (and (not (servida ?t))
                           (<= (dtarea ?t) (+ (hprog ?p) 1)))
        :effect (and (servida_por ?t ?p) (servida ?t)
                     (increase (tprog ?p) (dtarea ?t))
                     (increase (ttotal) (dtarea ?t))
                     (when (= (dtarea ?t) (+ (hprog ?p) 1))
                        (and (increase (tprog ?p) 2)
                             (increase (ttotal) 2)))
                     (when (= (cprog ?p) 1) (por_revisar_1 ?t))
                     (when (= (cprog ?p) 2) (por_revisar_2 ?t)))
    )

    (:action revisa
        :parameters (?t - tarea ?p - programador)
        :precondition (and (not (revisada ?t)) 
                           (or (por_revisar_1 ?t) 
                               (por_revisar_2 ?t))
                           (<= (dtarea ?t) (+ (hprog ?p) 1))
                           (not (servida_por ?t ?p)))
        :effect (and (when (por_revisar_1 ?t)
                        (and (revisada ?t) (increase (tprog ?p) 1) (increase (ttotal) 1)))
                     (when (por_revisar_2 ?t)
                        (and (revisada ?t) (increase (tprog ?p) 2) (increase (ttotal) 2))))
    )
)
