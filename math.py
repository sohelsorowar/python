
# pi=22/7

# degree=float(input("enter degree: "))
# radian= degree*(pi/180)
# print(radian) 

#3 trapezoid

# h=float(input("height: "))
# a=float(input("f_value: "))
# b=float(input("s_value: "))

# trapezoid=((a+b)/2)*h
# print(trapezoid)

#5 cylender

# pi=22/7
# h=float(input("height: "))
# r=float(input("Radius"))
# v=pi*(r*r)*h
# print(v)

# A= (2*pi*r*h )+ (2*pi*(r*r))

# print(A)

#10 smallest multiple

# def smallest_multiple(n):
#     if (n<=2):
#         return n
#     i = n*2
#     factors= [number for number in range(n,1,-1) if number *2>n]
#     print(factors)

#     while True:
#         for a in factors:
#             if i % a !=0:
#                 i+=n
#                 break
#             if (a == factors[-1] and i % a == 0):
#                 return i

# print(smallest_multiple(13))
# print(smallest_multiple(11))


#pyramid problems 

# def peramid(x):

#     for i in range(x):
#         for j in range(i+1):
#             print("*", end=" ")
#         print("\r")

# x=int(input("enter number: "))
# peramid(x)

# print(".........")

# def per(z):
#     k= 2*z - 2
#     for i in range(0,z):
#         for j in range(0,k):
#             print(end="")
#         k=k-2
#         for j in range(0, i+1): 
#             print("* ", end="")
#         print("\r")

# z=5
# per(z)   

# def pypart2(n): 
#     k = 2*n - 2
#     for i in range(0, n): 
#         for j in range(0, k): 
#             print(end=" ") 
#         k = k - 2
#         for j in range(0, i+1): 
#             print("* ", end="")      
#         print("\r") 
# n = 5
# pypart2(n) 

# rows = 5
# b = 0
# for i in range(rows, 0, -1):
#     b += 1
#     for j in range(1, i + 1):
#         print(b, end=' ')
#     print('\r')


# >>>>>>>       <<<<<<<<<<<
# rows = 10
# b=0
# for i in range(rows):

#     for j in range(-1+i,-1,-1):
#         print(format(2**j,"5d"), end=" ")
#     print(" ")

#     1  
#     2     1  
#     4     2     1  
#     8     4     2     1  
#    16     8     4     2     1  
#    32    16     8     4     2     1  
#    64    32    16     8     4     2     1  
#   128    64    32    16     8     4     2     1  
#   256   128    64    32    16     8     4     2     1  
# >>>>>>>>>>>>>>      <<<<<<<<<<<


# c=1
# s=2
# rows=3

# for i in range(rows):
#     for j in range(1,s):
#         print(c, end=" ")
#         c+=1
#     print(" ")
#     s+=2

# 1  
# 2 3 4  
# 5 6 7 8 9  
# >>>>>>>> <<<<<<<<<<<<



# rows = 6
# for i in range(0, rows):
#     for j in range(rows - 1, i, -1):
#         print(j, '', end='')
#     for l in range(i):
#         print('    ', end='')
#     for k in range(i + 1, rows):
#         print(k, '', end='')
#     print('\n')

# 5 4 3 2     2 3 4 5 

# 5 4 3         3 4 5 

# 5 4             4 5 

# 5                 5 
# >>>>>>>>>>>>>>>            <<<<<<<<<<




# rows = 6
# for row in range(1, rows):
#     num = 1
#     for j in range(rows, 0, -1):
#         if j > row:
#             print(" ", end=' ')
#         else:
#             print(num, end=' ')
#             num += 1
#     print("")
#           1 
#         1 2 
#       1 2 3 
#     1 2 3 4 
#   1 2 3 4 5 




print("Print equilateral triangle Pyramid with characters ")
# size = 7
# asciiNumber = 65
# m = (2 * size) - 2
# for i in range(0, size):
#     for j in range(0, m):
#         print(end=" ")
#     m = m - 1
#     for j in range(0, i + 1):
#         character = chr(asciiNumber)
#         print(character, end=' ')
#         asciiNumber += 1
#     print(" ")


# change string camel case to snake case


# def change_case(str):
#     res=[str[0].lower()]
#     for c in str[1: ]:
#         if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#             res.append('_')
#             res.append(c.lower())
#         else:
#             res.append(c)
#     return ''.join(res)


# str="SohelSorowar"
# print(change_case(str))

input = ['fun', 'Foo', 'BaR'] 

lst=[x.upper() for x in input]
print(lst)