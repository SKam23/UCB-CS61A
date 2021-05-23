test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from ryans_drinks;
          assam|mango|tapioca pearl
          assam|passionfruit|tapioca pearl
          assam|peach|tapioca pearl
          gong fu|mango|tapioca pearl
          gong fu|passionfruit|tapioca pearl
          gong fu|peach|tapioca pearl
          high mountain|peach|milk pudding
          jasmine|peach|lychee jelly
          osmanthus|peach|milk pudding
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
