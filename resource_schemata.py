"""
Defines schemata (app names, associated id types, and associated scores) for
the three app types: 'code', 'data', and 'resource'.
"""
with open('database/github_repositories.txt', 'r') as fo:
    repos = [l.strip() for l in fo.readlines()]
    repos = ['github/' + r.replace('/', '__') for r in repos]

CODE_SCHEMA = {}

for repo in repos:
    CODE_SCHEMA[repo] = {'id_type': 'orcid',
                         'scores': ['count']}

DATA_SCHEMA = {
    'openneuro': {
        'id_type': 'orcid',
        'scores': ['datasets'],
    },
}

RESOURCE_SCHEMA = {
    'appstract': {
        'id_type': 'orcid',
        'scores': ['score'],
    },
    'publons': {
        'id_type': 'orcid',
        'scores': ['merit', 'editor_merit'],
    },
}
