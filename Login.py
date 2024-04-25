import sys
import app.Connection as Connection
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget, QApplication
from gui.ui_login import Ui_Login
from app.Menu import Menu

class Login(QWidget):
    login_successful = Signal()
    def __init__(self, parent=None):
        super(Login,self).__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.user = None
        self.password = None
        try:
            self.conexion = Connection.Connection()
        except Exception as e:
            print(f'Error: {e}')
        self.ui.login_button.clicked.connect(self.loginfunction)

    def loginfunction(self):
        self.user=self.ui.user.text()
        self.password=self.ui.password.text()
        if self.login(self.conexion, self.user, self.password):
            self.login_successful.emit()
            widget = Menu()
            widget.show()
        else:
            self.ui.user.clear()
            self.ui.password.clear()
        
    def login(self, conexion, user, password):
        if(user == '' and password == ''):
            print('Usuario o contraseña vacios')
            return False
        else:
            conexion.connect()
            sql = f"SELECT * FROM Usuarios WHERE Nombre = '{user}' AND Contraseña = '{password}'"
            result = conexion.select(sql)
            if len(result) > 0:
                conexion.disconnect()
                print('Login correcto')
                return True
            else:
                conexion.disconnect()
                print('Usuario o contraseña incorrectos')
                return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())