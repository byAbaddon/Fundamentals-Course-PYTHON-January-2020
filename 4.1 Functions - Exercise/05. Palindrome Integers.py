def palindrome_num(n):
    for i in n:
        if i == i[::-1]:
            print('True')
        else:
            print('False')

palindrome_num( input().split(', '))