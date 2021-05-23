; ---USAGE---

; python3 ok <name_of_function>

; e.g. python3 ok map-stream

; ---NOTES---

; - if you want to see the verbose output, run this:

;     python3 ok <name_of_function> -v

; - if you want to test all of your functions, run this:

;     python3 ok

;

;;; Discussion 12 - Streams ;;;

;;;;;;;;;;;;;;;;;;;
;;;   Streams   ;;;
;;;;;;;;;;;;;;;;;;;

(define (naturals n)
  (cons-stream n (naturals (+ n 1))))

(define nat (naturals 0))

; Q1.1 - WWSD
;;; No Tests
; (define (has-even? s) (cond ((null? s) #f) ((even? (car s)) #t) (else (has-even? (cdr-stream s)))))
; expect has-even?
; (define (f x) (* 3 x))
; expect f
; (define nums (cons-stream 1 (cons-stream (f 3) (cons-stream (f 5) nil))))
; expect nums
; (cdr nums)
; expect 'YOUR-CODE-HERE
; (cdr-stream nums)
; expect 'YOUR-CODE-HERE
; nums
; expect 'YOUR-CODE-HERE
; (define (f x) (* 2 x))
; expect f
; (cdr-stream nums)
; expect 'YOUR-CODE-HERE
; (cdr-stream (cdr-stream nums))
; expect 'YOUR-CODE-HERE
; (has-even? nums)
; expect 'YOUR-CODE-HERE

; Q1.2 - filter-stream
;;; No Tests

; Correct
(define (filter-stream f s)
  (cond
    ((null? s) nil)
    ((f (car s)) (cons-stream (car s) (filter-stream f (cdr-stream s))))
  (else (filter-stream f (cdr-stream s)))))

; Incorrect
; (define (filter-stream f s)
;   (if (null? s) nil
;     (let ((rest (filter-stream f (cdr-stream s))))
;       (if (f (car s))
;         (cons-stream (car s) rest)
;         rest))))

; Q1.3 - map-stream
;;; Tests
; (car (cdr-stream evens))
; expect 2

(define (map-stream f s)
  'YOUR-CODE-HERE
)
(define evens (map-stream (lambda (x) (* x 2)) nat))

; Q1.4 - slice
;;; Tests
; (slice nat 4 12)
; expect (4 5 6 7 8 9 10 11)

(define (slice s start end)
  'YOUR-CODE-HERE
)

(define (combine-with f xs ys)
  (if (or (null? xs) (null? ys))
    nil
    (cons-stream
      (f (car xs) (car ys))
      (combine-with f (cdr-stream xs) (cdr-stream ys)))))

; Q1.5i - factorials
;;; Tests
; (slice factorials 0 10)
; expect (1 1 2 6 24 120 720 5040 40320 362880)

(define factorials
  'YOUR-CODE-HERE
)

; Q1.5ii - fibs
;;; Tests
; (slice fibs 0 10)
; expect (0 1 1 2 3 5 8 13 21 34)

(define fibs
  'YOUR-CODE-HERE
)

; Q1.5iii - exp
;;; Tests
; (slice (exp 2) 0 5)
; expect (1 3 5 6.333333333333333 7)

(define (exp x)
  'YOUR-CODE-HERE
)

; Q1.6 - sieve
;;; Tests
; (slice primes 0 10)
; expect (2 3 5 7 11 13 17 19 23 29)

(define (sieve s)
  'YOUR-CODE-HERE
)

(define primes
  (sieve (naturals 2)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;   Extra Questions   ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;

; Q2.1 - make-lambda
;;; Tests
; (make-lambda (print 'hi))
; expect (lambda () (print (quote hi)))
; (make-lambda (/ 1 0))
; expect (lambda () (/ 1 0))
; ((make-lambda (print 3)))
; expect 3

(define-macro (make-lambda expr)
  'YOUR-CODE-HERE
)

; Q2.2 - make-stream
;;; Tests
; (define a (make-stream (print 1) (make-stream (print 2) nil)))
; expect 1
; expect a
; (define b (my-cdr-stream (make-stream (print 1) (make-stream (print 2) nil))))
; expect 1
; expect 2
; expect b
; (my-cdr-stream (my-cdr-stream (make-stream (print 1) (make-stream (print 2) nil))))
; expect 1
; expect 2
; expect ()

(define-macro (make-stream first second)
  'YOUR-CODE-HERE
)

(define (my-cdr-stream stream)
  'YOUR-CODE-HERE
)
