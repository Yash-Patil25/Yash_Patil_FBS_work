# #Multithreading.

# Calculate the sum of squares of numbers from 1 to 100 using four threads. Divide the
# range equally among the threads, and each thread calculates the sum of squares for its
# range. Finally, combine the results to get the total sum of squares.

import threading

results = []

def sum_of_squares(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i * i
    results.append(total)

t1 = threading.Thread(target=sum_of_squares, args=(1, 25))
t2 = threading.Thread(target=sum_of_squares, args=(26, 50))
t3 = threading.Thread(target=sum_of_squares, args=(51, 75))
t4 = threading.Thread(target=sum_of_squares, args=(76, 100))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

total_sum = sum(results)

print("Sum of squares from 1 to 100:", total_sum)
