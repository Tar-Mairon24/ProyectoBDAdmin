import sys
import connection
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QFile
from ui.ui_login import Ui_Login

class Login(QWidget):
    def __init__(self):
        super(Login,self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.user = None
        self.password = None
        self.ui.login_button.clicked.connect(self.loginfunction)
        self.conexion = connection.Connection()

    def loginfunction(self):
        self.user=self.ui.user.text()
        self.password=self.ui.password.text()
        
    def login(self):
        self.conexion.connect()
        sql = f"SELECT * FROM usuarios WHERE user = '{self.user}' AND password = '{self.password}'"
        result = self.conexion.select(sql)
        if len(result) > 0:
            print('Login correcto')
            self.conexion.disconnect()
            return True
        else:
            print('Login incorrecto')
            self.conexion.disconnect()
            return False