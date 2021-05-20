n = int(input())

def solve(n):
    num_sum = 0

    for i in range(1, n):
        if n % i == 0:
            num_sum += i
    
    if num_sum == n:
        return  'We have a perfect number!'
    else:
        return  'It\'s not so perfect.'

print(solve(n))