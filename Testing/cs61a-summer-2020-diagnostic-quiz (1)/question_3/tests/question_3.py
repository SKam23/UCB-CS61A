test = {
  'name': 'question_3',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sculptural(1234, 1)
          4
          
          >>> sculptural(32749, 2)
          79
          
          >>> sculptural(1917, 2)
          97
          
          >>> sculptural(32749, 18)
          32749
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from question_3 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
