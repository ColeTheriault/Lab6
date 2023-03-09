def main():  # Function that stores the programs menu
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
            pass
        elif menu_option == 3:  # if statement that occurs if menu option is 3
            break


def encoder(password):  # Function that encodes/ changes the password inputted by user
    new_password_string = ''
    for variable in password:  # Takes each individual number from the password by user
        number = int(variable)  # Changes the variable to an integer
        number = str(number + 3)  # Adds 3 to the variable and changes the variable back to a string
        new_password_string = new_password_string + number[-1]  # adds the last number in the variable
    return new_password_string  # returns the new password


if __name__ == '__main__':
    main()

