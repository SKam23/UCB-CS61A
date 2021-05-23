test = {
  'name': 'b',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define zeros (cons-stream 0 zeros))
          zeros
          
          scm> (define ones (cons-stream 1 ones))
          ones
          
          scm> (take 10 (surgery-switch zeros ones))
          (0 0 0 0 0 0 0 0 0 0)
          
          scm> (take 10 (surgery-switch ones zeros))
          (1 1 1 1 1 1 1 1 1 1)
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'scm> (load-all ".")',
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (define a (cons-stream 0 (cons-stream 'chemistry (cons-stream 1 (cons-stream 'chemistry (cons-stream 2 a))))))
          a
          
          scm> (define b (cons-stream 'x (cons-stream 'chemistry (cons-stream 'y (cons-stream 'chemistry (cons-stream 2 a))))))
          b
          
          scm> (take 10 a)
          (0 chemistry 1 chemistry 2 0 chemistry 1 chemistry 2)
          
          scm> (take 10 b)
          (x chemistry y chemistry 2 0 chemistry 1 chemistry 2)
          
          scm> (take 10 (surgery-switch a b))
          (0 x 1 y 2 0 2 0 1 1)
          
          scm> (take 10 (surgery-switch b b))
          (x x y y 2 0 2 0 1 1)
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'scm> (load-all ".")',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
