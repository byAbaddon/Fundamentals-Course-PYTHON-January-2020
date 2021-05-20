def password_validator(string):
    length = len(string) >= 6  and len(string) <= 10 
    count_digits = 0
    wrong_char = False

    for i in string:
       if  48 <= ord(i) <= 57:
            count_digits += 1
       if  not (65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57):
            wrong_char = True

    if length == True and count_digits >=2 and wrong_char == False:
        print('Password is valid')
    else:
        if length == False : 
            print('Password must be between 6 and 10 characters')
        if wrong_char == True:   
            print('Password must consist only of letters and digits')      
        if count_digits < 2: 
            print('Password must have at least 2 digits')  

password_validator(input())