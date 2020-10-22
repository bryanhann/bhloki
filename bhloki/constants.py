import os
import pathlib
from bhloki.local import Local
from bhloki.remote import Remote

HOME = pathlib.Path(os.environ['HOME'])
DICT = HOME/'.config/tmp.loki.dict.6'
LOCAL = Local(dictpath=DICT)
REMOTE = Remote()
