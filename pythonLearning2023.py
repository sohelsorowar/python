

words = {'cat','dog','monky','ox'}

for x in words: 
    print((x), len(x))


# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

for i in range(5):
    print(i)