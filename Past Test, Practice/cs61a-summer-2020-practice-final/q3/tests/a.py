test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> cs61a_plus = Network()
          
          >>> cs61a_plus.add_friend('Robert', 'Jeffrey')
          
          >>> cs61a_plus.friends['Robert']
          ['Jeffrey']
          
          >>> cs61a_plus.friends['Jeffrey']
          ['Robert']
          
          >>> cs61a_plus.add_friend('Jessica', 'Robert')
          
          >>> cs61a_plus.friends['Robert']
          ['Jeffrey', 'Jessica']
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q3 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
