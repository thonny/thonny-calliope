from thonnycontrib.micropython import MicroPythonProxy, MicroPythonConfigPage
from thonny.globals import get_workbench

class CalliopeMiniProxy(MicroPythonProxy):
    @property
    def firmware_filetypes(self):
        return [('*.hex files', '.hex'), ('all files', '.*')]

class CalliopeMiniConfigPage(MicroPythonConfigPage):
    pass

def load_early_plugin():
    get_workbench().set_default("CalliopeMini.port", "auto")
    get_workbench().add_backend("CalliopeMini", CalliopeMiniProxy, 
                                "MicroPython on Calliope mini", CalliopeMiniConfigPage)

