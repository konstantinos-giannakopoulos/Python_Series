import threading
import queue
import math

lifoQueue = queue.LifoQueue()

'''
threads = []

def worker():
    while True:
        item = lifoQueue.get()
        if item is None:
            break
        print(item)
        lifoQueue.task_done()

for x in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)
'''

numbers = [1, 2, 3, 4, 5]

for item in numbers:
    lifoQueue.put(item)

#lifoQueue.join()

#for i in range(5):
#    lifoQueue.put(None)

while not lifoQueue.empty():
    print(lifoQueue.get())
