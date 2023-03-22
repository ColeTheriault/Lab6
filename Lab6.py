def main():  # Function that stores the programs menu
    new_password = 0
    print()
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()
    while True:  # Loop that runs while true
        menu_option = int(input('Please enter an option: '))  # asks user to choose a menu option
        if menu_option == 1:  # if statement that occurs if menu option is 1
            old_password = input('Please enter your password to encode: ')  # stores user password
            new_password = encoder(old_password)  # calls the encode function with the users password
            print('Your password has been encoded and stored!')
            print()
        elif menu_option == 2:  # if statement that occurs if menu option is 2
            if new_password != 0: # New_password is 0 by default to avoid issues
                decoded_password = decoder(new_password)
                print('Your password is:', decoded_password)
                print()
            else:  # In case there is no stored password
                print('No stored password')
        elif menu_option == 3:  # if statement that occurs if menu option is 3
            break


def encoder(password):  # Function that encodes/ changes the password inputted by user
    new_password_string = ''
    for variable in password:  # Takes each individual number from the password by user
        number = int(variable)  # Changes the variable to an integer
        number = str(number + 3)  # Adds 3 to the variable and changes the variable back to a string
        new_password_string = new_password_string + number[-1]  # adds the last number in the variable
    return new_password_string  # returns the new password


def decoder(x):
    x = int(x)  # Turns value into integer
    a = (((x // 10000000) % 10) + 7) % 10
    b = (((x // 1000000) % 10) + 7) % 10
    c = (((x // 100000) % 10) + 7) % 10
    d = (((x // 10000) % 10) + 7) % 10
    e = (((x // 1000) % 10) + 7) % 10
    f = (((x // 100) % 10) + 7) % 10   # Fetches values for each individual place and adds 7.
    g = (((x // 10) % 10) + 7) % 10    # This returns the original number (3+7=10) if you mod it with 10.
    h = ((x % 10) + 7) % 10
    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)
    e = str(e)
    f = str(f)
    g = str(g)
    h = str(h)
    addition = a + b + c + d + e + f + g + h   # Adds strings together to get the password value
    return addition


if __name__ == '__main__':
    main()

