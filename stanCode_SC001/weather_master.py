"""
File: weather_master.py
Name: Yunchuan Kao
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# The constant stands for which number to leave the program
EXIT = -1


def main():
	"""
	This program computes the average, highest, lowest, cold days among user inputs
	"""
	print('stanCode \"Weather Master 4.0"!')
	data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = data
		minimum = data
		# Set a variable to count the frequency user inputted
		input_number = 1
		# Set a variable to compute the sum of temperatures user inputted
		total = data
		average = total / input_number
		# Set a variable to count the temperatures below 16 degrees
		if data < 16:
			cold = 1
		else:
			cold = 0
		while True:
			data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if data == EXIT:
				break
			input_number += 1
			total = total + data
			average = total / input_number
			if data < 16:
				cold += 1
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(cold) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
