# Even or Odd: Write a program that takes an integer 
# input from the user and checks if it's even or odd 
# using an if statement.

x = float(input("please enter an number: "))
if(x%2==0):
   print("even")
else:
    print("odd")

# Positive, Negative, or Zero: Ask the user to input a number, then use an if statement to determine if the number is positive, negative, or zero.


x = float(input("please enter an number: "))
if(x>0):
    print("positive")
elif(x==0):
    print("zero")
elif(x<0):
    print("negative")



# Vowel or Consonant: Take a single character as input and check if it is a vowel (a, e, i, o, u) or a consonant using an if statement.
x = input("please enter an character: ")
if(x=='a'or x=='e'or x=='i' or x=='o'or x=='u'):
    print("vowel",x)
else:
    print("consonant",x)

# Leap Year Checker: Write a program that checks if a given year is a leap year using an if statement (hint: A leap year is divisible by 4, but if divisible by 100, it should also be divisible by 400).
x = float(input("Please enter a year: "))
#
# Check if the year is a leap year
if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
    print("leap year", x)
else:
    print("not a leap year", x)
