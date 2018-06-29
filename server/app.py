# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
How do we want this to work?
-   Users are identified by ORCID
    -   OAuth is required to create an account (to verify ORCID)
    -   POST/DEL users with ORCID OAuth
    -   PUT users == other accounts (e.g., GitHub) requires other OAuth
-   Resources and their contribution scores are extracted regularly and
    automatically
    - Resource contributions must be publicly accessible by ORCID
-   Resources' contribution scores can be retrieved, but not edited, with API
    calls
    - No authentication required for GET calls
"""
import os

from eve import Eve
from eve.auth import TokenAuth
#from oauth2 import BearerAuth
from eve_swagger import swagger
from settings import settings

API_TOKEN = os.environ.get('API_TOKEN')


class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        return token == API_TOKEN

app = Eve(settings=settings, auth=TokenAuth)
app.register_blueprint(swagger, url_prefix='/api')
app.add_url_rule('/api', 'eve_swagger.index')

# required. See http://swagger.io/specification/#infoObject for details.
app.config['SWAGGER_INFO'] = {
    'title': 'nerdmetric API',
    'version': 'v1',
    'description': """Nerdmetric is an open-source metric quantifying
    researcher contributions to community resources.""",
}

if os.environ.get('SWAGGER_HOST', None):
    app.config['SWAGGER_HOST'] = os.environ.get('SWAGGER_HOST')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
