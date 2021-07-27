#print all even number from 100
for i in range ( 1 , 100 , 2 ):
    print(i)

#print all odd number from 100
for i in range ( 1 , 100 , 2 ):
    print(i)

#print all even and odd numbers together from 101
even = []
odd = []
for i in range ( 1 , 101):
    if i % 2 == 0: 
        even.append(i)
    else:
        odd.append(i)
print ( " Even Numbers: ", even)
print ( " Odd Numbers: " , odd)

#print all even and odd numbers together from 101
for i in range (1 , 100):
    if i % 2 == 0:
        print("even number: ", i)
    else:
        print("odd number:" , i)

#print sum of all even number from 101
sum = 0
for i in range ( 2 , 101 ):
    if i % 2 == 0:
        sum = sum + i
print(sum)

#print sum of all odd number from 101
sum = 0
for i in range ( 1 , 101 ):
    if i % 2 != 0:
        sum = sum + i
print(sum)

#print sum of all even number and odd number together from 101
sum1 = 0
sum2 = 0
for i in range ( 1 , 101 ):
    if i % 2 == 0:
        sum1 = sum1 + i
    else:
        sum2 = sum2 + i
print ( " sum of even no" , sum1)
print ( " sum of odd no" , sum2)

#calculate the square of each number of list
numbers =[1,2,3,4,5]
for i in numbers:
    square = i ** 2
    # print("The square root is :" , square)
    print("square root:", i , "is" , square)
#another way
numbers = [1,2,3,4,5]
square_numbers=[]
for i in numbers:
    square_numbers.append(i ** 2)
print("square of:",numbers,"is", square_numbers)

#calculate the average of list of number 
numbers = [10,20,30,40,50]
sum = sum(numbers)
for i in numbers:
    avg = sum / 5
print("average of:", numbers , "is" , avg)

#Another way
numbers = [10,20,30,40,50]
sum = sum(numbers)
len = len(numbers)
for i in numbers:
    avg = sum / len
print("average of:", numbers , "is" , avg)