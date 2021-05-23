test = {
  'name': 'c',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t1 = Tree(5, [Tree(2), Tree(1)])
          
          >>> fn_tree = make_checker_tree(t1)
          
          >>> t2 = Tree(5, [Tree(10), Tree(7)])
          
          >>> apply_tree(fn_tree, t2) #5 is a combo of 5, 10 is a combo of 52, 7 isn't a combo of 51
          
          >>> t2
          Tree(True, [Tree(True), Tree(False)])
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
