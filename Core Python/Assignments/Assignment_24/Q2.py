# #Create two threads, one printing even numbers and the other printing odd numbers
# from 1 to 10. Ensure proper synchronization to alternate between even and odd
# numbers.


import threading

condition = threading.Condition()
current = 1  

def print_odd():
    global current
    with condition:
        while current <= 10:
            if current % 2 == 1:
                print("Odd:", current)
                current += 1
                condition.notify()
            else:
                condition.wait()

def print_even():
    global current
    with condition:
        while current <= 10:
            if current % 2 == 0:
                print("Even:", current)
                current += 1
                condition.notify()
            else:
                condition.wait()

t1 = threading.Thread(target=print_odd)
t2 = threading.Thread(target=print_even)

t1.start()
t2.start()

t1.join()
t2.join()
