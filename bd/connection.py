import pymysql 

myConnection = pymysql.connect(host='localhost',user = 'root', passwd = 'Daniarely3', db= 'ventas')

cur = myConnection.cursor()

cur.execute("select nombre, direccion from cliente") # metodo execute permite realizar consultas 

for nombre, direccion in cur.fetchall():
    print(nombre," | ",direccion)
    
myConnection.close()