import socket

host = 'www.google.com'
path = '/search?q=hello'

ip = socket.gethostbyname(host)
port = 80

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket dibuka")

    s.connect((ip, port))
    print("Socket berjaya berhubung dgn host")

    request = f"GET {path} HTTP/1.0\r\n\r\n"
    byt = request.encode()
    s.send(byt)
    print("Data berjaya dihantar")

except socket.error as err:
    print(f"Error: {err}")

finally:
    reply = s.recv(4096)
    print(f"Data dr host ialah: \n {reply}")

    s.shutdown(socket.SHUT_RDWR)
    s.close()
    print("Socket ditutup")