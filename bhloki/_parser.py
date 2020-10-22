import argparse
parser = argparse.ArgumentParser()
parser.add_argument('command',nargs='+')
parser.add_argument('--user', action='store', default='bryanhann')
parser.add_argument('--hash', action='store', default='')
parser.add_argument('--skipempty', action='store_true')
parser.add_argument('--path', action='store')
parser.add_argument('--name', action='store', default='')
ARGS  = parser.parse_args()
ARGS.args = ARGS.command[1:] + ['']*5
ARGS.cmd = ARGS.command[0]
