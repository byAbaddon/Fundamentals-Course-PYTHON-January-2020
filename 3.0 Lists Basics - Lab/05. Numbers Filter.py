n = int(input())
coll_list = [int(input()) for _ in range(n)]
command = input()

option = {
    'even' : list(filter(lambda x: x % 2 == 0 , coll_list)),
    'odd' : list(filter(lambda x:  x % 2 != 0 , coll_list)),
    'negative' : list(filter(lambda x: x < 0 , coll_list)),
    'positive' : list(filter(lambda x: x >= 0 , coll_list)),
}

print(option[command])