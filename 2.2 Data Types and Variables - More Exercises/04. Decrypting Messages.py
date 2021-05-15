key = int(input())
n = int(input())
collection = [input() for _ in range(n)]

result = list(map(lambda a: chr(ord(a) + key), collection))
print(''.join(result))