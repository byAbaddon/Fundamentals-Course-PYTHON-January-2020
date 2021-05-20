def odd_even_sum(string):
    odd, even = 0, 0
    
    for i in string:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)

    return f'Odd sum = {odd}, Even sum = {even}'


print(odd_even_sum(input()))
