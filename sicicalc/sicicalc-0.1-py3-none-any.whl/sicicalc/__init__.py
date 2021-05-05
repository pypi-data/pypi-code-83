"""
Created by Snehashish Laskar
Email : snehashish.laskar@gmail.com
Created on 08-03-2021
This a very Basic Simple Intrest  and Compound intrest calculator
This is a very simple project to try
"""
import webbrowser

def SimpleIntrest(principle, time, rate):

	intrest = (int(principle)*int(rate)*time)/100

	amount = int(principle)+intrest

	print(f"money will amount to {amount} and the intrest is {intrest}")


def CompoundIntrest(principle, time, rate):
	amount = principal*((1 + rate)**time)

	intrest = amount - principal

	print(f" You'r money will amount to {amount} and the intrest you are paying is {intrest}")
