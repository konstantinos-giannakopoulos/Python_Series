import threading
import time

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print("{}: Trying access...".format(thread_number))
    semaphore.acquire()
    print("{}: Access granted!...".format(thread_number))
    print("{}: Waiting 5 seconds...".format(thread_number))
    time.sleep(5)
    semaphore.release()
    print("{}: Releasing!".format(thread_number))

for thread_number in range(10):
    t = threading.Thread(target=access,args=(thread_number,))
    t.start()
