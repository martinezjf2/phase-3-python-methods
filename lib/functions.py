#!/usr/bin/env python

def greet_programmer():
   print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if isinstance(number, int) or isinstance(number, float):
        return number / 2
    else:
        return None
