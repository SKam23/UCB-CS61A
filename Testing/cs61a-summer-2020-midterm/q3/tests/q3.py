test = {
  'name': 'q3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> isinstance("abc", str)
          True
          
          >>> isinstance("abc", list)
          False
          
          >>> x = [200, 300]
          
          >>> x.append(x)
          
          >>> y = [x, x]              # this is the `y` from the doctests
          
          >>> night_y = night(y)      # this is the `night_y` from the doctests
          
          >>> len(night_y)
          2
          
          >>> night_y[0] is night_y[1]
          True
          
          >>> len(night_y[0])
          3
          
          >>> night_y[0][0]
          200
          
          >>> night_y[0][1]
          300
          
          >>> night_y[0][2] is night_y[0]
          True
          
          >>> night_y is y
          False
          
          >>> night_y[0] is y[0]
          False
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q3 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> a = []
          
          >>> night_a = night(a)
          
          >>> night_a
          []
          
          >>> night_a is a
          False
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q3 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> b = []
          
          >>> b.append(b)
          
          >>> night_b = night(b)
          
          >>> len(night_b)
          1
          
          >>> night_b is night_b[0]
          True
          
          >>> night_b is b
          False
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q3 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
