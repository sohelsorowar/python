
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

def smallest_multiple(n):
    if (n<=2):
        return n
    i = n*2
    factors= [number for number in range(n,1,-1) if number *2>n]
    print(factors)

    while True:
        for a in factors:
            if i % a !=0:
                i+=n
                break
            if (a == factors[-1] and i % a == 0):
                return i

print(smallest_multiple(13))
print(smallest_multiple(11))