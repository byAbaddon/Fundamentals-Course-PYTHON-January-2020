f_char, l_char  = ord(input()), ord(input())
text =  list(map(lambda x:  ord(x) , input()))
result = sum(filter(lambda x:  x > f_char and  x < l_char , text))
print(result)