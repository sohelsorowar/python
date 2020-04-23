nums=[20,15,16,21,26]
for num in nums:
    if num%5==0:
        print(num)
        break
else:
    print("not found")





#prime number test using for_else
num=9

for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")
