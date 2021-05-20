arr = [int(input()) for _ in range(3)]

def smallest(a, b, c):
    return min(a, b, c)

print(smallest(arr[0], arr[1], arr[2]))