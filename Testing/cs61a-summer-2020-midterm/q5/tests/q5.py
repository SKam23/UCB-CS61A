test = {
  'name': 'q5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t = tree(10, [tree(20), tree(30)])
          
          >>> river = lambda x: tree(x, [tree(x + 1), tree(x + 2)])
          
          >>> print_tree(drawing(river, t))
          10
            11
              20
                21
                22
              30
                31
                32
            12
              20
                21
                22
              30
                31
                32
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q5 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> t = tree(1, [tree(2, [tree(3)])])
          
          >>> f = lambda x: tree(x * 10, [tree(x * 10 + 1)])
          
          >>> print_tree(drawing(f, t))
          10
            11
              20
                21
                  30
                    31
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q5 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
