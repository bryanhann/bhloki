#import os
#import pathlib
#from bhloki.local import Local
#from bhloki.remote import Remote
#
#HOME = pathlib.Path(os.environ['HOME'])
#3DICT = HOME/'.config/tmp.loki.dict.6'
#3LOCAL = Local(dictpath=DICT)
#3REMOTE = Remote()
#######

import os
import pathlib
from bhloki.local import Local
from bhloki.remote import Remote

HOME = pathlib.Path(os.environ['HOME'])
HERE = pathlib.Path(__file__).parent
TEST_DICT = HERE/'examples/test_dict'
USER_DICT = HOME/'.config/tmp.loki.dict.6'

TEST = os.environ.get('loki_test')
DICT = TEST_DICT if TEST else USER_DICT

LOCAL = Local(dictpath=DICT)
REMOTE = Remote()
