import pytest
from bhloki.cli import main
from subprocess import *

UNIQUE_HASH = "3a0"
UNIQUE_SHA  = "3a08ca9070b547bb5a95fa00ef01e1042f8e9a74"
UNIQUE_NAME = ".cache.bh.zjot"

def out_err(cmd):
    p = Popen(cmd, shell=True, bufsize=100000, stderr=PIPE, stdin=PIPE, stdout=PIPE, close_fds=True)
    out = str(p.stdout.read(), 'utf-8')
    err = str(p.stderr.read(), 'utf-8')
    return out,err

def out(cmd): return out_err(cmd)[0].strip()

def dump(cmd):
    NEWLINE='\n'
    cmd_head = '---[command]--------------------------------'
    out_head = '---[stdout]--------------------------------'
    err_head = '---[stder]--------------------------------'
    out,err = out_err(cmd)
    return NEWLINE.join( [cmd_head , cmd , out_head , out , err_head , err] )

@pytest.fixture

def loki(regtest):
    prefix = 'loki .test '
    """Usage: [run('commandline string')]. It will run and out,err will be regtested."""
    return lambda cmd: regtest.write(dump(prefix + cmd))


if 1:
    def test_help(loki):        loki( 'help' )
    def test_help_rlist(loki):  loki( 'help rlist' )
    def test_help__shas(loki):  loki( 'help _shas' )
    def test_help__sha(loki):   loki( 'help _sha' )
    def test_help_find(loki):   loki( 'help find' )
    def test_help_update(loki): loki( 'help update' )
    def test_help_list(loki):   loki( 'help _list' )
    def test_help_help(loki):   loki( 'help help' )
if 1 and "testing _list":
    L = '_list'
    S = ' --skipempty'
    N = ' --name .c'
    H = ' --hash 3'
    X = ''
    def test_l____(loki):   loki( L+X+X+X )
    def test_l___s(loki):   loki( L+X+X+S )
    def test_l__n_(loki):   loki( L+X+N+X )
    def test_l__ns(loki):   loki( L+X+N+S )
    def test_l_h__(loki):   loki( L+H+X+X )
    def test_l_h_s(loki):   loki( L+H+X+S )
    def test_l_hn_(loki):   loki( L+H+N+X )
    def test_l_hns(loki):   loki( L+H+N+S )
    def test_rlist(loki):   loki( 'rlist'  )
    def test_shas_1(loki):     loki( '_shas ' )
    def test_shas_2(loki):     loki( '_shas --hash 3'    )
    def test_shas_3(loki):     loki( '_shas --hash 3a0'  )
    def test_sha_1(loki):     loki( '_sha ' )
    def test_sha_2(loki):     loki( '_sha --hash 3'    )
    def test_sha_3(loki):     loki( '_sha --hash 3a0'  )
if 1:
    def test_sha_return_value_1():  assert UNIQUE_SHA   == out( 'loki .test _sha --hash %s' % UNIQUE_HASH)
    def test_sha_return_value_2():  assert ""           == out( 'loki .test _sha --hash xxx' )
    def test_find():                assert UNIQUE_NAME  == out( 'loki .test find --hash %s' % UNIQUE_HASH)


