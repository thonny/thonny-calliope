import os.path
from thonnycontrib.micropython import MicroPythonProxy, MicroPythonConfigPage
from thonny import get_workbench
from thonny.ui_utils import run_with_busy_window
from thonny.misc_utils import find_volume_by_name
import shutil

class CalliopeMiniProxy(MicroPythonProxy):
    pass

class CalliopeMiniConfigPage(MicroPythonConfigPage):
    pass

def flash_the_firmware():
    mount_path = find_volume_by_name("MINI",
                                     not_found_msg="Could not find disk '%s'.\n"
                                        + "Make sure you have Calliope Mini plugged in!\n\n"
                                        + "Do you want to continue and locate the disk yourself?")
    if mount_path is None:
        return
    
    hex_path = os.path.join(os.path.dirname(__file__), "res", "firmware.hex")
    def work():
        shutil.copy(hex_path, mount_path)
    
    run_with_busy_window(work, description="Copying firmware")

def load_plugin():
    get_workbench().set_default("CalliopeMini.port", "auto")
    get_workbench().add_backend("CalliopeMini", CalliopeMiniProxy, 
                                "MicroPython on Calliope mini", CalliopeMiniConfigPage)

    get_workbench().add_command("uploadmicropythoncalliope", "tools", "Upload MicroPython to Calliope Mini ...",
                                flash_the_firmware,
                                group=120)
