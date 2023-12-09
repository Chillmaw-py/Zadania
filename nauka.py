import random

my_list = ["a","b","c","d","e","f","g","!","?","A","B","C","D","E","F","G","H"]
for k in range(15):
    my_list.append(random.randint(0,9))
for _ in range(16):
    print(f"{(random.choice(my_list))}", end="")

