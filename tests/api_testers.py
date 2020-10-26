from misc import RunObject, Gatherer

G=Gatherer()

G+RunObject( 'url4sha without sha'
    , cmd = 'python -m bhloki.api url4sha'
    , out = ''
    , err = 'a sha must be provided'
    , fe = lambda x:x.strip()
)

G+RunObject( 'url4sha with short sha'
    , cmd = 'python -m bhloki.api url4sha xx'
    , out = ''
    , err = 'too short\n'
)

G+RunObject( 'lookup with short sha'
    , cmd = 'loki-lookup xx'
    , out = ''
    , err = 'Already up to date.\ntoo short\n'
)
G+RunObject( 'lookup with a good sha'
    , cmd = 'loki-lookup e13f2'
    , out = 'https://github.com/bryanhann/...example...\n'
    , err = 'Already up to date.\n'
)

G+RunObject( 'lookup with a bad sha'
    , cmd = 'loki-lookup xxxxxx'
    , out = ''
    , err = 'Already up to date.\nnot found\n'
)

G+RunObject( 'loki-dump'
    , cmd = 'loki-dump e13f2'
    , out = '...example...\n    '
    , fo = lambda x: x[:18]
)
OBJECTS=G._list
for ii,obj in enumerate(OBJECTS):
    obj.name = '%s: %s' % (ii,obj.name)

