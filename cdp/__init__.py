from cdp import *
from cdp.data_items import *

from cdp.device_data_items import *

# Include .so's such that Cythonized cdp-py can still be properly imported
module_files = glob.glob(dirname(__file__)+"/*.py") + glob.glob(dirname(__file__)+"/*.so")
for module_file in module_files:
    if 'device_data_items' in module_file:
        module_name = ''
        if module_file.endswith('.py'):
            module_name = basename(module_file)[:-3]
        else:
            # Cython outputs to module_name.cpython-python_version-platform.so
            module_name = basename(module_file).split(".cpython")[0]

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
            if inspect.isclass(obj) and issubclass(obj, DeviceDataItem):
                DeviceData.register_dd_item(obj)

try:
    from cdp.private_network_commands import *
    # Include .so's such that Cythonized cdp-py can still be properly imported
    module_files = glob.glob(dirname(__file__)+"/*.py") + glob.glob(dirname(__file__)+"/*.so")
    for module_file in module_files:
        if 'network_commands' in module_file:
            module_name = ''
            if module_file.endswith('.py'):
                module_name = basename(module_file)[:-3]
            else:
                # Cython outputs to module_name.cpython-python_version-platform.so
                module_name = basename(module_file).split(".cpython")[0]

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
                if inspect.isclass(obj) and issubclass(obj, UWBNetworkCommandItem):
                    ExecuteDeviceCommandV2.register_cmd_item(obj)
except:
    pass

