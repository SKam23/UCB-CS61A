(define (rle s)
  (define (helper stri previous count)
    (cond ((null? stri) (cons-stream (list previous count) nil))
        ((= previous (car stri)) (helper (cdr-stream stri) previous (+ count 1)))
        (else (cons-stream (list previous count) (rle stri) ))
        
    )
  )
  (if(null? s)
    nil
    (helper (cdr-stream s) ( car s) 1))
)



(define (group-by-nondecreasing s)
    (define (helper s lis last)
        (cond 
            ((null? s) (cons-stream lis nil))
            ((<= last (car s) ) (helper (cdr-stream s) (append lis  (list (car s))) (car s)))
            ((> last (car s)) (cons-stream lis (helper s nil 0)  ))
            
            
        )
    
    
    )
    (helper s nil 0)
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

