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
