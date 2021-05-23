test = {
  'name': 'c',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from toppings;
          lychee jelly|green|4
          milk pudding|oolong|4
          red bean|green|3
          tapioca pearl|black|5
          """,
          'hidden': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': 'sqlite> .read q7.sql',
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
