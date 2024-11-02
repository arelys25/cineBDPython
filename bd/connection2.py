import mariadb #importar libreria de mariadb

# hacer la coneccion 
cons = mariadb.connect(
    user = 'root', # mi usuario de mariadb
    passwd = 'Daniarely3', # mi contraseña de mariadb
    host = 'HP-LAP-ARELY25', # se obtuvo gracias al comando de mariadb: SHOW VARIABLES LIKE 'hostname'
    port = 3305, # el puerto lo pude identificar en heidi.sql al momento de ingresar 
    db = 'ventas' # nombre de la base de datos 
)

# crearemos un cursor (funcion ya hecha) que nos permitira ejecutar nuestras sentencias sql como en la terminal de maria db
cur = cons.cursor()

sql = 'SELECT * FROM cliente'

# para ejecutar la sentencia usaremos execute 
cur.execute(statement=sql)

res = cur.fetchall() # regresa los resultados 


print(res) # imprimir el resultado

cons.close() # todas las conexiones se deben cerrar para que no se creen nuevas conecciones y podemos saturar la BDD