test = {
  'name': 'b',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t3 = Tree(10, [Tree(20, [Tree("gate", [Tree("gate", [Tree("gate")])])]), Tree(30, [Tree(50, [Tree("gate", [Tree("gate")])])]), Tree(40, [Tree(70, [Tree("gate", [Tree("gate")])])])])
          
          >>> print(t3)
          10
              20
                  gate
                      gate
                          gate
              30
                  50
                      gate
                          gate
              40
                  70
                      gate
                          gate
          
          >>> smallest_no_gate(t3)
          [10, 20]
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
