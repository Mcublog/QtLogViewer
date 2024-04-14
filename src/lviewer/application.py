import logging
import sys

from pylogus import LOG_FORMAT, logger_init
from PyQt6.QtWidgets import QApplication

from lviewer.ui.qt.viewer import QtApplicationView

log = logger_init(__name__, logging.INFO)

class Application:

    app: QApplication

    #---------------------- Internal
    def __init__(self, view: QtApplicationView):
        self.app = QApplication(sys.argv)
        # styler.set_debug_pallete(self.app)
        self.view = view
        self.view.init()

    def run(self) -> int:
        self.view.show()
        res = self.app.exec()
        self.view.exit()
        return res
#----------------------
