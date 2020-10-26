import os
import argparse
import bhloki.api_commands as commands
import bhloki.api_constants as CC
from bhloki.api_util import die
parser = argparse.ArgumentParser()
parser.add_argument('args',nargs='+')
parser.add_argument('--user', action='store', default=CC.GITHUB_USERNAME)
parser.add_argument('--path', action='store', default=CC.LOKI_DICT)
parser.add_argument('--hash', action='store', default='')
parser.add_argument('--name', action='store', default='')
ARGS = parser.parse_args()

if __name__=='__main__':
    cmdname = ARGS.args.pop(0)
    fullname = 'cmd_%s' %  cmdname
    try:
        cmd = getattr(commands, fullname)
    except:
        die(99, 'not a command: %s' % repr(cmdname))
    cmd(ARGS)
