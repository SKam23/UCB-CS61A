test = {
  'name': 'q6',
  'points': 8,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (zero-cond ((0 'result1) ((- 1 1) 'result2) ((* 1 1) 'result3) (2 'result4)))
          result3
          
          scm> (zip-tail '(1 2 3) '(4 5 6))
          ((1 4) (2 5) (3 6))
          
          scm> (zip-tail '(c 6 a) '(s 1 ! hello world))
          ((c s) (6 1) (a !))
          
          scm> (append '(1 2 3) '(4 5 6))
          (1 2 3 4 5 6)
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
