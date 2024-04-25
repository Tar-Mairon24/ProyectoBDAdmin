import sys
from PySide6.QtGui import QAction
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from gui.ui_menu import Ui_Menu

class Menu(QWidget):
    def __init__(self, parent=None):
        super(Menu,self).__init__(parent)
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Menu()
    widget.show()
    sys.exit(app.exec())
