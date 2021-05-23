(define email "skam@berkeley.edu")

; ; Su18 Mock Final q3, 5b
; ; This question is in two parts, implementing `zero-cond` and
; ; `zip-tail`. See the specifications above each definition
; ; for details.
; ; Part (a) (4 pt)
; ; Write a macro called zero-cond that takes in a list of clauses, where each clause is a two-element list containing
; ; two expressions, a predicate and a corresponding result expression. All predicates evaluate to a number. The macro
; ; should evaluate each predicate and return the value of the expression corresponding to the first true predicate,
; ; treating 0 as a false value.
; ;
; ; To run tests just for this part, run
; ;      python3 ok -q a
; ;
; ; scm> (zero-cond ((0 'result1) ((- 1 1) 'result2) ((* 1 1) 'result3) (2 'result4)))
; ; result3
(define-macro (zero-cond clauses)
  (cons 'cond
        (map (lambda (case)
               (cons `(not (= 0 ,(car case))) (cdr case)))
             clauses)))

; ; Part (b) (4 pt)
; ; Implement zip-tail, which is a tail recursive procedure that takes in two lists a and b and returns a
; ; single list containing two-element lists of co-indexed elements from a and b. If one list is shorter than the other,
; ; the zipped list’s length is that of the shorter list. Your solution should be tail recursive.
; ;
; ; To run tests just for this part, run
; ;      python3 ok -q b
; ;
; ; scm> (zip-tail '(1 2 3) '(4 5 6))
; ; ((1 4) (2 5) (3 6))
; ; scm> (zip-tail '(c 6 a) '(s 1 ! hello world))
; ; ((c s) (6 1) (a !))
; ; Hint: Use the built-in append procedure, which you can assume is tail recursive, to concatenate two lists
; ; together. For example:
; ; scm> (append '(1 2 3) '(4 5 6))
; ; (1 2 3 4 5 6)
(define (zip-tail a b)
  (define (zipper a b result)
    (if (or (null? a) (null? b))
        result
        (zipper (cdr a)
                (cdr b)
                (append result (list (list (car a) (car b)))))))
  (zipper a b nil))

; ORIGINAL SKELETON FOLLOWS
; ;; Su18 Mock Final q3, 5b
; ;; This question is in two parts, implementing `zero-cond` and
; ;; `zip-tail`. See the specifications above each definition
; ;; for details.
; ;; Part (a) (4 pt)
; ;; Write a macro called zero-cond that takes in a list of clauses, where each clause is a two-element list containing
; ;; two expressions, a predicate and a corresponding result expression. All predicates evaluate to a number. The macro
; ;; should evaluate each predicate and return the value of the expression corresponding to the first true predicate,
; ;; treating 0 as a false value.
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q a
; ;;
; ;; scm> (zero-cond ((0 'result1) ((- 1 1) 'result2) ((* 1 1) 'result3) (2 'result4)))
; ;; result3
; (define-macro (zero-cond clauses)
;      (cons 'cond
;           (map ______
;                  ______
;                 ______)))
; ;; Part (b) (4 pt)
; ;; Implement zip-tail, which is a tail recursive procedure that takes in two lists a and b and returns a
; ;; single list containing two-element lists of co-indexed elements from a and b. If one list is shorter than the other,
; ;; the zipped list’s length is that of the shorter list. Your solution should be tail recursive.
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q b
; ;;
; ;; scm> (zip-tail '(1 2 3) '(4 5 6))
; ;; ((1 4) (2 5) (3 6))
; ;; scm> (zip-tail '(c 6 a) '(s 1 ! hello world))
; ;; ((c s) (6 1) (a !))
; ;; Hint: Use the built-in append procedure, which you can assume is tail recursive, to concatenate two lists
; ;; together. For example:
; ;; scm> (append '(1 2 3) '(4 5 6))
; ;; (1 2 3 4 5 6)
; (define (zip-tail a b)
;     (define (zipper a b ______)
;         (if (or ______ ______)
;             ______
;             ______))
;     (zipper ______ ______ ______))
