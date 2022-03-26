import socket
import sys
import fnmatch

host = '129.151.100.51' # dirección IP del Servidor
puerto = 8080 # Puerto de conexión
mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # se crea el objeto Socket de tipo internet(AD_INET) y protocolo tcp/ip(SOCK_STREAM)
mi_socket.bind((host, puerto )) # establecer la conexion y pasamos los datos de conexión
mi_socket.listen() # Se coloca a escucha de los clientes
print(f"Servidor {host}:{puerto} esperando conexion...")

while True:
    conexion, direccion = mi_socket.accept() # Acepta la conexión entrante del nuevo cliente
    try:
        print(f"Conexión establecida con: {direccion}") # Se identifica al cliente que se conecta con el servidor
        while True:
            mensaje = conexion.recv(1024) # Acepta los datos del socket y devuelve una cadena con un tamaño maximo de bufsize de 1024
            opcion = mensaje.decode('utf-8') # decodifica el mensaje enviado desde el cliente
            if opcion == "1":
                conexion.send("---CONSIGNAR A CUENTA---\n".encode('utf-8')) # envia mensaje al cliente
                archivo = open("datos.txt","a")  # Abre archivo para guardar información
                print(" Consignando ... ")
                cuenta = conexion.recv(1024) # Acepta los datos del socket y devuelve una cadena con un tamaño maximo de bufsize de 1024
                account = cuenta.decode('utf-8') # recibe cuenta y monto del cliente
                print("cuenta y monto: "+ account)# imprime en servidor cuenta y monto
                archivo.write(account + '\n') # guarda en archivo
                conexion.send(" OK \n".encode('utf-8')) # envia mensaje de confirmación al cliente
                archivo.close() # cierra el archivo

            elif opcion == "2":
                conexion.send("---CONSULTAR CUENTA---\n".encode('utf-8')) # Envia mensaje al cliente
                print(" Consultado... ")
                buscar = conexion.recv(1024) # Acepta los datos del socket y devuelve una cadena con un tamaño maximo de bufsize de 1024
                ctabuscar = buscar.decode('utf-8') # recibe número de cuenta del cliente
                ctabuscar1 = ("*"+ctabuscar+"*") # convierte a formato para busqueda en fnmatch
                print("cuenta a buscar: "+ctabuscar)
                with open("datos.txt", "r") as datos: # abre el archivo para consulta
                    cuentas = datos.read().split('\n') # pasa toda la información del txt a una lista
                master = fnmatch.filter(cuentas, ctabuscar1) # busca la cuenta dentro de la lista
                strmaster = str(master).strip("['']") # convierte a string
                posicion = cuentas.index(strmaster) # ubica la posición de la cuenta en la lista
                saldo = cuentas[posicion] # guarda el valor de la posicion en la lista
                conexion.send(saldo.encode('utf-8')) #Envia sel saldo al cliente

            elif opcion == "3":
                conexion.send("---SALIR---\n".encode('utf-8')) # Envia mensaje al cliente
                print(mensaje.decode('utf-8') + " Conexion cerrada: ")
                break

    finally:
        conexion.close() # Cierra conexion con el cliente
