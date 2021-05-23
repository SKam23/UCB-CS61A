(define email "skam@berkeley.edu")

;; Fa18 Final q5

;; This question is in two parts, implementing `next-run` and
;; `runs`. See the specifications above each definition
;; for details.

;; A data abstraction for a pair of a first run and the rest of a list.
(define (pair a b) (lambda (c) (if c a b)))
(define (first p) (p #t))
(define (rest p) (p #f))

;; Part (a)
;; Implement next-run, which takes a non-empty list of integers s and returns a pair of lists:
;; the longest non-decreasing prefix of s and the rest of s. Use the provided pair data abstraction.
;;
;; Your implementation should be correct even if the pair implementation were to change.
;;
;; Two equivalent definitions for what next-run should do:
;;  (1) Return a list of non-decreasing lists that together contain the elements of s.
;;  (2) Return a pair containing the first run in s (a list) and the rest of s (another list).
;;      -- this definition relies on information from part (b)
;;
;; To run tests just for this part, run
;;      python3 ok -q a
;;
;; scm> (first (next-run '(4 5 1 3 2)))
;; (4 5)
;; scm> (rest (next-run '(4 5 1 3 2)))
;; (1 3 2)

(define (next-run s)
    (if (or (null? (cdr s))
        (< (car(cdr s))(car s)))
        (pair (list(car s)) (cdr s))
        (begin
            (define p (next-run (cdr s)))
            (pair (cons (car s) (first p)) (rest p)))))

;; Part (b)
;; Now implement runs, a Scheme procedure that takes a list of integers s and returns a list of non-empty lists of
;; integers t. Together, the lists in t should contain all elements of s in order. The first element in each list in t
;; must be less than the last element in the previous list, if there is one. The rest of the elements in each list in
;; t must be greater than or equal to the previous element.
;;
;; scm> (runs '(3 4 7 6 6 8 1 2 5 5 4))
;; ((3 4 7) (6 6 8) (1 2 5 5) (4))
;; scm> (runs '(4 3 2 3))
;; ((4) (3) (2 3))

(define (runs s)
    (if (null? s) nil
        (let ((p (next-run s)))
            (cons (first p) (runs (rest p))))))

; ORIGINAL SKELETON FOLLOWS

; ;; Fa18 Final q5

; ;; This question is in two parts, implementing `next-run` and
; ;; `runs`. See the specifications above each definition
; ;; for details.

; ;; A data abstraction for a pair of a first run and the rest of a list.
; (define (pair a b) (lambda (c) (if c a b)))
; (define (first p) (p #t))
; (define (rest p) (p #f))

; ;; Part (a)
; ;; Implement next-run, which takes a non-empty list of integers s and returns a pair of lists:
; ;; the longest non-decreasing prefix of s and the rest of s. Use the provided pair data abstraction.
; ;;
; ;; Your implementation should be correct even if the pair implementation were to change.
; ;;
; ;; Two equivalent definitions for what next-run should do:
; ;;  (1) Return a list of non-decreasing lists that together contain the elements of s.
; ;;  (2) Return a pair containing the first run in s (a list) and the rest of s (another list).
; ;;      -- this definition relies on information from part (b)
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q a
; ;;
; ;; scm> (first (next-run '(4 5 1 3 2)))
; ;; (4 5)
; ;; scm> (rest (next-run '(4 5 1 3 2)))
; ;; (1 3 2)

; (define (next-run s)
;     (if (or ______
;         ______)
;         (pair ______ ______)
;         (begin
;             (define p (next-run (cdr s)))
;             (pair ______ ______))))

; ;; Part (b)
; ;; Now implement runs, a Scheme procedure that takes a list of integers s and returns a list of non-empty lists of
; ;; integers t. Together, the lists in t should contain all elements of s in order. The first element in each list in t
; ;; must be less than the last element in the previous list, if there is one. The rest of the elements in each list in
; ;; t must be greater than or equal to the previous element.
; ;;
; ;; scm> (runs '(3 4 7 6 6 8 1 2 5 5 4))
; ;; ((3 4 7) (6 6 8) (1 2 5 5) (4))
; ;; scm> (runs '(4 3 2 3))
; ;; ((4) (3) (2 3))

; (define (runs s)
;     (if (null? s) ______
;         (let ((p (next-run s)))
;             ______)))
