players = set(input().split(' '))
a_team = 11 - len(list(filter(lambda x: x.split('-')[0] == 'A' , players)))
b_team = 11 - len(list(filter(lambda x: x.split('-')[0] == 'B' , players)))

print(f'Team A - {a_team}; Team B - {b_team}')
print('Game was terminated') if a_team < 7 or b_team < 7 else None



#-------------------------------(2)-------Fucking Judge --------------------------------------------
# from re import findall

# coll_list = ''.join(set(input().split(' ')))
# a_team = findall(r'A+', coll_list)
# b_team = findall(r'B+', coll_list)

# a_players = 11 - len(a_team) 
# b_players = 11 - len(b_team) 

# print(f'Team A - {a_players}; Team B - {b_players}')