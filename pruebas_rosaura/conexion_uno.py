
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
    
    

    
    # Solicitar datos del usuario
    idTipodeDocumento = int(input('Ingrese el ID del tipo de documento: '))
    
    # Ejecutar consulta simple con parámetros seguros
    sql = 'SELECT * FROM tipodocumento WHERE id = %s'
    cursor.execute(sql, (idTipodeDocumento,))

    
    #obtener resultado (en este caso son listas)
    records =cursor.fetchone()
    print(f"Conectado a la base de datos. Total registros: {len(records)}")
    print(records)
    


    #-----cerrar el cursor y la conexion
    cursor.close()
    
    
except Exception as error:
    print(f"Error al conectar a la base de datos: {error}")
        
        
finally:
    #------cerrar conexion con validación si existio la conexion
    if connection is not None:
        connection.close()
        print('Conexion cerrada')