input_list = input().lower().split()
data = {}

def isOdd(word):
    result = input_list.count(word)
    if result & 1:
        data[word] = 1
        return data
       
for word in input_list:
    isOdd(word)
  
print(*data)