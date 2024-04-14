from PyQt6.QtWidgets import QMainWindow

from lviewer.ui.qt.main.main_window_ui import Ui_MainWindow


class MainWindowUi(QMainWindow, Ui_MainWindow):

    def __init__(self, title: str):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"{title}")

    def exit(self):
        pass