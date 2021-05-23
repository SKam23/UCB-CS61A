test = {
  'name': 'question_2',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> conserve(1234, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 > 3 * 1
          True
          
          >>> conserve(11111111111112, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1 * 1 * ... * 1
          True
          
          >>> conserve(11111111111112, lambda x,y: x+y, lambda x,y: x+y) # 2 <= 1 + 1 + ... + 1
          False
          
          >>> conserve(12, lambda x,y: x+y, lambda x,y: x*y) # 2 > 1
          True
          
          >>> conserve(12345, lambda x,y: x+y, lambda x,y: x*y) # 4 + 2 <= 1 * 3 * 5
          False
          
          >>> conserve(18383, lambda x,y: x-y, lambda x,y: x-y) # 8 - 8 > 3 - 3 - 1
          True
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from question_2 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
