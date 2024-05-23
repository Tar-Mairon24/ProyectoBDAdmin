import json
import mysql.connector

class Connection:
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def connect(self):
        try:
            with open('credentials.json', 'r') as file:
                credentials = json.load(file)

            self.conexion = mysql.connector.connect(
                host=credentials['host'],
                user=credentials['user'],
                password=credentials['password'],
                database=credentials['database']
            )
            self.cursor = self.conexion.cursor()
        except Exception as e:
            error = str(e)
            print(f'Error: {error}')

    def disconnect(self):
        if self.conexion is not None:
            self.cursor.close()
            self.conexion.close()
        else:
            print('No exiten una conexión activa')

    def getCursor(self):
        return self.cursor

    def select(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def insertar(self, sql):
        self.cursor.execute(sql)
        print("Valores insertados")
    
    def delete(self, sql):
        self.cursor.execute(sql)
        print("Valores eliminados")

    def update(self, sql):
        self.cursor.execute(sql)
        print("Valores actualizados")
    
    def commit(self):
        self.conexion.commit()
        print("Commit realizado")
    
    def rollback(self):
        self.conexion.rollback()
        print("Se relizo un rollback")

    def leerCredenciales(self):
        with open('credenciales.txt', 'r') as archivo:
            credenciales = archivo.readlines()
            credenciales = [x.strip() for x in credenciales]
        return credenciales

