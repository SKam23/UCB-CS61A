(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car(cdr s))
)

(define (caddr s)
  (car(cdr(cdr s)))
)


(define (sign num)
  (cond 
    ((< num 0) (- 0 1))
    ((> num 0) 1)
    (ELSE 0)
  )
) 


(define (square x) (* x x))

(define (pow x y)
  (if (even? y)
      (square(expt x (/ y 2)))
      (* x (square(expt x (/ (- y 1) 2)))  )
  )
)


(define (unique s)
  ( if  (null? s)
        nil
        (cons(car s) (filter(lambda (x) (not(equal? (car s) x)) ) (unique(cdr s))  )  )

          
  )
)


(define (replicate x n)
  (define (helper temp_list count)
      (if (= count n)
          temp_list
          (helper (append temp_list (list x)) (+ count 1))
          )
      )
  (helper nil 0)
  )


(define (accumulate combiner start n term)
  (define (helper count total)
        (if (> count n)
            total
            (helper (+ count 1)  (combiner total (term count)))
        )  
  )
  (helper 1 start)
)


(define (accumulate-tail combiner start n term)
  (define (helper count total)
        (if (> count n)
            total
            (helper (+ count 1)  (combiner total (term count)))
        )  
  )
  (helper 1 start)
)


(define-macro (list-of map-expr for var in lst if filter-expr)
 `(map(lambda (,var) ,map-expr) (filter(lambda (,var) ,filter-expr ) ,lst) )
  ;(list 'map(list 'lambda (list var) map-expr) (list 'filter(list 'lambda (list var) filter-expr ) lst) )

)

