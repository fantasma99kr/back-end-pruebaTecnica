#  Conexion a la base de datos
import pyodbc

def db_con():
    # Datos para la conexion
    try:
        connection_string = (
            "DRIVER={ODBC Driver 17 for SQL Server};"#tipo de conexion con sqlServer
            "SERVER=IRON\\IRON;"#este es el servidor localhost o 127.0.0.1 en mi caso es diferente por eso se llama IRON
            "DATABASE=aeropuerto;"#nombre de la base de datos
            "UID=sa;"#usuario
            "PWD=redriot9474"#constraseña
        )
        #Regresa la conexion a la base de datos
        return pyodbc.connect(connection_string)
    #Control de las excepciones si es que no se puede conectar
    except Exception as e:
        #Esto se puede colocar en un log para poder consultar de forma mas facil
        #que esta pasando mal
        print(f"Error en conexion a la base de datos {str(e)}")
        return None
    