from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    SELECCIONAR_ID = 'SELECT * FROM cliente WHERE id = %s'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            #mapeo de clase-table-cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1],
                                  registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar el cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar_por_id(cls, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id,)
            cursor.execute(cls.SELECCIONAR_ID, valores)
            registro = cursor.fetchone()
            # mapeo de clase-table-cliente
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3])

            return cliente

        except Exception as e:
            print(f'Ocurrio un error al seleccionar un cliente por id: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error ao insertar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al elimar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)



if __name__ == '__main__':

    #insertar cliente
    # cliente1 = Cliente(nombre='cau', apellido='pacheco', membresia='400')
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes Insertados: {clientes_insertados}')

    #actualizar cliente
    # cliente_actualizar = Cliente(2, 'Clauberson', 'Pacheco', 500)
    # cliente_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes actualizados = {cliente_actualizados}')

    # cliente_eliminar = Cliente(id=3)
    # cliente_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    # print(f'Clientes eliminados: {cliente_eliminados}')

    #selecionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

