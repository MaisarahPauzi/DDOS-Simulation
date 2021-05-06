import threading
import datetime

def do_something(process_number):
    current = datetime.datetime.now().time()
    print(f"Running Process {process_number} at {current}")

thread = []

for i in range(20):
    process = threading.Thread(target=do_something, args=[i])
    process.start()
    thread.append(process)

for process in thread:
    process.join()