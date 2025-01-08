import socket

# Crear un socket
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
cliente_socket.connect(('localhost', 12345))  # Conectarse a localhost y puerto 12345

# Recibir el mensaje del servidor
mensaje = cliente_socket.recv(1024).decode()  # Recibir hasta 1024 bytes
print("Mensaje recibido:", mensaje)

# Cerrar la conexión
cliente_socket.close()
