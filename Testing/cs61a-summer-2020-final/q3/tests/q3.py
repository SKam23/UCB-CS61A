test = {
  'name': 'q3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> engine1 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
          
          >>> engine2 = Link(1, Link(4))
          
          >>> university([engine1, engine2])
          Link(0, Link(2, Link(3, Link(4, Link(5, Link(9))))))
          
          >>> engine1 # unchanged
          Link(0, Link(1, Link(2, Link(3, Link(5, Link(9))))))
          
          >>> engine2 # unchanged
          Link(1, Link(4))
          
          >>> engine1 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
          
          >>> engine2 = Link(1, Link(4))
          
          >>> university([engine1, engine1, engine2])
          Link(1, Link(4))
          
          >>> engine3 = Link(0, Link(1, Link(2, Link(3,  Link(5, Link(9))))))
          
          >>> engine4 = Link(1, Link(2, Link(3,  Link(5, Link(9)))))
          
          >>> university([engine3, engine4])
          Link(0)
          
          >>> university([engine1, engine2, engine3, engine4])
          Link(2, Link(3, Link(4, Link(5, Link(9)))))
          
          >>> s = Link(1, Link(2, Link(3, Link(4))))
          
          >>> len(s)
          4
          
          >>> s[2]
          3
          
          >>> s
          Link(1, Link(2, Link(3, Link(4))))
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q3 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> university([Link(1), Link(2), Link(3), Link(4), Link(5)])
          Link(1, Link(2, Link(3, Link(4, Link(5)))))
          
          >>> university([Link(1, Link(2, Link(3, Link(4, Link(5)))))])
          Link(1, Link(2, Link(3, Link(4, Link(5)))))
          
          >>> university([Link(1), Link.empty, Link(-2, Link(3))])
          Link(-2, Link(1, Link(3)))
          
          >>> university([Link(1), Link(1)]) is Link.empty
          True
          
          >>> university([Link(2), Link(2, Link(3)), Link(3)]) is Link.empty
          True
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': '>>> from q3 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
