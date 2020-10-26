import sys
import os
from collections import defaultdict
import getpass
class Namespace:
    pass
def reverse_dictionary(oDict):
    #nDict = type(oDict)()
    nDict = defaultdict(list)
    for key, value_sequence in oDict.items():
        for value in value_sequence:
            nDict[value].append(key)
    return nDict
def get_username( prompt='username:', var=None ):
    return (var and os.environ.get(var,None)) or input(prompt)
def get_password( prompt='password:', var=None ):
    return (var and os.environ.get(var,None)) or getpass.getpass(prompt)
def lmap(f,seq):
    return list(map(f,seq))

class UniqExc(Exception): pass
class UniqTooFew(UniqExc): pass
class UniqTooMany(UniqExc): pass
def unique(oSeq):
    oList = list(oSeq)
    if   len(oList) > 1: raise UniqTooMany
    elif len(oList) < 1: raise UniqTooFew
    else: return oList[0]



def _unzip2(pairs):
    a=[pairs[0] for pair in pairs]
    b=[pairs[1] for pair in pairs]
    return a,b
lfilter = lambda *x  : list(filter(*x))
prefix_test_4_prefix = lambda PREFIX : lambda STRING : STRING.startswith(PREFIX)
fTRUE = lambda x: True
fID = lambda x: x






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
