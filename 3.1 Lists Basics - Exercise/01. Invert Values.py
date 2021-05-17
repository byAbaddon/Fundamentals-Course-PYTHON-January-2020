num_list = list(map(int, input().split(' ')))
filter_list = list(map(lambda x: x * -1 if x > 0 else abs(x), num_list))

print(filter_list)

