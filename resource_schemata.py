"""
Defines schemata (app names, associated id types, and associated scores) for
the three app types: 'code', 'data', and 'resource'.
"""

CODE_SCHEMA = {
    'github/ME-ICA__tedana': {
        'id_type': 'orcid',
        'scores': ['count'],
    },
    'github/neurostuff__NiMARE': {
        'id_type': 'orcid',
        'scores': ['count'],
    }
}

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
    'other': {
        'id_type': 'other',
        'scores': ['test'],
    },
}
