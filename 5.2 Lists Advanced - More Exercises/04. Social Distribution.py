import os   
os.system('clear')
#--------------------------------------WTF  Fucking Judge ???----TODO   only 80pts
population = list(sorted(map(int, input().split(', '))))
min_wealth = int(input())

for poor in range(len(population)):
    if population[poor] >= min_wealth:
        continue
    else:
        for rich in range(len(population) -1, 0, -1):
            if population[rich] >= (min_wealth - population[poor]) + min_wealth :
                population[rich] -= (min_wealth - population[poor])
                population[poor] = min_wealth
            else:
                continue
                    
test = list(filter(lambda x: x >= min_wealth, population))
if len(test) == len(population):
    print(population)
else:
    print('No equal distribution possible')

#---------------------------------(2)--------------------------------#TODO   only 80pts

# import sys

# population = list(sorted(map(int, input().split(', '))))
# min_wealth = int(input())

# ps = sum(population)
# ms = min_wealth * len(population)
# add = 0

# if ps < ms:
#     print('No equal distribution possible')
#     sys.exit()
# else:
#     for i in range(len(population)):               # 2, 3, 5 ,15, 75     | 5
#       if population[i] < min_wealth and not population[i] == min_wealth:               # 5 | 2
#             add +=  (min_wealth - population[i])
#             population[i] = min_wealth
       
#             for j in range(len(population) -1, -1, -1):  
#                 if population[j] >= (add + min_wealth):           # 75 > |5 + min
#                     population[j] -= add  
#                     add = 0
                    
            
#print(population)



#-----------------------------------------(3)--------  #TODO   only 80pts


# import sys

# population = list(sorted(map(int, input().split(', '))))
# min_wealth = int(input())

# ps = sum(population)
# ms = min_wealth * len(population)

# if ps < ms:
#     print('No equal distribution possible')
#     sys.exit()
# else:
#     for i in range(len(population)):
#       if population[i] < min_wealth:
#             add = min_wealth - population[i]
#             if  population[-1] - add >= min_wealth: 
#                 population[-1] -= add
#                 population[i] += add
#             else:
#                 population[-2] -= add
#                 population[i] += add

# print(population)

















