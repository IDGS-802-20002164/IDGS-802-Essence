from db import get_connection

class insertCliente:
    def insertM(nombre,ape_paterno,ape_materno,telefono,email,password):
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call insertar_cliente(%s,%s,%s,%s,%s,%s)',(nombre,ape_paterno,ape_materno,telefono,email,password))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)

class insertEmpleado:
    def insertM(nombre,ape_paterno,ape_materno,telefono,email,password):
        try:
            connection  = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call insertar_empleado(%s,%s,%s,%s,%s,%s)',(nombre,ape_paterno,ape_materno,telefono,email,password))
            connection.commit()
            connection.close()
        except Exception as ex:
            print(ex)

