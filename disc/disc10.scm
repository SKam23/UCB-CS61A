; Discussion 10 - Scheme
; Note: this file does not include doctests

; Q3.1 - WWSD
(define a (+ 1 2))
; a
a
; 3
(define b (+ (* 3 3) (* 4 4)))
; b
(+ a b)
; 28
(= (modulo 10 3) (quotient 5 3))
; #t
(even? (+ (- (* 5 4) 3) 2))
; #f

; Q4.1 - WWSD
(if (or #t (/ 1 0)) 1 (/ 1 0))
; 1
(if (> 4 3) (+ 1 2 3 4) (+ 3 4 (* 3 2)))
; 10
((if (< 4 3) + -) 4 100)
; -96
(if 0 1 2)
; 1

; Q4.2 - factorial
(define (factorial x)
    (if (= x 1)  
            1
            (* x factorial((- x 1)))))

; Q4.3 - fib
(define (fib n)
    (if (<= n 1)
        n 
        (+ (fib(- n 2)) (fib(- n 1)))))

; Q5.1 - my-append
(define (my-append a b)
    (if(null? a)
        b
        (cons(car a) (my-append (cdr a) b ))))
; Q5.2 - insert
(define (insert element lst index)
    YOUR-CODE-HERE)

; Q5.3 - duplicate
(define (duplicate lst)
    YOUR-CODE-HERE)