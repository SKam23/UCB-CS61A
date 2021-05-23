test = {
  'name': 'q4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> republic(['a', 'b', 'c'], [1, 2, 3])
          ['a', 'b', 'b', 'c', 'c', 'c']
          
          >>> republic(['a', 'b', 'c'], [3])
          ['a', 'a', 'a']
          
          >>> republic(['a', 'b', 'c'], [0, 2, 0])
          ['b', 'b']
          
          >>> republic([], [1,2,3])
          []
          
          >>> republic(['a', 'b', 'c'], [1, -1, 3])
          ['c', 'c', 'c']
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q4 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
