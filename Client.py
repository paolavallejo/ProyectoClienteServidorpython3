# Importamos las librerias necesarias
import socket
# Establecemos el tipo de socket/conexion
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5000 # Puerto de comunicacion
# Realizamos la conexion al la IP y puerto
sock.connect(('localhost',port))
# Leemos los datos del servidor
data = sock.recv(4096)
# Cerramos el socket
sock.close()
# Mostramos los datos recibidos
print(data.decode())

# Fuente: https://evilnapsis.com/2019/06/03/ejemplo-basico-de-socket-cliente-y-servidor-con-python/