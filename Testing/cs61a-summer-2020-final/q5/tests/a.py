test = {
  'name': 'a',
  'points': 0.1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM parta;
          car f
          car c
          car d
          """,
          'hidden': False
        }
      ],
      'ordered': True,
      'scored': True,
      'setup': 'sqlite> .read q5.sql',
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
