while True:
    word = input()
    if word == 'end':
        break
    else:
        print(word, '=', word[::-1])


