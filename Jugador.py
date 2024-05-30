import sys, re
import app.Connection as Connection
from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QMessageBox
from gui.ui_jugadores import Ui_Jugador

class Jugador(QWidget):
    def __init__(self, parent=None):
        super(Jugador,self).__init__(parent)
        self.ui = Ui_Jugador()
        self.ui.setupUi(self)
        try:
            self.conexion = Connection.Connection()
        except Exception as e:
            print(f'error: {e}')
        self.ui.botonGuardar.clicked.connect(self.guardar)
        self.cargarGeneros(self.conexion)
        self.cargarCategoria(self.conexion)
        self.ui.botonBorrar.clicked.connect(self.borrar)
        self.ui.LimpiarCampos.clicked.connect(self.limpiarCampos)
        self.ui.combo_categoria.currentIndexChanged.connect(self.cargarEquipos)
        self.ui.combo_equipo.currentIndexChanged.connect(self.generarTabla)
        self.ui.combo_equipo.currentIndexChanged.connect(self.actualizarLabelEquipo)
        self.ui.tableWidget.cellClicked.connect(self.seleccionarFila)

    def guardar(self):
        nombre = self.ui.nombre_text.text()
        paterno = self.ui.ApellidoPaterno_text.text()
        materno = self.ui.ApellidoMaterno_text.text()
        numero = self.ui.numero_text.text()
        celular = self.ui.telefono_text.text()
        equipo = self.seleccionarEquipo(self.conexion)
        genero = self.seleccionarGenero(self.conexion)
        id = self.ui.id_label.text()
        if nombre == '' or paterno == '' or materno == '' or numero == '' or celular == '':
            QMessageBox.warning(self, "Error", "No puedes dejar campos vacios")
        elif len(nombre) > 45 or len(paterno) > 45 or len(materno) > 45:
            QMessageBox.warning(self, "Error", "El Nombre, Apellido Paterno o Apellido Materno tienen muchos caracteres")
        elif not re.match("^[a-zA-Z]*$", nombre) or not re.match("^[a-zA-Z]*$", paterno) or not re.match("^[a-zA-Z]*$", materno):
            QMessageBox.warning(self, "Error", "El Nombre, Apellido Paterno, Apellido Materno deben contener solo letras")
        elif not re.match("^[0-9]*$", numero) or not re.match("^[0-9]*$", celular):
            QMessageBox.warning(self, "Error", "El Numero o Celular deben contener solo numeros")
        elif len(numero) > 2:
            QMessageBox.warning(self, "Error", "El Numero solo debe contener 2 digitos")
        elif len(celular) > 10:
            QMessageBox.warning(self, "Error", "El Celular solo debe contener 10 digitos")
        elif equipo == -1:
            QMessageBox.warning(self, "Error", "Selecciona un Equipo")
        elif self.ui.id_label.text() == 'Id:':
            self.insertar(self.conexion, nombre, paterno, materno, numero, celular, equipo, genero)
            self.limpiarCampos()
        else:
            self.update(self.conexion, id, nombre, paterno, materno, numero, celular, equipo, genero)
            self.limpiarCampos()

    def insertar(self, conexion, nombre, paterno, materno, numero, celular, equipo, genero):
        try:
            conexion.connect()
            sql = f'SELECT id_jugador FROM Jugador ORDER BY id_jugador DESC LIMIT 1'
            result = conexion.select(sql)
            if(len(result) > 0):
                id = int(result[0][0]) + 1
            else:
                id = 1
            sql = f"INSERT INTO Jugador VALUES({id}, '{nombre}', '{paterno}', '{materno}', '{numero}', '{celular}', {genero}, {equipo})"
            conexion.insertar(sql)
            conexion.commit()
            
        except Exception as e:
            print(f"Error: {e}") 
            conexion.rollback()

    def update(self, conexion, id, nombre, paterno, materno, numero, celular, equipo, genero):
        try:
            conexion.connect()
            id_jugador = id.split(" ")[1]
            sql = f"UPDATE Jugador SET Nombre = '{nombre}', Paterno = '{paterno}', Materno = '{materno}', Numero = '{numero}', id_genero = '{genero}', id_equipo = '{equipo}', Celular = '{celular}' WHERE id_jugador = {id_jugador}"
            conexion.update(sql)
            conexion.commit()
            conexion.disconnect()
        except Exception as e:
            print(f"Error: {e}")
            conexion.rollback()

    def borrar(self):
        if self.ui.nombre_text.text() == '' or self.ui.id_label.text() == 'Id:' or self.ui.ApellidoPaterno_text.text() == '' or self.ui.ApellidoMaterno_text.text() == '' or self.ui.numero_text.text() == '' or self.ui.telefono_text.text() == '' or self.ui.combo_equipo.currentText() == '' or self.ui.combo_genero.currentText() == '':
            QMessageBox.warning(self, "Error", "Llenar todos los campos a borrar")
        else:
            self.delete(self.conexion, self.ui.id_label.text())
            self.limpiarCampos()

    def delete(self, conexion, id):
        try:
            conexion.connect()
            id_jugador = id.split(" ")[1]
            sql = f"DELETE FROM Jugador WHERE id_jugador = {id_jugador}"
            conexion.delete(sql)
            conexion.commit()
        except Exception as e:
            print(f"Error: {e}")
            conexion.rollback()

    def seleccionarEquipo(self, conexion):
        try:
            equipo = self.ui.combo_equipo.currentText()
            categoria = self.seleccionarCategoria(conexion)
            conexion.connect()
            sql = f"SELECT id_equipo FROM Equipo WHERE Nombre = '{equipo}' and id_categoria = '{categoria}';"
            result = conexion.select(sql)
            conexion.disconnect()
            if len(result) > 0:
                return result[0][0]
            else:
                return -1
        except Exception as e:
            print(f"Error: {e}")

    def seleccionarGenero(self, conexion):
        try:
            genero = self.ui.combo_genero.currentText()
            conexion.connect()
            sql = f"SELECT id_genero FROM Genero WHERE Genero = '{genero}'"
            result = conexion.select(sql)
            conexion.disconnect()
            if len(result) > 0:
                return result[0][0]
            else:
                return -1
        except Exception as e:
            print(f"Error: {e}")

    def seleccionarCategoria(self, conexion):
        try:
            categoria = self.ui.combo_categoria.currentText()
            conexion.connect()
            sql = f"SELECT id_categoria FROM Categoria WHERE Descripcion = '{categoria}'"
            result = conexion.select(sql)
            conexion.disconnect()
            if len(result) > 0:
                return result[0][0]
            else:
                return -1
        except Exception as e:
            print(f"Error: {e}")

    def cargarEquipos(self):
        catergoria = self.seleccionarCategoria(self.conexion)
        try:
            self.conexion.connect()
            sql = f"SELECT Nombre FROM Equipo where id_categoria = {catergoria}"
            result = self.conexion.select(sql)
            self.conexion.disconnect()
            self.ui.combo_equipo.clear()
            for row in result:
                self.ui.combo_equipo.addItem(row[0])
        except Exception as e:
            print(f"Error: {e}")
    
    def cargarGeneros(self, conexion):
        try:
            conexion.connect()
            sql = f"SELECT Genero FROM Genero"
            result = conexion.select(sql)
            conexion.disconnect()
            self.ui.combo_genero.clear()
            for row in result:
                self.ui.combo_genero.addItem(row[0])
        except Exception as e:
            print(f"Error: {e}")

    def cargarCategoria(self, conexion):
        try:
            conexion.connect()
            sql = f"SELECT id_categoria, Descripcion FROM Categoria"
            result = conexion.select(sql)
            conexion.disconnect()
            self.ui.combo_categoria.clear()
            for row in result:
                self.ui.combo_categoria.addItem(row[1])
        except Exception as e:
            print(f"Error: {e}")

    def generarTabla(self):
        try:
            equipo = self.seleccionarEquipo(self.conexion)
            # Perform the select query using self.conexion
            self.conexion.connect()
            sql = f'select Nombre, Paterno, Materno, Numero, Celular from Jugador where id_equipo = {equipo};'
            result = self.conexion.select(sql)
            self.conexion.disconnect()
            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(5)
            self.ui.tableWidget.setHorizontalHeaderLabels(['Nombre', 'Apellido Paterno', 'Apellido Materno', 'Numero', 'Celular'])
            self.ui.tableWidget.setColumnWidth(1, 115)
            self.ui.tableWidget.setColumnWidth(2, 115)
            self.ui.tableWidget.setColumnWidth(3, 70)
            for row in range(len(result)):
                for col in range(5):
                    item = QTableWidgetItem(str(result[row][col]))
                    self.ui.tableWidget.setItem(row, col, item)
        except Exception as e:
            print(f'Error: {e}')

    def actualizarLabelEquipo(self):
        try:
            equipo = self.ui.combo_equipo.currentText()
            categoria = self.ui.combo_categoria.currentText()
            self.ui.equipo_label.setText(f'Equipo: {equipo} ({categoria})')
        except Exception as e:
            print(f'Error: {e}')

    def seleccionarFila(self, row):
        try:
            nombre = self.ui.tableWidget.item(row, 0).text()
            paterno = self.ui.tableWidget.item(row, 1).text()
            materno = self.ui.tableWidget.item(row, 2).text()
            numero = self.ui.tableWidget.item(row, 3).text()
            celular = self.ui.tableWidget.item(row, 4).text()
            self.ui.nombre_text.setText(nombre)
            self.ui.ApellidoPaterno_text.setText(paterno)
            self.ui.ApellidoMaterno_text.setText(materno)
            self.ui.numero_text.setText(numero)
            self.ui.telefono_text.setText(celular)
            self.conexion.connect()
            sql = f"SELECT id_jugador, id_genero FROM Jugador WHERE Nombre = '{nombre}' and Paterno = '{paterno}' and Materno = '{materno}' and Numero = '{numero}' and Celular = '{celular}';"
            result = self.conexion.select(sql)
            if len(result) > 0:
                id_jugador = result[0][0]
                id_genero = result[0][1]
            self.conexion.disconnect()
            self.ui.id_label.setText(f'Id: {id_jugador}')
            self.ui.combo_genero.setCurrentIndex(id_genero - 1)
            self.conexion.disconnect()
            self.conexion.connect()

        except Exception as e:
            print(f"Error: {e}")
        
    def limpiarCampos(self):
        self.ui.ApellidoMaterno_text.clear()
        self.ui.ApellidoPaterno_text.clear()
        self.ui.nombre_text.clear()
        self.ui.numero_text.clear()
        self.ui.telefono_text.clear()
        self.cargarGeneros(self.conexion)
        self.ui.id_label.setText("Id:")   
        self.ui.tableWidget.clearSelection() 
        self.generarTabla()
    
if __name__ == "__main__":  
    app = QApplication(sys.argv)
    generos = Jugador()
    generos.show()
    sys.exit(app.exec())