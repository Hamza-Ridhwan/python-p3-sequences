#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
       print([])
    elif length == 1:
       print([0])
    else:
        my_two_numbers = [0,1]
        for _ in range(2, length):
         my_two_numbers.append(my_two_numbers[-1] + my_two_numbers[-2])
        
        print(my_two_numbers)

print_fibonacci(9)