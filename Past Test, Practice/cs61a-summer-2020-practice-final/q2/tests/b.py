test = {
  'name': 'b',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> double = lambda x: x*2
          
          >>> square = lambda x: x**2
          
          >>> identity = lambda x: x
          
          >>> t1 = Tree(double, [Tree(square), Tree(identity)])
          
          >>> t2 = Tree(6, [Tree(2), Tree(10)])
          
          >>> apply_tree(t1, t2)
          
          >>> t2
          Tree(12, [Tree(4), Tree(10)])
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
