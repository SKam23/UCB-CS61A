test = {
  'name': 'q2',
  'points': 14,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> [k for k in range(1000) if is_combo(357, k)]
          [0, 7, 12, 15, 22, 35, 56, 105]
          
          >>> double = lambda x: x*2
          
          >>> square = lambda x: x**2
          
          >>> identity = lambda x: x
          
          >>> t1 = Tree(double, [Tree(square), Tree(identity)])
          
          >>> t2 = Tree(6, [Tree(2), Tree(10)])
          
          >>> apply_tree(t1, t2)
          
          >>> t2
          Tree(12, [Tree(4), Tree(10)])
          
          >>> t1 = Tree(5, [Tree(2), Tree(1)])
          
          >>> fn_tree = make_checker_tree(t1)
          
          >>> t2 = Tree(5, [Tree(10), Tree(7)])
          
          >>> apply_tree(fn_tree, t2) #5 is a combo of 5, 10 is a combo of 52, 7 isn't a combo of 51
          
          >>> t2
          Tree(True, [Tree(True), Tree(False)])
          
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
      'setup': '>>> from q2 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
