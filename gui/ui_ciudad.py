# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ciudad.ui'
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

class Ui_Ciudad(object):
    def setupUi(self, Ciudad):
        if not Ciudad.objectName():
            Ciudad.setObjectName(u"Ciudad")
        Ciudad.resize(537, 429)
        self.comboBox = QComboBox(Ciudad)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 50, 391, 31))
        self.botonGuardar = QPushButton(Ciudad)
        self.botonGuardar.setObjectName(u"botonGuardar")
        self.botonGuardar.setGeometry(QRect(300, 380, 111, 41))
        self.botonBorrar = QPushButton(Ciudad)
        self.botonBorrar.setObjectName(u"botonBorrar")
        self.botonBorrar.setGeometry(QRect(420, 380, 111, 41))
        self.label = QLabel(Ciudad)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 371, 41))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.ciudad_text = QLineEdit(Ciudad)
        self.ciudad_text.setObjectName(u"ciudad_text")
        self.ciudad_text.setGeometry(QRect(80, 330, 201, 41))
        self.tableWidget = QTableWidget(Ciudad)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 100, 521, 221))
        self.id_label = QLabel(Ciudad)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setGeometry(QRect(10, 330, 61, 41))
        self.id_label.setAutoFillBackground(True)
        self.id_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.LimpiarCampos = QPushButton(Ciudad)
        self.LimpiarCampos.setObjectName(u"LimpiarCampos")
        self.LimpiarCampos.setGeometry(QRect(410, 50, 121, 31))
        self.combo_estados = QComboBox(Ciudad)
        self.combo_estados.setObjectName(u"combo_estados")
        self.combo_estados.setGeometry(QRect(300, 330, 231, 41))

        self.retranslateUi(Ciudad)

        QMetaObject.connectSlotsByName(Ciudad)
    # setupUi

    def retranslateUi(self, Ciudad):
        Ciudad.setWindowTitle(QCoreApplication.translate("Ciudad", u"Ciudades", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Ciudad", u"Ciudades:", None))
        self.botonGuardar.setText(QCoreApplication.translate("Ciudad", u"Guardar", None))
        self.botonBorrar.setText(QCoreApplication.translate("Ciudad", u"Borrar", None))
        self.label.setText(QCoreApplication.translate("Ciudad", u"Ciudades", None))
        self.ciudad_text.setText("")
        self.ciudad_text.setPlaceholderText(QCoreApplication.translate("Ciudad", u"Ciudad:", None))
        self.id_label.setText(QCoreApplication.translate("Ciudad", u"Id:", None))
        self.LimpiarCampos.setText(QCoreApplication.translate("Ciudad", u"Limpiar Campos", None))
        self.combo_estados.setPlaceholderText(QCoreApplication.translate("Ciudad", u"Estados:", None))
    # retranslateUi

