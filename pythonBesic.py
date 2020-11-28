
test_list = ['1', '4', '3', '6', '7'] 

print ("Original list is : " + str(test_list)) 
  
for i in range(0, len(test_list)): 
    test_list[i] = int(test_list[i]) 
print ("Modified list is : " + str(test_list)) 
