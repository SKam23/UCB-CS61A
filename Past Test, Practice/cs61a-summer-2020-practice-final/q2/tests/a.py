test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> [k for k in range(1000) if is_combo(357, k)]
          [0, 7, 12, 15, 22, 35, 56, 105]
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q2 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
