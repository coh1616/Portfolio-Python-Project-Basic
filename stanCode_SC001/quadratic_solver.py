"""
File: quadratic_solver.py
Name: Yunchuan Kao
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This program calculates the roots of equation(ax^2+bx+c) by entering a, b, and c
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	discriminant = (b ** 2) - (4 * a * c)
	if a != 0:
		if discriminant == 0:
			x = -b / (2 * a)
			print('One root: ' + str(x))
		elif discriminant > 0:
			x1 = (-b + math.sqrt(discriminant)) / (2 * a)
			x2 = (-b - math.sqrt(discriminant)) / (2 * a)
			print('Two root: ' + str(x1) + ', ' + str(x2))
		else:
			print('No real roots')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
