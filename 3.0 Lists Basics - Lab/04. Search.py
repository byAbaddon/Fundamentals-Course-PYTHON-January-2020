n = int(input())
word = input()

coll_list = [input() for _ in range(n)]
filtered_list = list(filter(lambda string : word in string, coll_list))

print(coll_list)
print(filtered_list)