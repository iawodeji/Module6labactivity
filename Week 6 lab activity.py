#Idris Awodeji
#8.6.2024


#Problem 1
#imports the random module 
import random

#loops 10 times to generate and print 10 random integers
for _ in range(10):
    #prints generated random numbers
    print(random.randrange(25, 36))



#Problem 2
#generates random odd integer between 1 and 100
random_odd_number = random.randrange(1, 100, 2)

#prints generated random odd number
print(random_odd_number)



#Problem 3
#lists days of the week
days_of_week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#uses random.choice to select a random day from the list
random_day = random.choice(days_of_week)

#prints selected random day
print(random_day)



#Problem 4
import math
#approximates pi using the arctangent function
approx_pi = 4 * math.atan(1)

#prints the approximated value and the actual value of pi
print(f"approximated value of pi: {approx_pi}")
print(f"actual value of pi: {math.pi}")



#Problem 5
#user inputs value
user_input = float(input("Enter a number: "))

#computes logarithm and convert to degrees
log_value = math.log10(user_input)
degrees_value = math.degrees(log_value)

#prints the results
print(f"Logarithm (base 10) of {user_input}: {log_value}")
print(f"Converted to degrees: {degrees_value}")



#Problem 6
#user inputs value
n = int(input("Enter a number: "))

#calculates factorial using a for loop
factorial_for_loop = 1
for i in range(1, n + 1):
    factorial_for_loop *= i

#calculates factorial using math.factorial
factorial_math = math.factorial(n)

#prints factorial using for loop and factorial using math.factorial
print(f"Factorial (for loop): {factorial_for_loop}")
print(f"Factorial (math.factorial): {factorial_math}")

