try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

NAME                = 'pyloki'
AUTHOR              = 'largo'
AUTHOR_EMAIL        = 'largo@pobox.com'
URL                 = 'https://github.com/sbryanhann/pippy'
LICENSE             = 'MIT'
ZIP_SAFE            =  False
VERSION             = '0.0.1' # manually bump version numbering in code to match
DESCRIPTION         = 'This is a one line description of the module.'
LONG_DESCRIPTION    = """ This is a long description of the module.\nIt is usually in some markup format.  """.strip()
SCRIPTS             = """ bin/loki bin/add.py bin/add.sh bin/loki-update bin/loki-url4sha """.split()
TEST_REQUIRES       = """ mock==4.0.2 pytest==6.1.1 pytest-regtest==1.4.5""".split()
INSTALL_REQUIRES    = """ PyGithub==1.53  progress==1.5""".split()
PACKAGES            = """ bhloki     """.split()
PACKAGE_DATA=dict()
PACKAGE_DATA['src'] = """ examples.*  """.split()

# hack to get testreuirements actually installed.
INSTALL_REQUIRES += TEST_REQUIRES

setup(
    name                  = NAME
    , description         = DESCRIPTION
    , long_description    = LONG_DESCRIPTION
    , author              = AUTHOR
    , url                 = URL
    , license             = LICENSE
    , author_email        = AUTHOR_EMAIL
    , version             = VERSION
    , install_requires    = INSTALL_REQUIRES
    , test_requires       = TEST_REQUIRES
    , packages            = PACKAGES
    , scripts             = SCRIPTS
    , zip_safe            = ZIP_SAFE
    , package_data        = PACKAGE_DATA
)
