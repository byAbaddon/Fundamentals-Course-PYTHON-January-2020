a, b = int(input()), int(input())

def recursion(f):
   if f == 1:
       return f
   else:
       return f * recursion(f - 1)

print(f'{(recursion(a) / recursion(b)):.2f}')




