# iterator ans for loop are same
nums = [7,6,8,9]
for i in nums:
    print(i)
it = iter(nums)
print("first==",it.__next__()) #it will print one value
print("second==",it.__next__())




#create won iterator


class TopTen():
    def __init__(self):
        self.num =0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration
values = TopTen()
print(next(values))
for i in values:
    print(i)
