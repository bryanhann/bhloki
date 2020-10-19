#!python
import os
import pathlib
from pprint import pprint

from pyloki.local import Local
from pyloki.remote import Remote

HOME = pathlib.Path(os.environ['HOME'])
DICT = HOME/'.config/tmp.loki.dict.6'
LOCAL = Local(dictpath=DICT)
REMOTE = Remote()

def main():
    od = LOCAL.dict()
    pprint( od.keys() )
    if 0:
        gd = REMOTE.dict()
        pprint( gd.keys() )
    pprint(LOCAL.rdict())
    while 1:
        sha = input()
        print( LOCAL.name4sha(sha) )



if __name__=='__main__':
    main()
