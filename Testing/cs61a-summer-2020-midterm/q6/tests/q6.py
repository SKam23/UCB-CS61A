test = {
  'name': 'q6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> chisel_a = encyclopedia()
          
          >>> chisel_b, x = chisel_a(2)
          
          >>> x                                   # 2
          2
          
          >>> chisel_c, x = chisel_b(8)
          
          >>> x                                   # 2 - 8
          -6
          
          >>> chisel_d, x = chisel_c(12)
          
          >>> x                                   # 2 - 8 + 12
          6
          
          >>> chisel_e, x = chisel_d(30)
          
          >>> x                                   # 2 - 8 + 12 - 30
          -24
          
          >>> chisel_b_again, x = chisel_a(100)
          
          >>> x                                   # 100 [note that we are using chisel_a not chisel_d here]
          100
          
          >>> wallsocket(encyclopedia(), [1, 2, 3, 4, 5])
          3
          
          >>> wallsocket(encyclopedia(), [4000])
          4000
          
          >>> wallsocket(encyclopedia(), [2, 90])
          -88
          
          >>> wallsocket(identity_chisel, [2, 90])
          90
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q6 import *',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': '',
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q6 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
