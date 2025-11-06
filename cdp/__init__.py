from cdp import *
from cdp.data_items import *

from cdp.device_data_items import *
module_files = glob.glob(dirname(__file__)+"/*.py")
for module_file in module_files:
    if module_file.endswith('device_data_items.py'):
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
            if inspect.isclass(obj) and issubclass(obj, DeviceDataItem):
                DeviceData.register_dd_item(obj)

try:
    from cdp.private_network_commands import *
    module_files = glob.glob(dirname(__file__)+"/*.py")
    for module_file in module_files:
        if module_file.endswith('network_commands.py'):
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
                if inspect.isclass(obj) and issubclass(obj, UWBNetworkCommandItem):
                    ExecuteDeviceCommandV2.register_cmd_item(obj)
except:
    pass

