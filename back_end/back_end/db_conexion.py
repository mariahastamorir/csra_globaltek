#importar libreria previamente instalada desde la terminal
import psycopg2

#Establecer datos de la conexion

dbname= 'proyecto_csra_globaltek'
user= 'postgres'
password= '19961994'
host= ''  #la dirección IP de postgres
port= '5432'

#conexion a la base de datos
try:
    connection = psycopg2.connect(
        dbname= dbname,
        user= user,
        password= password,
        host= host,
        port= port

    )
    
    #crear cursor para ejecutar consultas
    cursor = connection.cursor()
    
    #ejecutar consulta simple
    cursor.execute('select * from tipodocumento')
    
    #obtener resultado
    record =cursor.fetchall()
    print(f"Conectado a la base de datos: {record}")

    #cerrar el curso y la conexion
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error al conectar a la base de datos: {KeyError}")
        
        
