# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'estados.ui'
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

class Ui_Estados(object):
    def setupUi(self, Estados):
        if not Estados.objectName():
            Estados.setObjectName(u"Estados")
        Estados.resize(542, 389)
        self.comboBox = QComboBox(Estados)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 50, 391, 31))
        self.botonGuardar = QPushButton(Estados)
        self.botonGuardar.setObjectName(u"botonGuardar")
        self.botonGuardar.setGeometry(QRect(300, 330, 111, 41))
        self.botonBorrar = QPushButton(Estados)
        self.botonBorrar.setObjectName(u"botonBorrar")
        self.botonBorrar.setGeometry(QRect(420, 330, 111, 41))
        self.label = QLabel(Estados)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 371, 41))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.estado_text = QLineEdit(Estados)
        self.estado_text.setObjectName(u"estado_text")
        self.estado_text.setGeometry(QRect(80, 330, 201, 41))
        self.tableWidget = QTableWidget(Estados)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 100, 521, 221))
        self.id_label = QLabel(Estados)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setGeometry(QRect(10, 330, 61, 41))
        self.id_label.setAutoFillBackground(True)
        self.id_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.LimpiarCampos = QPushButton(Estados)
        self.LimpiarCampos.setObjectName(u"LimpiarCampos")
        self.LimpiarCampos.setGeometry(QRect(410, 50, 121, 31))

        self.retranslateUi(Estados)

        QMetaObject.connectSlotsByName(Estados)
    # setupUi

    def retranslateUi(self, Estados):
        Estados.setWindowTitle(QCoreApplication.translate("Estados", u"Estados", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Estados", u"Genero", None))
        self.botonGuardar.setText(QCoreApplication.translate("Estados", u"Guardar", None))
        self.botonBorrar.setText(QCoreApplication.translate("Estados", u"Borrar", None))
        self.label.setText(QCoreApplication.translate("Estados", u"Estados", None))
        self.estado_text.setText("")
        self.estado_text.setPlaceholderText(QCoreApplication.translate("Estados", u"Genero:", None))
        self.id_label.setText(QCoreApplication.translate("Estados", u"Id:", None))
        self.LimpiarCampos.setText(QCoreApplication.translate("Estados", u"Limpiar Campos", None))
    # retranslateUi

