(define (domain tareas-ext1)
    (:requirements :adl :typing :strips)
    (:types
        tarea programador - object
    )
    
    (:predicates
        (servida ?t - tarea)
        (servida_por ?t - tarea ?p - programador)

        (revisada ?t - tarea)
    )
    
    (:functions
        (dtarea ?t - tarea)
        (ttarea ?t - tarea)
        
        (hprog ?p - programador)
        (cprog ?p - programador)
    )
    
    (:action realiza
        :parameters (?t - tarea ?p - programador)
        :precondition (and (not (servida ?t))
                           (<= (dtarea ?t) (+ (hprog ?p) 1)))
        :effect (and (servida_por ?t ?p) (servida ?t))
    )

    (:action revisa
        :parameters (?t - tarea ?p - programador)
        :precondition (and (servida ?t)
                           (not (revisada ?t)) 
                           (<= (dtarea ?t) (+ (hprog ?p) 1))
                           (not (servida_por ?t ?p)))
        :effect (revisada ?t)
    )
)
