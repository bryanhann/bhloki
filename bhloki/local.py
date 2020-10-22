#!python
from collections import OrderedDict
from collections import defaultdict
import pickle

from bhloki.util import *

class Local:
    def __init__(self, dictpath):
        self._dict_path = dictpath
    def rdict(self):
        return reverse_dictionary(self.dict())
    def dict(self, path=None):
        if not self._dict_path.exists():
            self.write( OrderedDict() )
        with open(self._dict_path, 'rb') as fd:
            return pickle.load(fd)
    def dict_write(self,o):
        assert type(o) == type( OrderedDict() )
        with open(self._dict_path, 'wb') as fd:
            pickle.dump(o, fd)
    def dict_update(self,o):
        if not o == self.dict():
            self.dict_write(o)
            print('updatedodict')
    def shas4hash(self,hash):
        rdict = self.rdict()
        return [key for key in rdict if key.startswith(hash)]
    def sha4hash(self,hash):
        return unique(self.shas4hash(hash))
    def names4sha(self,sha):
        """Return the name of a repo that contains the supplied sha. A sha prefix is ok, if unique."""
        rdict = self.rdict()
        fullsha = unique( key for key in rdict if key.startswith(sha) )
        return rdict[fullsha]
        #[0]
        #except UniqTooMany:
        #    print('too many')
        #except UniqTooFew:
        #    print('too few')


