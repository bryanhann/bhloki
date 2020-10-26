import os
import sys
import pickle
from collections import OrderedDict

if 'UTIL':
    def err(x): sys.stderr.write(x+'\n'); sys.stderr.flush()
    def out(x): sys.stdout.write(x+'\n'); sys.stdout.flush()
    def pprint_kvv_dikt(dikt):
        PAD4='    '
        for k,vv in dikt.items():
            print(k)
            for v in vv:
                print(PAD4 + v)

    def die(e,msg):
        assert type(e)==type(1)
        if e: err(msg)
        else: out(msg)
        exit(e)


    def pickle_write(path, o):
        with open(path, 'wb') as fd:
            pickle.dump(o, fd)

    def pickle_read(path):
        try:
            with open(path, 'rb') as fd:
                return pickle.load(fd)
        except FileNotFoundError:
            return None

