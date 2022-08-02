import threading
import queue
import math

priorityQueue = queue.PriorityQueue()

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

#lifoQueue.join()

#for i in range(5):
#    lifoQueue.put(None)

priorityQueue.put((8, "Some string"))
priorityQueue.put((1, 2023))
priorityQueue.put((90, True))
priorityQueue.put((2, 10.23))

while not priorityQueue.empty():
    print(priorityQueue.get())
