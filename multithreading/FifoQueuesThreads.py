import threading
import queue
import math

fifoQueue = queue.Queue()
threads = []

def worker():
    while True:
        item = fifoQueue.get()
        if item is None:
            break
        print(math.factorial(item))
        fifoQueue.task_done()

for x in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

zahlen = [2, 5, 3] #[134000, 14, 5, 300, 98, 88, 11, 23]

for item in zahlen:
    fifoQueue.put(item)

fifoQueue.join()

for i in range(5):
    fifoQueue.put(None)
