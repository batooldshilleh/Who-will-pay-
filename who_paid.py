import random
test_seed = int(input("create a seed number: "))
random.seed(test_seed)
namesAsCSV = input("give me everybody's names , seprated by a comma. ")
names = namesAsCSV.split(", ")
x = len(names)
print(x)
r=random.randint(0 , x-1)
pwb = names[r]
print(pwb + "thy bay")
