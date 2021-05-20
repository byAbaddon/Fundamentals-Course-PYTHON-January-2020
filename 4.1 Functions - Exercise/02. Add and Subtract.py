arr = [int(input()) for _ in range(3)]

def add_and_subtract(a, b, c):

    def sum_numbers(a, b):
        return a + b

    def subtract(num, c):
        return num - c

    return subtract(sum_numbers(a, b),c)    

print(add_and_subtract(arr[0], arr[1], arr[2]))