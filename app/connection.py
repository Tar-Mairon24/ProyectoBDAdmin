import mysql.connector

class Connection:
    def __init__(self):
        self.conexion = None
        self.cursor = None

    def connect(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='admin',
                password='admin'
            )
            print(self.conexion)
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

    def select(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

