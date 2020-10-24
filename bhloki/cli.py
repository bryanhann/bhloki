# This module should be imported by [bhloki.__main__]
from pprint import pprint
from bhloki.util import *
from bhloki.constants import *
from bhloki._parser import parser
TAB = '    '
COMMANDS = dict()

def main():
    ARGS  = parser.parse_args()
    ARGS.args = ARGS.command[1:] + ['']*5
    ARGS.cmd = ARGS.command[0]
    # This function should be called by [bhloki.__main__]
    fn = COMMANDS.get(ARGS.cmd) or die(9,'unknown command: %s' % ARGS.cmd)
    try:
        fn(ARGS)
    except UniqExc:
        die(6, 'hash either overdetermined or underdermined the sha!')

def command(f):
    assert f.__doc__
    COMMANDS[f.__name__] = f

@command
def rlist(ARGS=None):
    "list reverse dictionary items"
    _pprint_items(sorted(LOCAL.rdict().items()))

@command
def _shas(ARGS=None):
    "List all shas with the hash prefix. Requires --hash"
    for sha in sorted(LOCAL.shas4hash(ARGS.hash)):
        print(sha)

@command
def _sha(ARGS=None):
    "Return the unique sha with the hash prefix. Requres --hash"
    print( LOCAL.sha4hash(ARGS.hash))

@command
def find(ARGS=None):
    "List the names for the given hash. Requires --hash"
    for name in LOCAL.names4sha(ARGS.hash):
        print(name)

@command
def update(ARGS=None):
    """Update the cached dictionary from github

    This is an interactive command that requires the user to supply credentials.

    Note: The current cached directory will be overwritten.
    """
    LOCAL.dict_write(REMOTE.dict())



@command
def _list(ARGS=None):
    """List items in the local dictionary. The output can be filtered with --name and --hash

    The output is a list of items formatted:
        repository-name
            sha-of-latest-commit
            ...
            sha-of-second-commit
            sha-of-initial-commit

    This output can be filtered with the following options:

        --name prefix : skip repository names that do not start with prefix
        --sha  prefix : skip shas that do not start with prefix
    """

    _dict = filtered4dict(
        LOCAL.dict()
        , vvMap      = fID
        , vvFilter   = prefix_test_4_prefix(ARGS.hash)
        , kFilter    = prefix_test_4_prefix(ARGS.name)
        , vFilter    = fID if ARGS.skipempty else fTRUE
    )
    _pprint_items( _dict.items() )


@command
def help(ARGS=None,*subcommand):
    """print help. For help on a subcomand use 'help subcommand'"""
    subcommand = ARGS.args[0]
    if not subcommand:
        print('loki subcommands')
        for name, cmd in COMMANDS.items():
            print( TAB*2 + name.ljust(10) + TAB + shortdoc(cmd) )
    elif subcommand in COMMANDS:
        print(COMMANDS[subcommand].__doc__)
    else:
        die(5,"unknown subcommand: '%s'" % subcommand)


# UI utilities:
def shortdoc(cmd):
    return cmd.__doc__.split('\n')[0]

def die(err, msg=''):
    msg = "[err:%s] loki: %s\n" % (err, msg)
    sys.stderr.write(msg)
    sys.stderr.flush()
    exit(err)

def _pprint_items(items):
    for k,vals in items:
        print(k)
        for val in vals:
            print('\t' + val)

