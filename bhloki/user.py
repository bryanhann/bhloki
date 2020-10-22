from bhloki.util import *

ENVNAME_PASS = '_loki_pass'
ENVNAME_USER = '_loki_user'

class User:
    def __init__(self):
        self._username = None
        self._password = None

    def username(self):
        self._username = self._username or get_username(var=ENVNAME_USER, prompt='github username:')
        return self._username

    def password(self):
        self._password = self._password or get_password(var=ENVNAME_PASS, prompt='github password:')
        return self._password

    def credentials(self):
        return (self.username(), self.password())

