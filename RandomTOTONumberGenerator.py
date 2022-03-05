import random

def randmNumGenerator(x,y):
    Num = random.randint(x,y)
    return Num


my_list = [[],[],[],[],[],[],[],[],[],[]]
Min = 1
Max = 49
i = 0

for x in range(1):
    while (i<6):
        a = randmNumGenerator(Min,Max)
        if a not in my_list[x]:
            my_list[x].append(a)
            i += 1
        else:
            continue
    i = 0
    print(sorted(my_list[x]))
    
