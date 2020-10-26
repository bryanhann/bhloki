from subprocess import *

def out_err(cmd):
    p = Popen(cmd, shell=True, bufsize=100000, stderr=PIPE, stdin=PIPE, stdout=PIPE, close_fds=True)
    out = str(p.stdout.read(), 'utf-8')
    err = str(p.stderr.read(), 'utf-8')
    return out,err

class RunObject:
    def __init__(self
        , name='Anon'
        , cmd = None
        , out = None
        , err = None
        , fo = lambda x:x
        , fe = lambda x:x
     ):
        self.name = name
        self.cmd = cmd
        self.out = out
        self.err = err
        self.fo = fo
        self.fe = fe
    def __repr__(self):
        return '<*** %s ***>' % self.name

class Gatherer:
    """Syntactic sugar for list appendage

    G = Gatherer()  # sets G._list=[]
    G + foo         # equivalent to G._list.append(foo)
    """
    def __init__(self):
        self._list = list()
    def __add__(self,other):
        self._list.append(other)
    def __sub__(self,other):
        pass
