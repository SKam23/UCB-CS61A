test = {
  'name': 'q7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> subdrama(2233) # 22 counts
          True
          
          >>> subdrama(2444423) # 4444 counts
          True
          
          >>> subdrama(82223) # 22 counts even if it appears as part of 222
          True
          
          >>> subdrama(234562) # 2...2 does not count if the 2s are not consecutive
          False
          
          >>> subdrama(1) # 1 counts
          True
          
          >>> subdrama(498729879871) # 1 counts
          True
          
          >>> subdrama(149872987987) # 1 counts
          True
          
          >>> subdrama(4445555) # no dramas in this number
          False
          
          >>> subdrama(20) # no dramas in this number
          False
          """,
          'hidden': False
        }
      ],
      'scored': True,
      'setup': 'from q7 import *',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
