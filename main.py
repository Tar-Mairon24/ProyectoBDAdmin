import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QFile
from ui.ui_login import Ui_Login
from ui.ui_mainwindow import Ui_MainWindow
from app.Login import Login

app=QApplication(sys.argv)
loginwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(loginwindow)
widget.show()
app.exec()
