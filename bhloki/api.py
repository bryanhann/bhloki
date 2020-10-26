import os
import sys
import getpass
import pickle
from collections import OrderedDict
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('args',nargs='+')
parser.add_argument('--user', action='store', default='bryanhann')
parser.add_argument('--path', action='store', default=os.environ.get('loki_dict', ''))
parser.add_argument('--hash', action='store', default='')
parser.add_argument('--skipempty', action='store_true')
parser.add_argument('--name', action='store', default='')
ARGS = parser.parse_args()

from github import Github, GithubException
import github

TEST_MAX=os.environ.get('loki_test_max')
TEST_MAX=TEST_MAX and int(TEST_MAX)

def err(x): sys.stderr.write(x+'\n'); sys.stderr.flush()
def out(x): sys.stdout.write(x+'\n'); sys.stdout.flush()
def url4name(name): return 'https://github.com/bryanhann/%s' % name

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

def acquire():
    def commits4repo(repo):
        try: return list(repo.get_commits())
        except GithubException: return list()
    username = os.environ.get( 'loki_user' ) or input('username:')
    password = os.environ.get( 'loki_pass' ) or getpass.getpass( 'password:')
    err( 'logging into github...' )
    hub = Github( username, password )
    err('done')
    user = hub.get_user()
    repos = user.get_repos()
    acc = dict()
    if TEST_MAX:
        repos = repos[:TEST_MAX]
    for repo in repos:
        err( repo.name )
        acc[ repo.name ] = []
        for commit in commits4repo(repo):
            acc[repo.name].append(commit.sha)
    return OrderedDict( sorted( acc.items() ) )

def cmd_dump(ARGS):
    old = pickle_read(ARGS.path)
    for k,vv in old.items():
        print(k)
        for v in vv:
            print('    ' + v)


def cmd_update(ARGS):
    DICTPATH=ARGS.path
    err( 'DICTPATH: ' + DICTPATH )
    old = pickle_read( DICTPATH  )
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
    if not ARGS.args:
        die(98, 'a sha must be provided')
    sha_prefix = ARGS.args[0]
    len(sha_prefix) > 4 or die(2,'too short')
    old = pickle_read( ARGS.path  ) or OrderedDict()
    for name,sha_seq in old.items():
        for sha in sha_seq:
            err(sha)
            if sha.startswith(sha_prefix):
                die(0,url4name(name))
    die(1,'not found')


if __name__=='__main__':
    import sys
    args = sys.argv[1:] + ['']*5
    cmdname = ARGS.args.pop(0)
    try:
        cmd = eval( 'cmd_' + cmdname )
    except:
        die(99, 'not a command: %s' % repr(cmdname))
    cmd(ARGS)
