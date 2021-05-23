test = {
  'name': 'b',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from special_drinks;
          assam|peach|tapioca pearl|5.0
          jasmine|peach|lychee jelly|4.5
          high mountain|peach|milk pudding|4.5
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
