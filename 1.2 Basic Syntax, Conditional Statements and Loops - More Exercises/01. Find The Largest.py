# 'Given a number, print the largest number that can be formed from the digits of the number given.'

# Wrong condition, number must be string !!!

#-------------------------------------------------(1)------------------------100pts
n = input()
result = ''.join(reversed(sorted(list(n))))
print(result)


#-------------------------------------------------(2)------------------------100pts
# n = input()
# result = list(str(n))
# print( ''.join(sorted(result, reverse = True)))



#------------------------------------------------(3)------------------------ 100pts
# n = input()

# test = list(str(n))
# test.sort()
# test.reverse()
# print( ''.join(test) )