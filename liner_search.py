

pos = -1      #global variable

def search(list,n):
    i=0
    while i < len(list):
        if list[i]==n:
            globals()['pos'] = i
            return True
        i +=1
    return False
list = [5,4,6,7,8,9,2]
n=9
if search(list,n):
    print("found in position: ", pos+1)
else:
    print("not found")
