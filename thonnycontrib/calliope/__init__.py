from thonnycontrib.micropython import MicroPythonProxy, MicroPythonConfigPage
from thonny import get_workbench
from thonny.running import create_frontend_python_process
from thonny.ui_utils import SubprocessDialog

class CalliopeMiniProxy(MicroPythonProxy):
    pass

class CalliopeMiniConfigPage(MicroPythonConfigPage):
    pass

def flash_the_firmware():
    proc = create_frontend_python_process(['-u', '-m', 'uflash'])
    dlg = SubprocessDialog(get_workbench(), proc, "Uploading firmware", autoclose=False)
    dlg.wait_window()

def load_plugin():
    get_workbench().set_default("CalliopeMini.port", "auto")
    get_workbench().add_backend("CalliopeMini", CalliopeMiniProxy, 
                                "MicroPython on Calliope mini", CalliopeMiniConfigPage)

    get_workbench().add_command("uploadmicropythoncalliope", "tools", "Upload MicroPython to Calliope Mini ...",
                                flash_the_firmware,
                                group=120)
