#!python
from collections import OrderedDict
from collections import defaultdict
import getpass

from github import GithubException
from github import Github

from progress.bar import Bar

from pyloki.util import *

class Remote:
    def __init__(self):
        self._hub = None
        self._username = None
        self._password = None
        self._dict = None
    def username(self):
        self._username = self._username or get_username(var='loki_user', prompt='github username:')
        return self._username
    def password(self):
        self._password = self._password  or get_password(var='loki_pass', prompt='github password:')
        return self._password
    def hub(s):
        s._hub = s._hub or Github( s.username(), s.password() )
        return s._hub
    def dict(self):
        if self._dict is None:
            self._dict = self.__network_gdict()
            LOCAL.dict_update(self._dict)
        return self._dict
    def __network_repos(self):
        acc_repos = []
        with Bar('Loading repos', fill='@', suffix='%(percent).1f%% - %(eta)ds') as bar:
            for repo in self.hub().get_user().get_repos():
                acc_repos.append(repo)
                bar.next()
        return acc_repos

    @staticmethod
    def commits4repo(repo):
        try:
            return list(repo.get_commits())
        except GithubException:
            return list()

    def __network_gdict(self):
        #item4repo = lambda repo : (repo.name, [commit.sha for commit in self.commits4repo(repo)])
        item4repo = lambda repo : (repo.name, [commit.sha for commit in repo.get_commits()])
        items = []
        with Bar('Loading shas ', fill='@', suffix='%(percent).1f%% - %(eta)ds') as bar:
            for repo in self.__network_repos()[:4]:
                try:
                    items.append( item4repo(repo) )
                except GithubException:
                    pass
                bar.next()
        return OrderedDict(sorted(items))





