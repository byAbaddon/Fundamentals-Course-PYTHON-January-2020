ban_words = input().split(', ')
text = input()

for ban in ban_words:
    text = text.replace(ban, '*' * len(ban))

print(text)