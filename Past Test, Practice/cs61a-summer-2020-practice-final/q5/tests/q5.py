test = {
  'name': 'q5',
  'points': 9,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (first (next-run '(4 5 1 3 2)))
          (4 5)
          
          scm> (rest (next-run '(4 5 1 3 2)))
          (1 3 2)
          
          scm> (runs '(3 4 7 6 6 8 1 2 5 5 4))
          ((3 4 7) (6 6 8) (1 2 5 5) (4))
          
          scm> (runs '(4 3 2 3))
          ((4) (3) (2 3))
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
