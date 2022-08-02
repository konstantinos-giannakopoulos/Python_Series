import threading
import time

path = "text.txt"
text = ""

def readFile():
    global path, text
    while True:
        with open(path) as file:
            text = file.read()
        time.sleep(3)

def printloop():
    global text
    for x in range(30):
        print("\n", x)
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printloop)

t1.start()
t2.start()
