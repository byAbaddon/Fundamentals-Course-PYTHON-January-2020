coll_list =  input().split(', ')
beggars = int(input())
beggars_list = [0] * beggars

for i in range(len(coll_list)):
    result = i % beggars
    beggars_list[result] += int(coll_list[i])
  
print(beggars_list)        


