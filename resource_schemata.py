CODE_SCHEMA = {
    'github__ME-ICA__tedana': {
        'id_type': 'github',
        'scores': ['commits', 'issues', 'lines'],
    },
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
    'other': {
        'id_type': 'other',
        'scores': ['test'],
    },
}
