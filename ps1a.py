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

epsilon = 0.01
k = 54321
guess = k/2.0
num_guesses = 0

while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    num_guesses += 1

print(f"the square root of {k} is {guess} after {num_guesses} guesses")