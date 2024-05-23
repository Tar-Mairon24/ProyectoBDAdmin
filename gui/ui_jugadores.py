# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jugadores.ui'
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

class Ui_Jugador(object):
    def setupUi(self, Jugador):
        if not Jugador.objectName():
            Jugador.setObjectName(u"Jugador")
        Jugador.resize(540, 581)
        self.botonGuardar = QPushButton(Jugador)
        self.botonGuardar.setObjectName(u"botonGuardar")
        self.botonGuardar.setGeometry(QRect(300, 530, 111, 41))
        self.botonBorrar = QPushButton(Jugador)
        self.botonBorrar.setObjectName(u"botonBorrar")
        self.botonBorrar.setGeometry(QRect(420, 530, 111, 41))
        self.label = QLabel(Jugador)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 371, 41))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.nombre_text = QLineEdit(Jugador)
        self.nombre_text.setObjectName(u"nombre_text")
        self.nombre_text.setGeometry(QRect(10, 330, 281, 41))
        self.tableWidget = QTableWidget(Jugador)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 90, 521, 221))
        self.LimpiarCampos = QPushButton(Jugador)
        self.LimpiarCampos.setObjectName(u"LimpiarCampos")
        self.LimpiarCampos.setGeometry(QRect(10, 530, 131, 41))
        self.combo_genero = QComboBox(Jugador)
        self.combo_genero.setObjectName(u"combo_genero")
        self.combo_genero.setGeometry(QRect(300, 330, 231, 41))
        self.ApellidoPaterno_text = QLineEdit(Jugador)
        self.ApellidoPaterno_text.setObjectName(u"ApellidoPaterno_text")
        self.ApellidoPaterno_text.setGeometry(QRect(10, 380, 281, 41))
        self.ApellidoMaterno_text = QLineEdit(Jugador)
        self.ApellidoMaterno_text.setObjectName(u"ApellidoMaterno_text")
        self.ApellidoMaterno_text.setGeometry(QRect(10, 430, 281, 41))
        self.numero_text = QLineEdit(Jugador)
        self.numero_text.setObjectName(u"numero_text")
        self.numero_text.setGeometry(QRect(10, 480, 81, 41))
        self.telefono_text = QLineEdit(Jugador)
        self.telefono_text.setObjectName(u"telefono_text")
        self.telefono_text.setGeometry(QRect(100, 480, 191, 41))
        self.combo_equipo = QComboBox(Jugador)
        self.combo_equipo.setObjectName(u"combo_equipo")
        self.combo_equipo.setGeometry(QRect(300, 380, 231, 41))
        self.combo_categoria_edad = QComboBox(Jugador)
        self.combo_categoria_edad.setObjectName(u"combo_categoria_edad")
        self.combo_categoria_edad.setGeometry(QRect(300, 430, 231, 41))
        self.combo_categoria_genero = QComboBox(Jugador)
        self.combo_categoria_genero.setObjectName(u"combo_categoria_genero")
        self.combo_categoria_genero.setGeometry(QRect(300, 480, 231, 41))
        self.equipo_label = QLabel(Jugador)
        self.equipo_label.setObjectName(u"equipo_label")
        self.equipo_label.setGeometry(QRect(10, 60, 521, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.equipo_label.setFont(font1)
        self.equipo_label.setStyleSheet(u"background-color: rgb(84, 84, 84);\n"
"border-radius:3px;\n"
"border-color: rgb(29, 29, 29);")
        self.equipo_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Jugador)

        QMetaObject.connectSlotsByName(Jugador)
    # setupUi

    def retranslateUi(self, Jugador):
        Jugador.setWindowTitle(QCoreApplication.translate("Jugador", u"Jugadores", None))
        self.botonGuardar.setText(QCoreApplication.translate("Jugador", u"Guardar", None))
        self.botonBorrar.setText(QCoreApplication.translate("Jugador", u"Borrar", None))
        self.label.setText(QCoreApplication.translate("Jugador", u"Jugadores", None))
        self.nombre_text.setText("")
        self.nombre_text.setPlaceholderText(QCoreApplication.translate("Jugador", u"Nombre:", None))
        self.LimpiarCampos.setText(QCoreApplication.translate("Jugador", u"Limpiar Campos", None))
        self.combo_genero.setPlaceholderText(QCoreApplication.translate("Jugador", u"Genero:", None))
        self.ApellidoPaterno_text.setText("")
        self.ApellidoPaterno_text.setPlaceholderText(QCoreApplication.translate("Jugador", u"Apellido Paterno:", None))
        self.ApellidoMaterno_text.setText("")
        self.ApellidoMaterno_text.setPlaceholderText(QCoreApplication.translate("Jugador", u"Apellido Materno:", None))
        self.numero_text.setText("")
        self.numero_text.setPlaceholderText(QCoreApplication.translate("Jugador", u"Numero:", None))
        self.telefono_text.setText("")
        self.telefono_text.setPlaceholderText(QCoreApplication.translate("Jugador", u"Celular:", None))
        self.combo_equipo.setPlaceholderText(QCoreApplication.translate("Jugador", u"Equipo:", None))
        self.combo_categoria_edad.setPlaceholderText(QCoreApplication.translate("Jugador", u"Categoria Edad:", None))
        self.combo_categoria_genero.setPlaceholderText(QCoreApplication.translate("Jugador", u"Categoria Genero:", None))
        self.equipo_label.setText("")
    # retranslateUi

