import threading


class MyThread(threading.Thread):
    
    def __init__(self,message):
        threading.Thread.__init__(self)
        self.message = message

    def run(self):
        for x in range(100):
            print(self.message)

mt1 = MyThread("This is my thread message!") 
mt1.start()
