def TopTen():
    yield 5    #this yield is generator



values = TopTen()
print(values)             #it wont print valu 5
print(values.__next__())   # this will print 5




#i want to print TopTen square values


def topten():
    n=1

    while n<=10:
        sq = n*n
        yield sq
        n += 1
value = topten()

for i in value:
    print(i)
