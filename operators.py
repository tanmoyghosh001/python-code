# Addition operator +
x = 10
y = 40
print(x + y)
# Output 50
# Example
name = "Kelly"
surname = "Ault"
print(surname + " " + name)
# Output Ault Kelly
# Subtraction -
x = 10
y = 40
print(y - x)
# Output 30
# Example
# Multiplication *
x = 2
y = 4
z = 5
print(x * y)
# Output 8 (2*4)
print(x * y * z)
# Output 40 (2*4*5)
# Example
name = "Jessa"
print(name * 3)
# Output JessaJessaJessa
# Division /
x = 2
y = 4
z = 8
print(y / x)
# Output 2.0
print(z / y / x)
# Output 1.0
# Example
x = 10
y = 40
print(x + y)
# Output 50
name = "Kelly"
surname = "Ault"
print(surname + " " + name)
# Output Ault Kelly
# Example
x = 10
y = 40
print(y - x)
# Output 30
# Example
x = 2
y = 4
z = 5
print(x * y)
# Output 8 (2*4)
print(x * y * z)
# Output 40 (2*4*5)
# Example
name = "Jessa"
print(name * 3)
# Output JessaJessaJessa
# Example
x = 2
y = 4
z = 8
print(y / x)
# Output 2.0
print(z / y / x)
# Output 1.0
# print(z / 0)  # error
x = 2
y = 4
z = 2.2
# normal division
print(y / x)
# Output 2.0
# floor division to get result as integer
print(y // x)
# Output 2
# normal division
print(y / z)  # 1.81
# floor division.
# Result as float because one argument is float
print(y // z)  # 1.0
# Moduls
x = 15
y = 4
print(x % y)
# Output 3
# Exponent
num = 2
# 2*2
print(num ** 2)
# Output 4
# 2*2*2
print(num ** 3)
# Output 8
# Relational (comparison) operators
x = 10
y = 5
z = 2
# > Greater than
print(x > y)  # True
print(x > y > z)  # True
# < Less than
print(x < y)  # False
print(y < x)  # True
# Equal to
print(x == y)  # False
print(x == 10)  # True
# != Not Equal to
print(x != y)  # True
print(10 != x)  # False
# >= Greater than equal to
print(x >= y)  # True
print(10 >= x)  # True
# <= Less than equal to
print(x <= y)  # False
print(10 <= x)  # True
# Assignment operators
a = 4
b = 2
a += b
print(a)  # 6
a = 4
a -= 2
print(a)  # 2
a = 4
a *= 2
print(a)  # 8
a = 4
a /= 2
print(a)  # 2.0
a = 4
a **= 2
print(a)  # 16
a = 5
a %= 2
print(a)  # 1
a = 4
a //= 2
print(a)  # 2
# Logical operators
print(True and False)  # False
# both are True
print(True and True)  # True
print(False and False)  # False
print(False and True)  # false
# actual use in code
a = 2
b = 4
# Logical and
if a > 0 and b > 0:
    # both conditions are true
    print(a * b)
else:
    print("Do nothing")
# Logical or
print(True or False)  # True
print(True or True)  # True
print(False or False)  # false
print(False or True)  # True
# actual use in code
a = 2
b = 4
# Logical and
if a > 0 or b < 0:
    # at least one expression is true so conditions is true
    print(a + b)  # 6
else:
    print("Do nothing")
# In operator
my_list = [11, 15, 21, 29, 50, 70]
number = 15
if number in my_list:
    print("number is present")
else:
    print("number is not present")
#Not in operator
my_tuple = (11, 15, 21, 29, 50, 70)
number = 35
if number not in my_tuple:
    print("number is not present")
else:
    print("number is present")
# IS operator
x = 10
y = 11
z = 10
print(x is y)  # it compare memory address of x and y
print(x is z)  # it compare memory address of x and z
# is not operator
x = 10
y = 11
z = 10
print(x is not y)  # it campare memory address of x and y
print(x is not z)  # it campare memory address of x and z