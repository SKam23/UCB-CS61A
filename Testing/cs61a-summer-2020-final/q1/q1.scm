(define email "skam@berkeley.edu")

;; This question is in two parts, implementing `leadership-locator` and
;; `surgery-switch`. See the specifications above each definition
;; for details.
;;
;; NOTE: these parts are unrelated to each other, you can work on
;;    them in any order.

;; Part (a)
;; Implement `leadership-locator` which takes in a number `newspaper` and circles
;; all digits of value `9` in the number by returning a list of digits where all the
;; `9` digits are individually placed in a nested list.
;;
;; NOTE 1: Your function should be tail recursive
;; NOTE 2: You can use the `//` procedure defined below to perform floordiv
;; NOTE 3: You can use the builtin `modulo` procedure to perform modulo
;; NOTE 4: In all scheme/sql questions you can put a multi-line answer
;;    in a blank
;;
;; To run tests just for this part, run
;;      python3 ok -q a

(define (// numer denom) (floor (/ numer denom)))

;; scm> (leadership-locator 12)
;; (1 2)
;; scm> (leadership-locator 1991)
;; (1 (9) (9) 1)
;; scm> (leadership-locator 0) ; no digits
;; ()
;; scm> (leadership-locator 99999999)
;; ((9) (9) (9) (9) (9) (9) (9) (9))
;; scm> (leadership-locator 1129651)
;; (1 1 2 (9) 6 5 1)

(define (leadership-locator newspaper)
    (define (helper newspaper new)
        (define current-digit
            (modulo newspaper 10))
        (define value
            (if
                (= current-digit 9)
                (list 9)
                current-digit))
        (if (= newspaper 0 )
            new
            (helper
                (// newspaper 10)
                (cons value new))))
    (helper newspaper nil))

;; Part (b)
;; The `surgery-switch` operation takes in two infinite streams `aj` and `df`
;; and returns a new stream containing the non-chemistry elements of each stream,
;; alternating from one stream to the other when encountering the symbol
;; `chemistry`.
;;
;; Note: the symbol `chemistry` should not appear in the final stream.
;;
;;
;; To run tests just for this part, run
;;      python3 ok -q b

;; the following function is defined for testing, and takes the first
;; k elements of a stream `s`, returning them as a list.
(define (take k s)
    (if (zero? k)
        nil
        (cons
            (car s)
            (take (- k 1) (cdr-stream s)))))

;; scm> (define just-chemistry (cons-stream 'chemistry just-chemistry))
;; just-chemistry
;; scm> (define two (cons-stream 1 (cons-stream 'chemistry two)))
;; two
;; scm> (define three (cons-stream 'x (cons-stream 'y (cons-stream 'chemistry three))))
;; three
;; scm> (take 10 two)
;; (1 chemistry 1 chemistry 1 chemistry 1 chemistry 1 chemistry)
;; scm> (take 10 three)
;; (x y chemistry x y chemistry x y chemistry x)
;; scm> (take 10 (surgery-switch two three))
;; (1 x y 1 x y 1 x y 1)
;; scm> (take 10 (surgery-switch two just-chemistry))
;; (1 1 1 1 1 1 1 1 1 1)
;; scm> (take 10 (surgery-switch three three))
;; (x y x y x y x y x y)

(define (surgery-switch aj df)
	(if (eq? (car aj) 'chemistry )
		(surgery-switch df (cdr-stream aj))
		(cons-stream (car aj) (surgery-switch (cdr-stream aj) df ))))


; ORIGINAL SKELETON FOLLOWS

; ;; This question is in two parts, implementing `leadership-locator` and
; ;; `surgery-switch`. See the specifications above each definition
; ;; for details.
; ;;
; ;; NOTE: these parts are unrelated to each other, you can work on
; ;;    them in any order.

; ;; Part (a)
; ;; Implement `leadership-locator` which takes in a number `newspaper` and circles
; ;; all digits of value `9` in the number by returning a list of digits where all the
; ;; `9` digits are individually placed in a nested list.
; ;;
; ;; NOTE 1: Your function should be tail recursive
; ;; NOTE 2: You can use the `//` procedure defined below to perform floordiv
; ;; NOTE 3: You can use the builtin `modulo` procedure to perform modulo
; ;; NOTE 4: In all scheme/sql questions you can put a multi-line answer
; ;;    in a blank
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q a

; (define (// numer denom) (floor (/ numer denom)))

; ;; scm> (leadership-locator 12)
; ;; (1 2)
; ;; scm> (leadership-locator 1991)
; ;; (1 (9) (9) 1)
; ;; scm> (leadership-locator 0) ; no digits
; ;; ()
; ;; scm> (leadership-locator 99999999)
; ;; ((9) (9) (9) (9) (9) (9) (9) (9))
; ;; scm> (leadership-locator 1129651)
; ;; (1 1 2 (9) 6 5 1)

; (define (leadership-locator newspaper)
;     (define (helper newspaper ______)
;         (define current-digit
;             ______)
;         (define value
;             (if
;                 ______
;                 ______
;                 ______))
;         (if ______
;             ______
;             (helper
;                 ______
;                 (cons value ______))))
;     (helper ______ ______))

; ;; Part (b)
; ;; The `surgery-switch` operation takes in two infinite streams `aj` and `df`
; ;; and returns a new stream containing the non-chemistry elements of each stream,
; ;; alternating from one stream to the other when encountering the symbol
; ;; `chemistry`.
; ;;
; ;; Note: the symbol `chemistry` should not appear in the final stream.
; ;;
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q b

; ;; the following function is defined for testing, and takes the first
; ;; k elements of a stream `s`, returning them as a list.
; (define (take k s)
;     (if (zero? k)
;         nil
;         (cons
;             (car s)
;             (take (- k 1) (cdr-stream s)))))

; ;; scm> (define just-chemistry (cons-stream 'chemistry just-chemistry))
; ;; just-chemistry
; ;; scm> (define two (cons-stream 1 (cons-stream 'chemistry two)))
; ;; two
; ;; scm> (define three (cons-stream 'x (cons-stream 'y (cons-stream 'chemistry three))))
; ;; three
; ;; scm> (take 10 two)
; ;; (1 chemistry 1 chemistry 1 chemistry 1 chemistry 1 chemistry)
; ;; scm> (take 10 three)
; ;; (x y chemistry x y chemistry x y chemistry x)
; ;; scm> (take 10 (surgery-switch two three))
; ;; (1 x y 1 x y 1 x y 1)
; ;; scm> (take 10 (surgery-switch two just-chemistry))
; ;; (1 1 1 1 1 1 1 1 1 1)
; ;; scm> (take 10 (surgery-switch three three))
; ;; (x y x y x y x y x y)

; (define (surgery-switch aj df)
; 	(if ______
; 		______
; 		(cons-stream ______ ______)))

