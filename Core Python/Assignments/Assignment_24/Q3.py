# Implement two threads to print lowercase and uppercase alphabets concurrently from
# 'a' to 'z' and 'A' to 'Z'.

import threading
import time

def print_lowercase():
    for ch in range(ord('a'), ord('z') + 1):
        print(chr(ch), end=" ")
        time.sleep(0.1)

def print_uppercase():
    for ch in range(ord('A'), ord('Z') + 1):
        print(chr(ch), end=" ")
        time.sleep(0.1)

t1 = threading.Thread(target=print_lowercase)
t2 = threading.Thread(target=print_uppercase)

t1.start()
t2.start()

t1.join()
t2.join()
