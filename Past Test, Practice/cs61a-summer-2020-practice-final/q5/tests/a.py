test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (first (next-run '(4 5 1 3 2)))
          (4 5)
          
          scm> (rest (next-run '(4 5 1 3 2)))
          (1 3 2)
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
