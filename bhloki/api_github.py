import os
import sys
import getpass
import pickle
from collections import OrderedDict
import argparse

from github import Github, GithubException
import github

from bhloki.api_constants import *
from bhloki.api_util import *

def commits4repo(repo):
    try: return list(repo.get_commits())
    except GithubException: return list()

def acquire():
    username = os.environ.get( 'loki_user' ) or input('username:')
    password = os.environ.get( 'loki_pass' ) or getpass.getpass( 'password:')
    err( 'logging into github...' )
    hub = Github( username, password )
    err('done')
    repos = list(hub.get_user().get_repos())
    repos = [repo for repo in repos if not repo.name in EXCLUDE_LIST ]
    if TEST_MAX:
        repos = repos[:TEST_MAX]
    acc = dict()
    for repo in repos:
        err( repo.name )
        acc[ repo.name ] = []
        for commit in commits4repo(repo):
            acc[repo.name].append(commit.sha)
    return OrderedDict( sorted( acc.items() ) )
