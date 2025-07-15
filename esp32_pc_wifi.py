from machine import Pin, PWM, I2C
import ssd1306
import network
import socket

def mostrar_oled(mensaje):
    oled.fill(0)
    oled.text(mensaje, 0 ,30)
    oled.show()



i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

led = PWM(Pin(4))
led.freq(1000)
ssid = "nashe"
password = "FR223118"

wlan = network.WLAN(network.STA_IF) #defino la conexion en modo estacion
wlan.active(True) #activo la conexion
wlan.connect(ssid, password) #la conecto a la red local (el wifi)

while not wlan.isconnected(): # .isconnected() devuelve True si la conexion ya se establecio
    pass

print(f"IP: {wlan.ifconfig()[0]}") # .ifconfig() devuelve una tupla con (ip, mascara de red, puerta de enlace, dns)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 1234)) #asocia cualquier IP (con el parametro "") al puerto 1234 de la esp32

mostrar_oled("funco")

while True:
    data, addr = s.recvfrom(1024) #data es el mensaje, addr es la ip que lo mando  
    # el parametro 1024 es el tamaño maximo en bytes del mensaje que espera recibir
    msg = data.decode() #paso de b'string' (string en bytes) a string normal
    print(msg)
    
    if "led on" in msg.lower():
        led.duty(1023)
        mostrar_oled(msg)
    elif "led off" in msg.lower():
        led.duty(0)
        mostrar_oled(msg)
    elif "intensidad" in msg.lower():
        datos = msg.strip().split(" ")
        led.duty(int(datos[1]))
        mostrar_oled(msg)
    else:
        mostrar_oled(msg)
        
    