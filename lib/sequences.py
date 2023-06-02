#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    fibonacci_sequence = [] #creates empty list 
    if length > 0: # checks if the value of the variable length is greater than 0. A condition that needs to evaluate to True for the subsequent code to execute
        fibonacci_sequence.append(0) #conditional statement that appends the number 0 to list
        if length > 1:
            fibonacci_sequence.append(1)
            if length > 2:
                for i in range(2, length): #for loop that iterates over a range of numbers starting from 2 up to length
                    fibonacci_sequence.append( # inside the loop, it calculates the Fibonacci numbers and appends them to the fibonacci_sequence list.
                        fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]) #The Fibonacci sequence is generated by adding the two previous numbers in the sequence
                    #fibonacci_sequence[i - 1] represents the previous Fibonacci number.
                    #fibonacci_sequence[i - 2] represents the Fibonacci number before the previous one.
                    #
    print(fibonacci_sequence)