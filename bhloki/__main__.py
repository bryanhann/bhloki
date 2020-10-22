assert __name__ == '__main__'

from pprint import pprint
import argparse
from bhloki.util import *
from bhloki.constants import LOCAL, REMOTE
def _unzip2(pairs):
    a=[pairs[0] for pair in pairs]
    b=[pairs[1] for pair in pairs]
    return a,b
lfilter = lambda *x  : list(filter(*x))
prefix_test_4_prefix = lambda PREFIX : lambda STRING : STRING.startswith(PREFIX)
fTRUE = lambda x: True
fID = lambda x: x
def _hash():
    return ARGS.hash or die( 5, 'need to supply --hash flag' )

def filtered_dict( oDict, keytest=None, valtest=None):
    """(oDict, keytest, valtest) -> dictOfLists
    Filter a dictionary, returning a new dictionary of the same type.
    It is assumed that the dictionary values are lists.

    The keytest filters keys from the dictionary.
    The valtest filters items from the values.
    """
    for val in oDict.values(): assert type(val)==type([])
    nDict = type(oDict)()
    for key in filter( keytest, oDict.keys() ):
        nDict[key] = filter( valtest, oDict[key] )
    return nDict

def filtered4dict(
        old
        , kFilter   = fTRUE
        , vFilter   = fTRUE
        , vvMap     = fID
        , vvFilter  = fTRUE
    ):
    new = type(old)()
    for key,val in old.items():
        val = lfilter(vvFilter,lmap(vvMap,val))
        if kFilter(key) and vFilter(val):
            new[key]=val
    return new

#_value_filteredfiltered_dict_remove_empty( oDict, keytest=None, valtest=None):


COMMANDS = {}
def command(f):
    assert f.__doc__
    COMMANDS[f.__name__] = f

@command
def rlist():
    "list reverse dictionary items"
    printitems(sorted(LOCAL.rdict().items()))

@command
def _shas():
    "List all shas with the hash prefix. Requires --hash"
    for sha in sorted(LOCAL.shas4hash(_hash())):
        print(sha)

@command
def _sha():
    "Return the unique sha with the hash prefix. Requres --hash"
    pprint(LOCAL.sha4hash(_hash()))

@command
def find():
    "List the names for the given hash. Requires --hash"
    for name in LOCAL.names4sha(_hash()):
        print(name)

@command
def update():
    """Update the cached dictionary from github

    This is an interactive command that requires the user to supply credentials.

    Note: The current cached directory will be overwritten.
    """
    LOCAL.dict_write(REMOTE.dict())



@command
def _list():
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
    printitems( _dict.items() )


def cmd4name(name):
    try:
        return COMMANDS[name]
    except KeyError:
        die(11, "unrecognized: '%s'.  Try 'loki help'" )

@command
def help(subcommand=None):
    """print help. For help on a subcomand use 'help subcommand'"""
    if subcommand:
        doc = cmd4name(subcommand).__doc__
        print( 'Help for loki %s' % subcommand)
        print()
        print(doc)
    else:
        print('loki subcommands')
        for name, cmd in COMMANDS.items():
            doc = cmd.__doc__.split('\n')[0]
            print( '\t%s%s' % (name.ljust(10),doc) )
def main():
    name = ARGS.command[0]
    args = ARGS.command[1:]
    if not name in COMMANDS:
        die (9,  'not recognized: "%s"' % name )
    try:
        COMMANDS[name](*args)
    except UniqExc:
        die(6, 'hash either overdetermined or underdermined the sha!')

parser = argparse.ArgumentParser()
parser.add_argument('command',nargs='+')
parser.add_argument('--user', action='store', default='bryanhann')
parser.add_argument('--hash', action='store', default='')
parser.add_argument('--skipempty', action='store_true')
parser.add_argument('--path', action='store')
parser.add_argument('--name', action='store', default='')
ARGS = args = parser.parse_args()
main()
