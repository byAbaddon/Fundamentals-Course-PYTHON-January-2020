find_words = input().split(', ')
arr  = input().split(', ')
unique = []

for word in find_words:
    for match in arr:
        if word in match:
            None if word in unique else unique.append(word) 
             
print(unique)

