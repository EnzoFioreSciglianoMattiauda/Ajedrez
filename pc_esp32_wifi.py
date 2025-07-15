import socket 

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
op = 0
while op != 2:
    if op == 1:
        print("""lista de comandos:
        1- "led on"
        2- "led off"
        3- "intensidad x""")
        mensaje = input("ingrese el comando: ")
        udp.sendto(mensaje.encode(), ("192.168.5.106", 1234))
    
    print("""Menu:
1- ingresar comando
2- salir
""")
    
    op = int(input("Ingrese una opcion: "))
