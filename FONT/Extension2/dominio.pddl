(define (domain tareas-ext2)
    (:requirements :adl :typing :strips :fluents)
    (:types
        tarea programador - object
    )
    
    (:predicates
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
    )
    
    (:action realiza
        :parameters (?t - tarea ?p - programador)
        :precondition (and (not (exists (?p2 - programador) (servida_por ?t ?p2)))
                           (<= (dtarea ?t) (+ (hprog ?p) 1)))
        :effect (and (servida_por ?t ?p) 
                     (increase (tprog ?p) (dtarea ?t))
                     (when (= (dtarea ?t) (+ (hprog ?p) 1)) (increase (tprog ?p) 2))
                     (when (= (cprog ?p) 1) (por_revisar_1 ?t))
                     (when (= (cprog ?p) 2) (por_revisar_2 ?t)))
    )

    (:action revisa
        :parameters (?t - tarea ?p - programador)
        :precondition (and (not (revisada ?t)) 
                           (or (por_revisar_1 ?t) 
                               (por_revisar_2 ?t))
                           (<= (dtarea ?t) (+ (hprog ?p) 1))
                           (forall (?p2 - programador) ;servida_por(t,p2) -> neq(p,p2)
                               (or (not (servida_por ?t ?p2))
                                   (not (= ?p ?p2)))))
        :effect (and (when (por_revisar_1 ?t) (and (revisada ?t) (increase (tprog ?p) 1)))
                     (when (por_revisar_2 ?t) (and (revisada ?t) (increase (tprog ?p) 2))))
    )
)