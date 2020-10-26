import os
EXCLUDE_LIST=[ '__index__' ]
TEST_MAX=os.environ.get('loki_test_max')
TEST_MAX=TEST_MAX and int(TEST_MAX)
GITHUB_PREFIX="https://github.com/bryanhann"
LOKI_DICT = os.environ.get('loki_dict', '')
GITHUB_USERNAME='bryanhann'
