# Implement a producer-consumer problem with a limited buffer of size 5. Create two
# producer threads and two consumer threads. Producers produce items, and consumers
# consume them. Ensure proper synchronization to avoid buffer overflows or underflows.

import threading
import time
import random

buffer = []
BUFFER_SIZE = 5

empty = threading.Semaphore(BUFFER_SIZE) 
full = threading.Semaphore(0)              
mutex = threading.Lock()                   


def producer(pid):
    for i in range(5):
        item = random.randint(1, 100)
        empty.acquire()          
        mutex.acquire()         

        buffer.append(item)
        print(f"Producer {pid} produced {item} | Buffer: {buffer}")

        mutex.release()
        full.release()           
        time.sleep(1)


def consumer(cid):
    for i in range(5):
        full.acquire()           
        mutex.acquire()         

        item = buffer.pop(0)
        print(f"Consumer {cid} consumed {item} | Buffer: {buffer}")

        mutex.release()
        empty.release()          
        time.sleep(1)

p1 = threading.Thread(target=producer, args=(1,))
p2 = threading.Thread(target=producer, args=(2,))

c1 = threading.Thread(target=consumer, args=(1,))
c2 = threading.Thread(target=consumer, args=(2,))

p1.start()
p2.start()
c1.start()
c2.start()

p1.join()
p2.join()
c1.join()
c2.join()
