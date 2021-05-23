test = {
  'name': 'q3',
  'points': 9,
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
          
          >>> cs61a_plus = Network()
          
          >>> cs61a_plus.friends = {'Robert': ['Jeffrey', 'Jessica'], 'Jeffrey': ['Robert', 'Jessica', 'Yulin'], 'Jessica': ['Robert', 'Jeffrey', 'Yulin'], 'Yulin': ['Jeffrey', 'Jessica'], 'Albert': []}
          
          >>> cs61a_plus.degrees('Robert', 'Yulin', 2) # Exactly 2 degrees
          True
          
          >>> cs61a_plus.degrees('Robert', 'Jessica', 2) # Less than 2 degrees
          True
          
          >>> cs61a_plus.degrees('Yulin', 'Robert', 1) # More than 1 degree
          False
          
          >>> cs61a_plus.degrees('Albert', 'Jessica', 10) # No friends!
          False
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
