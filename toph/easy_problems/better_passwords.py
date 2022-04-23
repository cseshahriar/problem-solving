""" better passwords """
password = input()
# sentence first character to upper
password_first_char_upper = password[:1].upper() + password[1:]
password = password_first_char_upper.replace('s', '$')
password = password.replace('i', '!')
password = password.replace('o', '()')
password += '.'
print(password)
