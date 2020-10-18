#!python
from pprint import pprint
from collections import OrderedDict
from collections import defaultdict
import time
import pickle
import sys
import os
import getpass
import pathlib

from github import GithubException
from github import Github

from progress.bar import Bar

HOME = pathlib.Path(os.environ.get('HOME', None))
CACHE=HOME/'.cache/loki.2'
LOCAL_DICT = CACHE/'github.bryanhann'
CACHE.exists() or CACHE.mkdir()

def github_dict_read():
    username = os.environ.get('loki_user', None)  or input('github username:')
    password = os.environ.get('loki_pass', None)  or getpass.getpass('github password')
    try:
        acc_repos = []
        with Bar('Loading repos', fill='@', suffix='%(percent).1f%% - %(eta)ds') as bar:
            for repo in Github( username, password ).get_user().get_repos():
                acc_repos.append(repo)
                bar.next()
        acc_items = []
        with Bar('Loading shas ', fill='@', suffix='%(percent).1f%% - %(eta)ds') as bar:
            for repo in acc_repos:
                try: commits = list(repo.get_commits())
                except GithubException: commits = list()
                name = repo.name
                shas = [ commit.sha for commit in commits ]
                acc_items.append( (name,shas) )
                bar.next()
        return OrderedDict( sorted(acc_items) )
    except OSError:
        sys.stderr.write( '\nconnection error\n' )
        exit(1)
    except GithubException:
        sys.stderr.write( '\ngithub exception\n' )
        exit(2)

def local_dict_write(dikt):
    with open(LOCAL_DICT, 'wb') as fd:
        pickle.dump(dikt, fd)

def local_dict_read():
    try:
        with open(LOCAL_DICT, 'rb') as fd:
            return pickle.load(fd)
    except FileNotFoundError:
        return OrderedDict()

def _dikt():
    return local_dict_read()

def _rdikt():
    acc = defaultdict(list)
    for name, shas in _dikt().items():
        for sha in shas:
            acc[sha].append(name)
    return acc


def name4sha(sha):
    """Return the name of a repo that contains the supplied sha. A sha prefix is ok, unless length<5"""
    if not len(sha) > 4:
        return None
    for (k,v) in load_rdikt().items():
        if k.startswith(sha):
            return v[0]
    else:
       return None

def main():
    new = github_dict_read()
    if new != local_dict_read():
        print('dumping new dikt')
        local_dict_write(new)


if __name__=='__main__':
    main()
