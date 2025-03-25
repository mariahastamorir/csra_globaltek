#importar libreria previamente instalada desde la terminal
import psycopg2

#Establecer datos de la conexion

dbname= 'proyecto_csra_globaltek'
user= 'postgres'
password= '19961994'
host= 'localhost'  #la dirección IP de postgres
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
    cursor.execute('SELECT * FROM tipodocumento')
    
    #obtener resultado (en este caso son listas)
    records =cursor.fetchall()
    print(f"Conectado a la base de datos. Total registros: {len(records)}")
    
    #imprimir iterando la consulta y guardando las filas - rows
    for fila in records:
        print(fila)


    #-----cerrar el cursor y la conexion
    cursor.close()
    
    
except Exception as error:
    print(f"Error al conectar a la base de datos: {error}")
        
        
finally:
    #------cerrar conexion con validación si existio la conexion
    if connection is not None:
        connection.close()
        print('Conexion cerrada')