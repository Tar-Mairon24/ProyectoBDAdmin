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
        self.cargarEquipos(self.conexion)
        self.cargarGeneros(self.conexion)
        self.cargarCategoria(self.conexion)
        self.ui.botonBorrar.clicked.connect(self.borrar)
        self.ui.LimpiarCampos.clicked.connect(self.limpiarCampos)

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
            self.actualizarCampos()
        else:
            self.update(self.conexion, id, nombre, paterno, materno, numero, celular, equipo, genero)
            self.actualizarCampos()

    def insertar(self, conexion, nombre, paterno, materno, numero, celular, equipo, genero):
        try:
            conexion.connect()
            sql = f'SELECT id_jugador FROM Jugador ORDER BY id_jugador DESC LIMIT 1'
            result = conexion.select(sql)
            if(len(result) > 0):
                id = int(result[0][0]) + 1
            else:
                id = 1
            sql = f"INSERT INTO Jugador ALUES({id}, '{nombre}', '{paterno}', '{materno}', '{numero}', '{genero}', '{equipo}', '{celular}')"
            conexion.insertar(sql)
            conexion.commit()
            
        except Exception as e:
            print(f"Error: {e}") 
            conexion.rollback()

    def update(self, conexion, id, nombre, paterno, materno, numero, celular, equipo, genero):
        try:
            conexion.connect()
            sql = f"UPDATE Ciudad SET Nombre = '{nombre}', ApellidoPaterno = '{paterno}', ApellidoMaterno = '{materno}', Numero = '{numero}', Genero = '{genero}', Equipo = '{equipo}', Celular = '{celular}' WHERE id_jugador = {id}"
            conexion.update(sql)
            conexion.commit()
            conexion.disconnect()
        except Exception as e:
            print(f"Error: {e}")
            conexion.rollback()

    def borrar(self):
        if self.ui.nombre_text.text() == '' or self.ui.id_label.text() == 'Id:' or self.ui.ApellidoPaterno_text.text() == '' or self.ui.ApellidoMaterno_text.text() == '' or self.ui.numero_text.text() == '' or self.ui.telefono_text.text() == '' or self.ui.combo_equipo.currentText() == '' or self.ui.combo_genero.currentText() == '' or self.ui.combo_categoriaEdad.currentText() == '' or self.ui.combo_categoriaGenero.currentText() == '':
            QMessageBox.warning(self, "Error", "No hay elemento a borrar")
        else:
            self.delete(self.conexion, self.ui.id_label.text())
            self.actualizarCampos()

    def delete(self, conexion, id):
        try:
            conexion.connect()
            sql = f"DELETE FROM Ciudad WHERE and id_ciudad = {id}"
            conexion.delete(sql)
            conexion.commit()
        except Exception as e:
            print(f"Error: {e}")
            conexion.rollback()

    def seleccionarEquipo(self, conexion):
        try:
            equipo = self.ui.combo_equipo.currentText()
            conexion.connect()
            sql = f"SELECT id_equipo FROM Equipo WHERE Nombre = '{equipo}'"
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

    def cargarEquipos(self, conexion):
        try:
            conexion.connect()
            sql = f"SELECT Nombre FROM Equipo"
            result = conexion.select(sql)
            conexion.disconnect()
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
            sql = f'select Nombre, Paterno, Materno, Numero, Celular from Jugadores where id_equipo = {equipo};'
            result = self.conexion.select(sql)

            # Clear the table widget
            self.ui.tableWidget.clear()

            # Set the number of rows and columns in the table widget
            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(len(result[0]))
            self.ui.tableWidget.setHorizontalHeaderLabels(['Nombre', 'Paterno', 'Materno', 'Numero', 'Celular'])
            self.ui.tableWidget.setColumnWidth(0, 150)
            self.ui.tableWidget.setColumnWidth(1, 150)
            self.ui.tableWidget.setColumnWidth(2, 150)
            self.ui.tableWidget.setColumnWidth(3, 150)
            self.ui.tableWidget.setColumnWidth(4, 150)

            # Populate the table widget with the data
            for row in range(len(result)):
                for column in range(len(result[0])):
                    self.ui.tableWidget.setItem(row, column, QTableWidgetItem(str(result[row][column])))
            self.conexion.disconnect()
        except Exception as e:
            print(f'Error: {e}')

        
    def limpiarCampos(self):
        self.ui.ApellidoMaterno_text.clear()
        self.ui.ApellidoPaterno_text.clear()
        self.ui.nombre_text.clear()
        self.ui.numero_text.clear()
        self.ui.telefono_text.clear()
        self.cargarCategoria(self.conexion)
        self.cargarGeneros(self.conexion)
        self.cargarEquipos(self.conexion)
    
if __name__ == "__main__":  
    app = QApplication(sys.argv)
    generos = Jugador()
    generos.show()
    sys.exit(app.exec())