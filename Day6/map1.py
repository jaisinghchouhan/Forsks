import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
names=map(lambda x:random.choice(code_names),names)
print(list(names))