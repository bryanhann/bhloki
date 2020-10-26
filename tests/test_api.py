import sys
import pytest

import misc as MM
from api_testers import OBJECTS

@pytest.mark.parametrize("obj", OBJECTS)
def test_api(obj):
    if obj.name.startswith('0'):
        sys.stdout.write('\n ')
    print(obj)
    out,err = MM.out_err( obj.cmd )
    if obj.out is not None:
        assert obj.fo(out) == obj.out
    if obj.err is not None:
        assert obj.fe(err) == obj.err

