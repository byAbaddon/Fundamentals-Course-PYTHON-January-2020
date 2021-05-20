arr = [ord(input()) for i in range(2)]

def ascii(n1, n2):
   return [chr(x) for x in range(n1 +1, n2)]


print(*ascii(arr[0], arr[1]))