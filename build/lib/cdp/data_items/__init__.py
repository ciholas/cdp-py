import inspect
import sys
import glob
from cdp.cdp import CDP, CDPDataItem
from os.path import dirname, basename
import importlib

module_files = glob.glob(dirname(__file__)+"/*.py")
for module_file in module_files:
    if not module_file.endswith('__init__.py'):
        module_name = basename(module_file)[:-3]

        # Import the module
        module = importlib.import_module(__package__+'.'+module_name)
        
        # Emulate from X import *
        if "__all__" in module.__dict__:
            names = module.__dict__['__all__']
        else:
            names = [x for x in module.__dict__ if not x.startswith('_')]
        globals().update({k: getattr(module, k) for k in names})

        # Get all data items in current module and register their types
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, CDPDataItem):
                CDP.register_data_item(obj)