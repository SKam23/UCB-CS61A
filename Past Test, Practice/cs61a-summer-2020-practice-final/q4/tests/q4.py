test = {
  'name': 'q4',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t = Tree(4, [Tree(5, [Tree(6, [Tree(5)])]), Tree(1, [])])
          
          >>> tree_search(t, lambda x: x % 2 == 1)
          Link(1, Link(5, Link(5)))
          
          >>> t = Tree(6, [Tree(3, [Tree(5, [Tree(9), Tree(2, [Tree(9)])]), Tree(1)]), Tree(4, [Tree(0, [Tree(4)])])])
          
          >>> org = Organizer([lambda x: x > 4, lambda x: x % 2 == 0])
          
          >>> org.categorize(t)
          [Link(9, Link(5, Link(6))), Link(0, Link(4, Link(2)))]
          
          >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
          
          >>> t.label
          3
          
          >>> t.branches[0].label
          2
          
          >>> t.branches[1].is_leaf()
          True
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
