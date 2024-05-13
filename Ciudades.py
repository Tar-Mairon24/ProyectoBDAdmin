import sys, re
import app.Connection as Connection
from PySide6.QtWidgets import QWidget, QApplication, QTableWidgetItem, QMessageBox
from gui.ui_ciudad import Ui_Ciudad

class Estados(QWidget):
    def __init__(self, parent=None):
        super(Estados,self).__init__(parent)
        self.ui = Ui_Ciudad()
        self.ui.setupUi(self)
        try:
            self.conexion = Connection.Connection()
        except Exception as e:
            print(f'error: {e}')
        self.ui.botonGuardar.clicked.connect(self.guardar)
        self.generarTabla(self.conexion)
        self.cargarComboBox(self.conexion)
        self.cargarEstados(self.conexion)
        self.ui.botonBorrar.clicked.connect(self.borrar)
        self.ui.comboBox.currentIndexChanged.connect(self.seleccionarComboBox)
        self.ui.tableWidget.cellClicked.connect(self.seleccionarFila)
        self.ui.LimpiarCampos.clicked.connect(self.actualizarCampos)
    
    def guardar(self):
        ciudad = self.ui.ciudad_text.text()
        estado = self.seleccionarEstado(self.conexion)
        if ciudad == '':
            QMessageBox.warning(self, "Error", "Campo vacio")
        elif len(ciudad) > 45:
            QMessageBox.warning(self, "Error", "La Ciudad tiene muchos caracteres")
        elif ciudad.isnumeric():
            QMessageBox.warning(self, "Error", "La Ciudad no puede ser un numero")
        elif not re.match("^[a-zA-Z]*$", ciudad):
            QMessageBox.warning(self, "Error", "La Ciudad debe contener solo letras")
        elif self.existeEstado(self.conexion, ciudad, estado):
            QMessageBox.warning(self, "Error", "La Ciudad ya existe")
        elif estado == -1:
            QMessageBox.warning(self, "Error", "Selecciona un Estado")
        elif self.ui.id_label.text() == 'Id:':
            self.insertar(self.conexion, ciudad, estado)
            self.actualizarCampos()
        else:
            self.update(self.conexion, ciudad, self.ui.id_label.text(), estado)
            self.actualizarCampos()
  
    def insertar(self, conexion, ciudad, estado):
        try:
            conexion.connect()
            sql = f'SELECT id_ciudad FROM Ciudad ORDER BY id_ciudad DESC LIMIT 1'
            result = conexion.select(sql)
            if(len(result) > 0):
                id = int(result[0][0]) + 1
            else:
                id = 1
            sql = f"INSERT INTO Ciudad VALUES({id}, '{ciudad}', '{estado}')"
            conexion.insertar(sql)
            conexion.commit()
            
        except Exception as e:
            print(f"Error: {e}") 
            conexion.rollback()
    
    def borrar(self):
        if self.ui.ciudad_text.text() == '' or self.ui.id_label.text() == 'Id:':
            QMessageBox.warning(self, "Error", "No hay elemento a borrar")
        elif self.checarHijos(self.conexion, self.ui.id_label.text()):
            QMessageBox.warning(self, "Error", "No se puede borrar mientras se este utilizando")
        else:
            self.delete(self.conexion, self.ui.ciudad_text.text(), self.ui.id_label.text())
            self.actualizarCampos()

    def delete(self, conexion, ciudad, id):
        try:
            conexion.connect()
            sql = f"DELETE FROM Ciudad WHERE Nombre = '{ciudad}' and id_ciudad = {id}"
            conexion.delete(sql)
            conexion.commit()
        except Exception as e:
            print(f"Error: {e}")
            conexion.rollback()
    
    def update(self, conexion, ciudad, id, estado):
        print(estado)
        try:
            conexion.connect()
            if(estado == ' '):
                sql = f"UPDATE Ciudad SET Nombre = '{ciudad}' WHERE id_ciudad = {id}"
            else:
                sql = f"UPDATE Ciudad SET Nombre = '{ciudad}', id_estados = '{estado}' WHERE id_ciudad = {id}"
            conexion.update(sql)
            conexion.commit()
            conexion.disconnect()
        except Exception as e:
            print(f"Error: {e}")
            conexion.rollback()

    def existeEstado(self, conexion, ciudad, estado):
        try:
            conexion.connect()
            sql = f"SELECT * FROM Ciudad WHERE Nombre = '{ciudad}' and id_estados = '{estado}'"
            result = conexion.select(sql)
            conexion.disconnect()
            for row in result:
                if row[1].lower() == ciudad.lower():
                    return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")

    def checarHijos(self, conexion, id):
        try:
            conexion.connect()
            sql = f"SELECT * FROM Colonia WHERE id_ciudad = {id}"
            resultColonia = conexion.select(sql)
    
            conexion.disconnect()
            if len(resultColonia) > 0:
                return True
            else:
                return False
        except Exception as e:
            print(f"Error: {e}")
            
    def seleccionarComboBox(self):
        try:
            if self.ui.comboBox.currentIndex() == 0:
                self.ui.ciudad_text.clear()
                self.ui.id_label.setText('Id:')
            else:
                id_ciudad, ciudad_nombre, ciudad_estado = self.ui.comboBox.currentText().split(', ')
                # Find the index of the text in the comboBox
                index = self.ui.combo_estados.findText(ciudad_estado)
                # If the text is found, select it
                if index >= 0:
                    self.ui.combo_estados.setCurrentIndex(index)
                self.ui.ciudad_text.setText(ciudad_nombre)
                self.ui.id_label.setText(id_ciudad)
                
        except Exception as e:
            print(f"Error: {e}")

    def seleccionarEstado(self, conexion):
        try:
            estado = self.ui.combo_estados.currentText()
            conexion.connect()
            sql = f"SELECT id_estados FROM Estados WHERE Nombre = '{estado}'"
            result = conexion.select(sql)
            conexion.disconnect()
            if len(result) > 0:
                return result[0][0]
            else:
                return -1
        except Exception as e:
            print(f"Error: {e}")

    def cargarEstados(self, conexion):
        try:
            # Perform the select query using self.conexion
            conexion.connect()
            sql = "SELECT Nombre FROM Estados order by Nombre asc"
            result = self.conexion.select(sql)
            # Clear the combobox
            self.ui.combo_estados.clear()
            # Populate the combobox with the data
            self.ui.combo_estados.addItem('Seleccionar')
            for row in result:
                nombre = row[0]
                self.ui.combo_estados.addItem(f'{nombre}')
            conexion.disconnect()
        except Exception as e:
            print(f"Error: {e}")
    
    def seleccionarFila(self, row):
        try:
            ciudad_id = self.ui.tableWidget.item(row, 0).text()
            ciudad_nombre = self.ui.tableWidget.item(row, 1).text()
            # Get the text in column 3
            ciudad_estado = self.ui.tableWidget.item(row, 2).text()
            # Find the index of the text in the comboBox
            index = self.ui.combo_estados.findText(ciudad_estado)
            # If the text is found, select it
            if index >= 0:
                self.ui.combo_estados.setCurrentIndex(index)

            self.ui.ciudad_text.setText(ciudad_nombre)
            self.ui.id_label.setText(ciudad_id)
        except Exception as e:
            print(f"Error: {e}")
   
    def cargarComboBox(self, conexion):
        try:
            # Perform the select query using self.conexion
            conexion.connect()
            sql = f'SELECT id_ciudad, Ciudad.Nombre, Estados.Nombre from Ciudad, Estados where Ciudad.id_estados = Estados.id_estados'
            result = self.conexion.select(sql)
            # Clear the combobox
            self.ui.comboBox.clear()
            # Populate the combobox with the data
            self.ui.comboBox.addItem('Seleccionar')
            for row in result:
                nombre = row[1]
                id = row[0]
                estado = row[2]
                self.ui.comboBox.addItem(f'{id}, {nombre}, {estado}')
            conexion.disconnect()
        except Exception as e:
            print(f"Error: {e}")

    def generarTabla(self,conexion):
        try:
            # Perform the select query using self.conexion
            conexion.connect()
            sql = f'SELECT id_ciudad, Ciudad.Nombre, Estados.Nombre from Ciudad, Estados where Ciudad.id_estados = Estados.id_estados'
            result = self.conexion.select(sql)

            # Clear the table widget
            self.ui.tableWidget.clear()

            # Set the number of rows and columns in the table widget
            self.ui.tableWidget.setRowCount(len(result))
            self.ui.tableWidget.setColumnCount(len(result[0]))
            self.ui.tableWidget.setHorizontalHeaderLabels(['ID', 'Ciudad', 'Estado'])
            self.ui.tableWidget.setColumnWidth(0, 100)
            self.ui.tableWidget.setColumnWidth(1, 200)
            self.ui.tableWidget.setColumnWidth(2, 200)

            # Populate the table widget with the data
            for row_idx, row_data in enumerate(result):
                for col_idx, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.ui.tableWidget.setItem(row_idx, col_idx, item)
            conexion.disconnect()

        except Exception as e:
            print(f'Error: {e}')

    def actualizarCampos(self):
        self.generarTabla(self.conexion)
        self.cargarComboBox(self.conexion)
        self.cargarEstados(self.conexion)
        self.ui.ciudad_text.clear()
        self.ui.id_label.setText('Id:')

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    generos = Estados()
    generos.show()
    sys.exit(app.exec())
