# 1)write a programme to check the sum of numbers
total=0
for number in range(1,9):
    total=total+number
   # print(number)
print("Sum of number is ",total)

#2) Write a Python program that prints the following pattern:

# markdown
# Copy code
# *
# **
# ***
# ****
# *****
# Number of rows
n = 5

# Outer loop for each row
for i in range(1, n + 1):
    # Create a string with 'i' stars
    row = "*" * i
    # Print the whole string at once
    print(row)
# second solution


#3) write a programme to print character using "hello" using for loop
# this is my solution
name=["h","e","l","l","o"]
for i in name:
    print(i)
# second solution  i learn from chatgpt
text = "hello"
for i in text:
    print(i)


# 4) Sum of Odd Numbers: Write a program that calculates the sum of all odd numbers between 1 and 10 using a for loop.

# this is my solution 
sum=0
for x in range(1,11):
 if(x%2==0):
    print()
 else:
    print()
    sum=sum+x
print(sum)

# second solution i learn from chatgpt

sum =0
for odd in range(1,11):
   if(odd%2!=0):
      sum=sum+odd
print(sum)