n = int(input())
pos_list = []
neg_list = []

for _ in range(n):
    current = int(input())
    if current >= 0:
       pos_list.append(current) 
    else:
       neg_list.append(current)
  
print(f'{pos_list}\n{neg_list}')
print(f'Count of positives: {len(pos_list)}. Sum of negatives: {sum(neg_list)}')


#------------------------------(2)----Fucking Judge-----------------------------------
# n = int(input())
# pos_list = [int(input()) for i in range(n) if i % 2 == 0]
# neg_list = [int(input()) for i in range(n) if not i % 2 == 0]

# print(f'{pos_list}\n{neg_list}')
# print(f'Count of positives: {len(pos_list)}. Sum of negatives: {sum(neg_list)}')