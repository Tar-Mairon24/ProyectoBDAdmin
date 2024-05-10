import sys
import app.Connection as Connection
from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QMessageBox
from gui.ui_estados import Ui_States

class Estados(QWidget):
    def __init__(self, parent=None):
        super(Estados,self).__init__(parent)
        self.ui = Ui_States()
        self.ui.setupUi(self)
        try:
            self.conexion = Connection.Connection()
        except Exception as e:
            print(f'error: {e}')
        self.ui.botonGuardar.clicked.connect(self.guardar)
        self.generarTabla(self.conexion)
        self.cargarComboBox(self.conexion)
        self.ui.botonBorrar.clicked.connect(self.borrar)
        self.ui.comboBox.currentIndexChanged.connect(self.seleccionarComboBox)
        self.ui.tableWidget.cellClicked.connect(self.seleccionarFila)
        self.ui.LimpiarCampos.clicked.connect(self.actualizarCampos)
    
    def guardar(self):
        estado = self.ui.estodo_text.text()
        if estado == '':
            QMessageBox.warning(self, "Error", "Campo vacio")
        elif len(estado) > 45:
            QMessageBox.warning(self, "Error", "El Estado tiene muchos caracteres")
        elif estado.isnumeric():
            QMessageBox.warning(self, "Error", "El Estado no puede ser un numero")
        elif self.existeGenero(self.conexion, estado):
            QMessageBox.warning(self, "Error", "El Estado ya existe")
        elif self.ui.id_label.text() == 'Id:':
            self.insertar(self.conexion, estado)
            self.actualizarCampos()
        else:
            self.update(self.conexion, estado, self.ui.id_label.text())
            self.actualizarCampos()
  
    def insertar(self, conexion, genero):
        try:
            conexion.connect()
            sql = f'SELECT id_estados FROM Estados ORDER BY id_estados DESC LIMIT 1'
            result = conexion.select(sql)
            if(len(result) > 0):
                id = int(result[0][0]) + 1
            else:
                id = 1
            sql = f"INSERT INTO Estados VALUES({id}, '{genero}')"
            conexion.insertar(sql)
            conexion.commit()
            
        except Exception as e:
            print(f"Error: {e}") 
            conexion.rollback()
    
    def borrar(self):
        if self.ui.genero_text.text() == '' or self.ui.id_label.text() == 'Id:':
            QMessageBox.warning(self, "Error", "No hay elemento a borrar")
        elif self.checarHijos(self.conexion, self.ui.id_label.text()):
            QMessageBox.warning(self, "Error", "No se puede borrar mientras se este utilizando")
        else:
            self.delete(self.conexion, self.ui.genero_text.text(), self.ui.id_label.text())
            self.actualizarCampos()

    def delete(self, conexion, genero, id):
        try:
            conexion.connect()
            sql = f"DELETE FROM Genero WHERE Genero = '{self.ui.genero_text.text()}' and id_genero = {self.ui.id_label.text()}"
            conexion.delete(sql)
            conexion.commit()
        except Exception as e:
            print(f"Error: {e}")
            conexion.rollback()
    
    def update(self, conexion, genero, id):
        try:
            conexion.connect()
            sql = f"UPDATE Genero SET Genero = '{genero}' WHERE id_genero = {id}"
            conexion.update(sql)
            conexion.commit()
            conexion.disconnect()
        except Exception as e:
            print(f"Error: {e}")
            conexion.rollback()

    def existeGenero(self, conexion, genero):
        try:
            conexion.connect()
            sql = f"SELECT * FROM Genero WHERE Genero = '{genero}'"
            result = conexion.select(sql)
            conexion.disconnect()
            for row in result:
                if row[1].lower() == genero.lower():
                    return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")

    def checarHijos(self, conexion, id):
        try:
            conexion.connect()
            sql = f"SELECT * FROM Arbitro WHERE Genero_id_genero = {id}"
            resultArbitro = conexion.select(sql)
            sql = f"SELECT * FROM Entrenador WHERE Genero_id_genero = {id}"
            resultEntrenador = conexion.select(sql)
            sql = f"SELECT * FROM Jugador WHERE id_genero = {id}"
            resultJugador = conexion.select(sql)
            conexion.disconnect()
            if len(resultArbitro) > 0 or len(resultEntrenador) > 0 or len(resultJugador) > 0:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            
    def seleccionarComboBox(self):
        try:
            if self.ui.comboBox.currentIndex() == 0:
                self.ui.genero_text.clear()
                self.ui.id_label.setText('Id:')
            else:
                genero_id, genero_nombre = self.ui.comboBox.currentText().split(', ')
                self.ui.genero_text.setText(genero_nombre)
                self.ui.id_label.setText(genero_id)
        except Exception as e:
            print(f"Error: {e}")
    
    def seleccionarFila(self, row):
        try:
            genero_id = self.ui.tableWidget.item(row, 0).text()
            genero_nombre = self.ui.tableWidget.item(row, 1).text()
            self.ui.genero_text.setText(genero_nombre)
            self.ui.id_label.setText(genero_id)
        except Exception as e:
            print(f"Error: {e}")
   
    def cargarComboBox(self, conexion):
        try:
            # Perform the select query using self.conexion
            conexion.connect()
            sql = "SELECT * FROM Genero"
            result = self.conexion.select(sql)
            # Clear the combobox
            self.ui.comboBox.clear()
            # Populate the combobox with the data
            self.ui.comboBox.addItem('Seleccionar')
            for row in result:
                nombre = row[1]
                id = row[0]
                self.ui.comboBox.addItem(f'{id}, {nombre}')
            conexion.disconnect()
        except Exception as e:
            print(f"Error: {e}")

    def generarTabla(self,conexion):
        try:
            # Perform the select query using self.conexion
            conexion.connect()
            sql = f'SELECT * from Genero'
            result = self.conexion.select(sql)

            # Clear the table widget
            self.ui.tableWidget.clear()

            # Set the number of rows and columns in the table widget
            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(len(result[0]))
            self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'Genero'])
            self.ui.tableWidget.setColumnWidth(1, 100)
            self.ui.tableWidget.setColumnWidth(1, 200)

            # Populate the table widget with the data
            for i, row in enumerate(result):
                for j, colunm in enumerate(row):
                    self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(colunm)))
            conexion.disconnect()

        except Exception as e:
            print(f'Error: {e}')

    def actualizarCampos(self):
        self.generarTabla(self.conexion)
        self.cargarComboBox(self.conexion)
        self.ui.genero_text.clear()
        self.ui.id_label.setText('Id:')

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    generos = Estados()
    generos.show()
    sys.exit(app.exec())
