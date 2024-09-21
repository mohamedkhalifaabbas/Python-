import threading 
import time 


def eat_breakfast(): 
    time.sleep(3)
    print("you eat breakfast ")

def drink_coffee(): 
    time.sleep(4)
    print("you drink coffee ")

def study(): 
    time.sleep(6)
    print("study ")        



y = threading.Thread(target=drink_coffee , args=())
y.start()

x = threading.Thread(target=eat_breakfast , args=())
x.start()



z = threading.Thread(target=study , args=())
z.start()


# Thread synchronization
x.join()
y.join()
z.join()

print(threading.active_count())

print(time.perf_counter())



