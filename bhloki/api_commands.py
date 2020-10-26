import os
import sys
from collections import OrderedDict
import argparse


from bhloki.api_constants  import *
from bhloki.api_util import *
from bhloki.api_github import *



def cmd_dump(ARGS):
    pprint_kvv_dikt( pickle_read(ARGS.path) )


def cmd_update(ARGS):
    DICTPATH=ARGS.path
    err( 'DICTPATH: ' + ARGS.path )
    old = pickle_read( ARGS.path )
    new = acquire()
    if old == new:
        die(3,'UNCHANGED')
    try:
        pickle_write(DICTPATH, new)
        assert new == pickle_read( DICTPATH  )
        die(0,'CHANGED')
    except Exception:
        raise

def cmd_url4sha(ARGS):
    ARGS.args or die(98, 'a sha must be provided')
    sha_prefix = ARGS.args[0]
    len(sha_prefix) > 4 or die(2,'too short')
    old = pickle_read( ARGS.path  ) or OrderedDict()
    for name,sha_seq in old.items():
        for sha in sha_seq:
            if sha.startswith(sha_prefix):
                print(GITHUB_PREFIX + '/' + name)
                exit()
            err(sha)
    die(1,'not found')

def parse():
    global ARGS
    parser = argparse.ArgumentParser()
    parser.add_argument('args',nargs='+')
    parser.add_argument('--user', action='store', default='bryanhann')
    parser.add_argument('--path', action='store', default=os.environ.get('loki_dict', ''))
    parser.add_argument('--hash', action='store', default='')
    parser.add_argument('--skipempty', action='store_true')
    parser.add_argument('--name', action='store', default='')
    ARGS = parser.parse_args()

def main():
    parse()
    cmdname = ARGS.args.pop(0)
    try:
        cmd = eval( 'cmd_' + cmdname )
    except:
        die(99, 'not a command: %s' % repr(cmdname))
    cmd(ARGS)
if __name__=='__main__':
    main()
