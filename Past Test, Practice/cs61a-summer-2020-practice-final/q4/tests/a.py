test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t = Tree(4, [Tree(5, [Tree(6, [Tree(5)])]), Tree(1, [])])
          
          >>> tree_search(t, lambda x: x % 2 == 1)
          Link(1, Link(5, Link(5)))
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q4 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
