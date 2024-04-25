# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generos.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Genders(object):
    def setupUi(self, Genders):
        if not Genders.objectName():
            Genders.setObjectName(u"Genders")
        Genders.resize(542, 389)
        self.comboBox = QComboBox(Genders)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 50, 391, 31))
        self.botonGuardar = QPushButton(Genders)
        self.botonGuardar.setObjectName(u"botonGuardar")
        self.botonGuardar.setGeometry(QRect(300, 330, 111, 41))
        self.botonBorrar = QPushButton(Genders)
        self.botonBorrar.setObjectName(u"botonBorrar")
        self.botonBorrar.setGeometry(QRect(420, 330, 111, 41))
        self.label = QLabel(Genders)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 371, 41))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.genero_text = QLineEdit(Genders)
        self.genero_text.setObjectName(u"genero_text")
        self.genero_text.setGeometry(QRect(80, 330, 201, 41))
        self.tableWidget = QTableWidget(Genders)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 100, 521, 221))
        self.id_label = QLabel(Genders)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setGeometry(QRect(10, 330, 61, 41))
        self.id_label.setAutoFillBackground(True)
        self.id_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.LimpiarCampos = QPushButton(Genders)
        self.LimpiarCampos.setObjectName(u"LimpiarCampos")
        self.LimpiarCampos.setGeometry(QRect(410, 50, 121, 31))

        self.retranslateUi(Genders)

        QMetaObject.connectSlotsByName(Genders)
    # setupUi

    def retranslateUi(self, Genders):
        Genders.setWindowTitle(QCoreApplication.translate("Genders", u"Genders", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Genders", u"Genero", None))
        self.botonGuardar.setText(QCoreApplication.translate("Genders", u"Guardar", None))
        self.botonBorrar.setText(QCoreApplication.translate("Genders", u"Borrar", None))
        self.label.setText(QCoreApplication.translate("Genders", u"Generos", None))
        self.genero_text.setText("")
        self.genero_text.setPlaceholderText(QCoreApplication.translate("Genders", u"Genero:", None))
        self.id_label.setText(QCoreApplication.translate("Genders", u"Id:", None))
        self.LimpiarCampos.setText(QCoreApplication.translate("Genders", u"Limpiar Campos", None))
    # retranslateUi

