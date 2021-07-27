'''
#n = 3
# *
# **
# ***
'''
n = 3
for i in range(n+1):
    print(i*"*")

'''
#n = 4
# *
# **
# ***
# ****
'''
n = 4
for i in range(n+1):
    print(i*"*")


'''
n = 4
 *          #eqn  (2*i-1)
 ***
 *****
 *******'''
n = 4
for i in range(n+1):
    print((2*i-1)* "*")

'''n = 4
      *
    ***
  *****
******* '''
n = 4
for i in range(1 , n+1):
    print(" "*(n-i)+"*"*i)

'''n = 4
  *
  * *
 * * *
* * * * '''
n = 4 
for i in range(1 , n+1):
    print(" "*(n-i)+"* "*i)

'''n = 4 
      *
    * *
  * * *
* * * *'''
n = 4 
for i in range(1 , n+1):
    print("  "*(n-i)+"* "*i)

'''n = 4
   *
  * *
 * * *
* * * *
* * * *
 * * *
  * *
   *'''
n = 4 
for i in range(1 , n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n,0,-1):
    print(" "* (n-i) + "* "*i)

'''n =4
* * * *
  * * *
    * *
      *'''
n = 4
for i in range(n,0,-1):
    print("  "* (n-i) + "* "*i)

'''n =4 
* * * *
* * *
* *
*'''
n = 4
for i in range(n,0,-1):
    print("* "*i)
'''n -4 
*
* *
* * *
* * * *
* * *
* *
*'''
n = 4 
for i in range(1 , n+1):
    print("* "*i)
for i in range(n-1,0,-1):
    print("* "*i)
'''n = 4 
      *
    * *
  * * *
* * * *
  * * *
    * *
      *'''
n =4
for i in range (1 ,n+1):
    print("  "*(n-i)+"* "*i)
for i in range(n-1 , 0 , -1):
    print("  "*(n-i)+"* "*i)
'''
patern printing by using nested for loop

#
# #
# # #
# # # #
'''
for i in range(4):
  for j in range(i+1):
    print("#", end=" ")
  print()

'''
# # # # #
# # # #
# # #
# #
#
'''
# n=int(input("Enter the value:"))
# for i in range(n+1):
#   for j in range(n-i):
#     print("#", end=" ")
#   print()

'''
#
# # #
# # # # #
# # # # # # #
'''

for i in range(5):
  for j in range(2*i-1):
    print("#",end=" ")
  print()

'''
# # # # #
# # # #
# # #
# #
#
'''
for i in range(5,0,-1):
  for j in range(i):
    print("#",end=" ")
  print()

'''
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
'''
num= int(input("Enter the rows:"))
for i in range(1,num+1):
  for j in range(1,num-i+1):
    print(end="  ")
  for j in range(i,0,-1):
    print(j,end=" ")
  for j in range(2,i+1):
    print(j,end=" ")
  print()

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

n=int(input("Enter the rows:"))
for i in range(n+1):
    for j in range(1, i+1):
        print(j,end=" ")
    print()
