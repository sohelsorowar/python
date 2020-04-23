#while Loop
i=1
while i<=5:
    print("hello")
    i+=1


#to print in same line
i=1
while i<=5:
    print("Sohel+",end="")

    j=1
    while j<=5:
        print("Sorowar--",end="")
        j+=1
    i+=1
    print("")



#For Loop


x = ['Sohel',65,2.5]

for i in x:
    print(i)


#print 1 to 10

for i in range(10):
    print(i)


#reverse count

for i in range(20,10,-1): #20 to 11
    print(i)




#simple logic

av=5
x=int(input("how much candies do you want?"))
i=1
while i<x:
    if i>av:
        print("out of stock")
        break
    print("Candy")
    i+=1
print("thankyou")
