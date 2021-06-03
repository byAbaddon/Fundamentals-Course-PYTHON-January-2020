from re import findall

text = input()
regex = r'((?<=\s)[a-z0-9]+([\.\-_]?[a-z0-9]+)*@[a-z0-9]+([\.\-_]?[a-z0-9]+)*\.[a-z0-9]+([\.\-_]?[a-z0-9]+)*)'
for result in findall(regex, text):
    print(result[0])

#---------------------------(2)------------  # 75 pts  //TODO
#from re import findall
# text = input()
# regex = r"[a-z0-9]{1,}[\.\-\_]?[a-z0-9]{1,}[@][a-z]{1,}\-?[a-z]+[.][a-z]+\.?\w+" 
# result = findall(regex, text)
# print('\n'.join(result))