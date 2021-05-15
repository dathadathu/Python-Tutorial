from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)


t = Hello()
t2 = Hi()

t.start()
sleep(0.2)
t2.start()

t.join()
t2.join()

print("Bye")