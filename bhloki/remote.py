from collections import OrderedDict
from github import Github, GithubException

from progress.bar import Bar

from bhloki.user import User
from bhloki.util import *
from bhloki.transforms import *

LIMIT=None

class Remote:
    def __init__(self):
        self.__user = None
        self.__hub = None
        self.__repos = None
        self.__items = None

    def _user(self):
        self.__user = self.__user or User()
        return self.__user

    def _hub(self):
        self.__hub = self.__hub or self.__network_hub()
        return self.__hub

    def _repos(self):
        self.__repos = self.__repos or list(self.__network_repos())
        return self.__repos

    def _items(self):
        self.__items = self.__items or list(self.__network_items())
        return self.__items

    def dict(self):
        return OrderedDict(sorted(self._items()))

    # Always call self.user().credentials() before any Bar() to insure that
    # any userinteraction takes place outside of bars.

    def __network_hub(self):
        self._user().credentials()
        with Bar('Loading hub  ', fill='@', suffix='%(percent).1f%% - %(eta)ds') as bar:
            bar.next()
            return Github( *self._user().credentials() )

    def __network_repos(self):
        self._user().credentials()
        with Bar('Loading repos', fill='@', suffix='%(percent).1f%% - %(eta)ds') as bar:
            for repo in self._hub().get_user().get_repos():
                bar.next()
                yield repo

    def __network_items(self):
        self._user().credentials()
        with Bar('Loading shas ', fill='@', suffix='%(percent).1f%% - %(eta)ds') as bar:
            repos = self._repos()
            # Set LIMIT to a small number for testing purposes
            if LIMIT:
                repos = repos[:LIMIT]
            for repo in repos:
                bar.next()
                yield item4repo(repo)




