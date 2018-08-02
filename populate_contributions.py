"""
Look through app-related files in "integrations/" and run "populate_database"
function within each. This function calls the API for the integration and
looks for user contributions associated with each of the users in the
nerdmetric database to fill out the nerdmetric contributions database for
that app.
"""
import sys
import os.path as op
from glob import glob
from importlib import import_module

sys.path.append('integrations/')

scripts = glob('integrations/*_.py')
for script in scripts:
    package = op.basename(script).replace('.py', '')
    module = import_module(package)
    if 'populate_database' in module.__dir__():
        module.populate_database()
