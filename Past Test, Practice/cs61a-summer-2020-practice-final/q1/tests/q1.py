test = {
  'name': 'q1',
  'points': 9,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> odds = Link (1 , Link (3 , Link (5 , Link (7))))
          
          >>> evens = Link (2 , Link (4 , Link (6 , Link (8))))
          
          >>> catch_up (odds , evens )
          
          >>> print ( odds ) # odds is mutated
          <1 3 5 7 1 1 1 1>
          
          >>> print ( evens )
          <2 4 6 8>
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q1 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
