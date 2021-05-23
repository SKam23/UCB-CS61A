(define email "skam@berkeley.edu")

;; This question is in two parts, implementing `speaker-filter` and
;; `remove-comments`. See the specifications above each definition
;; for details.

;; You need to do part (a) to run the tests for part (b).

;; NOTE: In all scheme/sql questions you can put a multi-line answer
;;    in a blank


;; Part (a)
;; A speaker-filter is similar to a normal `filter` operation, except that
;; it involves deeply filtering the given list by removing all elements
;; that *do* match the predicate.
;;
;; NOTE 1: If the entire input matches the predicate, you should not delete it
;; NOTE 2: You can assume that `pred` can be called on an element of any type
;;
;; To run tests just for this part, run
;;      python3 ok -q a
;;
;; scm> (speaker-filter '(1 (2) (2 3)) (lambda (x) (and (number? x) (even? x))))
;; (1 () (3))
;; scm> (speaker-filter '(1 (2) (2 3) 4 5 6) list?)
;; (1 4 5 6)
;; scm> (speaker-filter '(1 2 3 4) list?)
;; (1 2 3 4)
;; scm> (speaker-filter '(i accidentally broke my computer) (lambda (x) (equal? x 'broke)))
;; (i accidentally my computer)
;; scm> (speaker-filter '(a (a) ((a)) (((a)))) (lambda (x) (equal? x 'a)))
;; (() (()) ((())))

(define (speaker-filter lst pred)
    (cond
        ((or (not (list? lst)) (null? lst))
            nil)
        ((pred (car lst))
            (speaker-filter (cdr lst) pred))
        (else
            (cons
                (car lst)
                (speaker-filter (cdr lst) pred)))))

;; Part (b)
;; Now implement the macro `remove-comments`, that takes in a piece of code
;; and evaluates it, ignoring the 'comments' within it.
;;
;; Comments are tagged lists that begin with the tag `comment-begins`
;;
;; scm> (remove-comments ((comment-begins hi) + 2 3))
;; 5
;; scm> (remove-comments '(this is (comment-begins even-when-quoted) a list))
;; (this is a list)
;; scm> (remove-comments '((this is not a comment comment-begins)))
;; ((this is not a comment comment-begins))

(define-macro (remove-comments code)
    (define (helper x)
        (lambda(finished_code) finished_code ))
    (speaker-filter code (lambda (cod) (equal? (car cod) 'comment-begins))))

; ORIGINAL SKELETON FOLLOWS

; ;; This question is in two parts, implementing `speaker-filter` and
; ;; `remove-comments`. See the specifications above each definition
; ;; for details.

; ;; You need to do part (a) to run the tests for part (b).

; ;; NOTE: In all scheme/sql questions you can put a multi-line answer
; ;;    in a blank


; ;; Part (a)
; ;; A speaker-filter is similar to a normal `filter` operation, except that
; ;; it involves deeply filtering the given list by removing all elements
; ;; that *do* match the predicate.
; ;;
; ;; NOTE 1: If the entire input matches the predicate, you should not delete it
; ;; NOTE 2: You can assume that `pred` can be called on an element of any type
; ;;
; ;; To run tests just for this part, run
; ;;      python3 ok -q a
; ;;
; ;; scm> (speaker-filter '(1 (2) (2 3)) (lambda (x) (and (number? x) (even? x))))
; ;; (1 () (3))
; ;; scm> (speaker-filter '(1 (2) (2 3) 4 5 6) list?)
; ;; (1 4 5 6)
; ;; scm> (speaker-filter '(1 2 3 4) list?)
; ;; (1 2 3 4)
; ;; scm> (speaker-filter '(i accidentally broke my computer) (lambda (x) (equal? x 'broke)))
; ;; (i accidentally my computer)
; ;; scm> (speaker-filter '(a (a) ((a)) (((a)))) (lambda (x) (equal? x 'a)))
; ;; (() (()) ((())))

; (define (speaker-filter lst pred)
;     (cond
;         ((or (not (list? lst)) (null? lst))
;             ______)
;         ((pred ______)
;             (speaker-filter ______ ______))
;         (else
;             (cons
;                 ______
;                 ______))))

; ;; Part (b)
; ;; Now implement the macro `remove-comments`, that takes in a piece of code
; ;; and evaluates it, ignoring the 'comments' within it.
; ;;
; ;; Comments are tagged lists that begin with the tag `comment-begins`
; ;;
; ;; scm> (remove-comments ((comment-begins hi) + 2 3))
; ;; 5
; ;; scm> (remove-comments '(this is (comment-begins even-when-quoted) a list))
; ;; (this is a list)
; ;; scm> (remove-comments '((this is not a comment comment-begins)))
; ;; ((this is not a comment comment-begins))

; (define-macro (remove-comments code)
;     (define (helper x)
;         ______)
;     (speaker-filter ______ ______))
