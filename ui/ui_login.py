# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(400, 500)
        font = QFont()
        font.setPointSize(12)
        Login.setFont(font)
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 40, 98, 49))
        font1 = QFont()
        font1.setPointSize(26)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"\n"
"color: rgb(243, 243, 243);")
        self.label.setAlignment(Qt.AlignCenter)
        self.login_button = QPushButton(Login)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(140, 390, 131, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.login_button.setFont(font2)
        self.user = QLineEdit(Login)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(80, 220, 250, 40))
        self.password = QLineEdit(Login)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(80, 300, 250, 40))
        self.password.setEchoMode(QLineEdit.Password)
        self.imagen = QLabel(Login)
        self.imagen.setObjectName(u"imagen")
        self.imagen.setGeometry(QRect(150, 100, 101, 101))
        self.imagen.setPixmap(QPixmap(u"resources/3755575.png"))
        self.imagen.setScaledContents(True)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label.setText(QCoreApplication.translate("Login", u"Login", None))
        self.login_button.setText(QCoreApplication.translate("Login", u"Login", None))
        self.user.setPlaceholderText(QCoreApplication.translate("Login", u"Usuario:", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Login", u"Contrase\u00f1a:", None))
        self.imagen.setText("")
    # retranslateUi

