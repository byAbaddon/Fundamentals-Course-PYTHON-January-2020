import os
os.system('clear')



tokens = input().strip().split(', ')
tickets = list(map(lambda x: x.strip(), tokens))
while tickets:
    ticket = tickets.pop(0)
    if len(ticket) < 20 or len(ticket) > 20 :
        print('invalid ticket')
        continue
    pattern = ['@', '#',"$", '^'] 
    left_part =  list(filter(lambda x: x in pattern, ticket[0:10]))
    right_part = list(filter(lambda x: x in pattern, ticket[10:20]))
    
  
    
    is_all_equals = len(set(left_part)) == 1  # True or  False
    
    if left_part == []:
                print(f'ticket "{ticket}" - no match')
    elif is_all_equals is not False:
        print(f'ticket "{ticket}" - {10}{left_part[3]} Jackpot!')  
    else:
        long_test = ''
        if left_part.count('@') > 6:
            long_test = left_part.count('@')
        elif  left_part.count('#') > 6 :      
            long_test = left_part.count('#')    
        elif  left_part.count('$') > 6 :      
            long_test = left_part.count('$')    
        elif  left_part.count('^') > 6 :      
            long_test = left_part.count('^')   
        
        print(f'ticket "{ticket}" - {len(left_result.group() -1)}{left_part[4]}') 

# 11111111111111111111
#Пробвай с $$$$$$$^$$$$$^$$$$$$ или ^$$$$$$$$$$$$$$$$$$^ . Трябва да ти върне 6$ за първото и 9$ за 




#---------------------------FUCKING JUDGE---------Time limit---------(2) 

# import re
# # tokens = re.split(r'(,\s+)|(\s+,?\s+)' ,input())
# tickets = input().split(r',\s+')

# while tickets:
#     ticket = tickets.pop(0)
#     if len(ticket) < 20:
#         print('invalid ticket')
#         break

#     left_part = ticket[0:10]  
#     right_part = ticket[10:20]
    
#     pattern = r'(@{6,10})|(#{6,10})|(\${6,10})|(\^{6,10})'
#     left_result = re.findall(pattern, left_part)   
#     right_result = re.findall(pattern, right_part) 

#     if left_result == []:
#         print(' - no match')
#     elif len(left_result[0]) == len(right_result[0]) and len(left_result[0]) < 10:
#         print(f'ticket {ticket} - {len(left_result[0])}{left_result[0][3]}')
#     else:       
#         print(f'ticket {ticket} - {len(left_result[0])}{left_result[0][3]} Jackpot!')
