test = {
  'name': 'b',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (zip-tail '(1 2 3) '(4 5 6))
          ((1 4) (2 5) (3 6))
          
          scm> (zip-tail '(c 6 a) '(s 1 ! hello world))
          ((c s) (6 1) (a !))
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
