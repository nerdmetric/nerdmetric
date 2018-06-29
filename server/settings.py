import os


MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = '<your username>'
MONGO_PASSWORD = '<your password>'
MONGO_DBNAME = 'nerdmetric'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

user_schema = {
    'id_field': 'orcid',
    'resource_methods': ['GET', 'PATCH', 'PUT'],
    'item_methods': ['GET'],
    'schema': {
        'orcid': {
            'type': 'string',
            'unique': True,
            'required': True,
            },
        'email': {
            'type': 'string',
            'regex': '^\S+@\S+$',
            },
        'password': {
            'type': 'string',
            'minlength': 7,
            'required': True,
            },
        'givenname': {
            'type': 'string',
            'minlength': 1,
            'required': True,
            },
        'surname': {
            'type': 'string',
            'minlength': 1,
            'required': True,
            },
        'github': {
            'type': 'string',
            'unique': True,
            'required': False,
            },
        },
    }


settings = {
    'URL_PREFIX': 'api',
    'API_VERSION': 'v1',
    'ALLOWED_FILTERS': ['*'],
    'MONGO_HOST': os.environ.get('MONGODB_HOST', ''),
    'MONGO_PORT': os.environ.get('MONGODB_PORT', ''),
    'MONGO_DBNAME': 'nerdmetric_api',
    'PUBLIC_METHODS': ['GET'],
    'PUBLIC_ITEM_METHODS': ['GET'],
    'RESOURCE_METHODS': ['GET', 'POST', 'PUT', 'DELETE'],
    'ITEM_METHODS': ['GET', 'POST'],
    'X_DOMAINS': '*',
    'DOMAIN': {
        'user': {
            'item_title': 'user',
            'schema': user_schema,
            'additional_lookup': {
                'url': 'regex("[\w]+")',
                'field': 'orcid',
                },
        },
    }
}
