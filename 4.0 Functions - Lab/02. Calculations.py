arr = [input() for _ in range(3)]

def calc(operator, n1, n2):
    operators = {'multiply' : n1 * n2, 'divide' : n1 / n2, 'add' : n1 + n2, 'subtract': n1 - n2}
    return int(operators[operator])

print(calc(arr[0], int(arr[1]), int(arr[2])))    