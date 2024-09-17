# range(1,5,2)

def f1():
    for i in range(1,10,2):
        print(i)
# 2 means step to next index value and print based on steps
# if there is 3 then 0,1,2 

# f1()


def f2():
    for i in range(10,1,-2):
        print(i)

# f2()


def f3():
    count = 0
    while count < 5:
        print(count)
        count = count+1

# f3()

def f4():
    for i in range(10):
        if(i==7):
            break
# if condition is true it will exit out of the loop permanently
# break is a statment
        print(i)

# f4()

def f5():
    for i in range(10):
        if(i%2==0):
            continue
#this continue statement means skip the current iteration if condition is true
        print(i)

# f5()

def f6():
    for i in range(10):
        if(i==3):
            pass
#the pass statement perform null operation; it does nothing 
        print(i)

# f6()

'''
nested loop concept
'''

def f7():
    for i in range(4): # outer loop; 
        for j in range(3): # inner loop 
            print(f"i:{i}and j:{j}")
# outer loop execute one iteration then goes to inner loop
# inner loop will iterate all iteration then come out to outer loop this process will goes on 
# f7()

# example calculate the sum of first N nutural numbers using while loop and for loop

def f8():
    count = 0
    sum = 0
    while count<2:
        count = count+1
        sum = sum+count
        print("count",count)
              
    print(sum)

# f8()

def f9():
    sum =0
    for i in range(11):
        sum=sum+i
    print(sum)

# f9()

## Example- Prime numbers between 1 and 100

def f10():
    for num in range(1,101):
        if(num>1):
            for i in range(2,num):
                if(num%2==0):
                    break
            else:
                print(num)

#f10()