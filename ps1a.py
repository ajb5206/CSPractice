#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 14:28:41 2025

@author: alexanderbertotto
"""

# yearly_salary = float(input("What is your yearly salary? "))
# portion_saved = float(input("What percentage of your salary are you saving?"))
# cost_of_dream_home = float(input("What is the cost of your dream home? "))
# portion_down_payment = .25 * cost_of_dream_home
# amount_saved = 0
# r = 0.05
# months = 0

# 1. If you are incrementing from 0 by 0.022, how many increments 
# can you do before you get a floating point error? 

# x = 0
# count = 20     # check different numbers here
# for i in range(count):
#     x += 0.022 # increment
#     print(x)      # check this value for floating point error


# 2. Automate the code from the previous problem. Suppose you are 
# just given an increment value. Write code that automatically
# determines how many times you can add increment to itself 
# until you start to get a floating point error.

# your code here


# Assume you are given an integer 0 \<= N \\<= 1000. Write a piece of Python code that uses bisection search to guess N.
#  The code prints two lines: count: with how many guesses it took to find N, and answer: with the value of N. Hints: 
#      If the halfway value is exactly in between two integers, choose the smaller one.


#Bisection search
# num_guesses = 0
# N = 994

# upper_bound = 1000
# guess = upper_bound//2
# lower_bound = 0

# while guess != N:
#     if guess > N: #500 > N
#         upper_bound = guess #upper = 750
#         #guess = (upper_bound + lower_bound)//2 # 250
#          #
#     else:
#         lower_bound = guess #500
#         # = int(guess * 1.5)
#        # guess = upper_bound//2
#     num_guesses += 1
#     guess = (upper_bound + lower_bound)//2
#     if num_guesses > 20:
#         break
    
    
# print(f"My guess: {guess}, number: {N}, {num_guesses}")


# num_guesses = 0
# number = 54321
# guess = number/2
# upper_bound = number
# lower_bound = 0
# epsilon = .1



# # while guess**2 != number and guess < number:
# while abs(guess**2 - number) > epsilon and guess < number: 
#     if guess**2 > number:
#         upper_bound = guess
#     else:
#         lower_bound = guess
#     num_guesses += 1
#     guess = (upper_bound + lower_bound)/2
    
#     if num_guesses > 50:
#         break

# print(f"{guess} is my guess for the square root of {number} after {num_guesses} tries")


#guess between 0-1
# num_guesses = 0
# number = 0.5
# upper_bound = 1
# lower_bound = number
# guess = (upper_bound + lower_bound)/2
# epsilon = .01

# while abs(guess**2 - number) >= epsilon:
#     if guess**2 > number:
#         upper_bound = guess
#     else:
#         lower_bound = guess
#     num_guesses += 1
#     guess = (upper_bound + lower_bound)/2
    
#     if num_guesses > 50:
#         break

# print(f"{guess} is my guess for the square root of {number} after {num_guesses} tries")


# find the cube roots using bisection search
# num_guesses = 0
# cube = 27
# epsilon = 0.0000000001
# low = 0
# high = cube
# guess = (high + low)/2

# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 > cube:
#         high = guess
#     else:
#         low = guess
#     guess = (high + low)/2
#     num_guesses += 1
#     print(f"{high}, {low}")

# print(f"the cube root of {cube} is {guess} after {num_guesses} guesses")

# epsilon = 0.01
# k = 54321
# guess = k/2.0
# num_guesses = 0

# while abs(guess*guess - k) >= epsilon:
#     guess = guess - (((guess**2) - k)/(2*guess))
#     num_guesses += 1

# print(f"the square root of {k} is {guess} after {num_guesses} guesses")

# def eval_quadratic(a, b, c, x):
    # """
    # a, b, c: numerical values for the coefficients of a quadratic equation
    # x: numerical value at which to evaluate the quadratic.
    # Returns the value of the quadratic a×x² + b×x + c.
    # """
    # Your code here
    
    # epsilon = .001
    # k = x
    # guess = k/2.0
    # num_guesses = 0
        
    # while abs(guess**2 - k) >= epsilon:
    #     guess = guess - (a(guess**2) + b(guess) + c)/(2(a)(guess) + b)
    #     if num_guesses > 100:
    #         break
    # print(num_guesses)
    
    # value = a*(x**2)
#     return a*(x**2) + b*(x) + c
# # Examples:    
# print(eval_quadratic(1, 1, 1, 1)) # prints 3


# eval_quadratic(1, 1, 1, 1)


# def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
#     """
#     a1, b1, c1: one set of coefficients of a quadratic equation
#     a2, b2, c2: another set of coefficients of a quadratic equation
#     x1, x2: values at which to evaluate the quadratics
#     Evaluates one quadratic with coefficients a1, b1, c1, at x1.
#     Evaluates another quadratic with coefficients a2, b2, c2, at x2.
#     Prints the sum of the two evaluations. Does not return anything.
#     """
#     # Your code here
    
#     quad1 = a1*(x1**2) + b1*(x1) + c1
#     quad2 = a2*(x2**2) + b2*(x2) + c2
#     print(f"{quad1 + quad2}")
# # Examples:    
# two_quadratics(1, 1, 1, 1, 1, 1, 1, 1) # prints 6
# print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)) # prints 6 then None


#Add odd integers between and including a - b
# def add_odds(a,b):
#     total = 0
#     for num in range(a, b+1):
#         total = total + num if num % 2 != 0 else total 
#     return total
# print(add_odds(1,11))

# def is_palindrome(str):
#     """ check if given string is a palindrome """
#     return str == str[::-1]

# print(is_palindrome("2222"))

# def keep_consonants(word):
#     """word is a string of lowercase letters
#         returns a string containing only the consonants
#         in the order they appear"""
#     new_word = ""
#     vowels = "aeiou"
#     for char in word:
#         if char not in vowels:
#             new_word += char
                
#     return new_word
    
# print(keep_consonants("helloe"))

# def first_to_last_diff(s, c):
#     """ s is a string, c is single character string
#         Returns the difference between the index where c first
#         occurs and the index where c last occurs. If c does not 
#         occur in s, returns -1. 
#     """
#     initial_loc = 0
#     last_loc = 0
#     if c not in s:
#         return -1
#  # alternate method put all occurances in a list of indices and subtract the last from the first
#     indices = [i for i, char in enumerate(s) if char == c]
    
#     return indices[len(indices)-1] - indices[0] 
    
    
    
    
    
#     # for index, char in enumerate(s):
#     #     if char == c:
#     #         initial_loc = index
#     #         break
#     # for index, char in enumerate(s[::-1]):
#     #     if char == c:
#     #         last_loc = (len(s) - 1) - index
#     #         break
#     # return last_loc - initial_loc

# print(first_to_last_diff("pants", "t"))
# print(first_to_last_diff('aaaa', 'a'))  # prints 3
# print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
# print(first_to_last_diff('xyz', 'b'))  # prints -1


def bisection_root(number):
    low = 0
    high = number
    ans = (high+low)/2.0
    epsilon = 0.001
    while abs(ans**2 - number) > epsilon:
        if ans**2 > number:
            high = ans
        else:
            low = ans
        ans = (high + low)/2.0
    return ans

def count_nums_with_sqrt_close_to(n, epsilon):
    """ n is an int > 2
        epsilon is a positive number < 1
        returns how many integers have a square root within epsilon of n """

    for num in range(2, n*n*n):
        # print(f"{99**0.5 - 10} nums")
        if abs((bisection_root(num)) - n) <= epsilon:
            print(num)
        
count_nums_with_sqrt_close_to(10, .1)
