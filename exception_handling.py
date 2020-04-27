#errors
#1.compiletime errors
#2.logical errors
#3.Run time errors

a = 5
b = 0 # if we use 0 it will stop working
try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("you can not divide by zero==Error==",e)

finally:
    print("resource closed")

print("bye")
