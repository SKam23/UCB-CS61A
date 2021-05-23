test = {
  'name': 'q6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t1 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])]), Tree(5)])
          
          >>> print(t1)
          1
              2
                  3
                      4
              5
          
          >>> pruner(t1, 2)
          
          >>> print(t1)
          1
              2
                  3
              5
                  gate
          
          >>> t2 = Tree(4, [Tree(5, [Tree(6), Tree(7)]), Tree(10), Tree(15, [Tree(16, [Tree(17, [Tree(18, [Tree(19)])])])])])
          
          >>> pruner(t2, 3)
          
          >>> print(t2)
          4
              5
                  6
                      gate
                  7
                      gate
              10
                  gate
                      gate
              15
                  16
                      17
          
          >>> t1 = Tree(1, [Tree(2, [Tree(3)]), Tree(5, [Tree("gate")])])
          
          >>> print(t1)
          1
              2
                  3
              5
                  gate
          
          >>> smallest_no_gate(t1)
          [1, 5]
          
          >>> t2 = Tree(4, [Tree(5, [Tree(6, [Tree("gate")]), Tree(7, [Tree("gate")])]), Tree(10, [Tree("gate", [Tree("gate")])]), Tree(15, [Tree(16, [Tree(17)])])])
          
          >>> print(t2)
          4
              5
                  6
                      gate
                  7
                      gate
              10
                  gate
                      gate
              15
                  16
                      17
          
          >>> smallest_no_gate(t2)
          [4, 10]
          
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
      'setup': '>>> from q6 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
