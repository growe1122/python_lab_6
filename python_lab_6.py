#  Lab 6: Software Engineering, Mary Rowe

def encode(raw_password_string):  # encodes password by adding 3 to each digit
    #  raw_password_string = '12345555'
    encoded_password_list = []
    raw_password_list = list(raw_password_string)
    for idx, elem in enumerate(raw_password_list):
        encoded_password_list.append(str(int(elem) + 3))
    encoded_password_string = ''.join(encoded_password_list)
    # encoded_password_string = '45678888'
    return encoded_password_string


def decode(encoded_password_string):  # password decoder function
    decoded_password_list = []
    encoded_password_list = list(encoded_password_string)
    for elem in encoded_password_list:
        decoded_password_list.append(str((int(elem) - 3) % 10))
    decoded_password_string = ''.join(decoded_password_list)
    return decoded_password_string


def main():

    option_quit = False

    while not option_quit:
        print('\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        option = int(input('\nPlease enter an option: '))
        if option == 1:  # encode password
            decoded_password = input('Please enter your password to encode: ')
            encoded_password = encode(decoded_password)
            print('Your password has been encoded and stored!')
        elif option == 2:  # decode password option added using decode() function
            print("The encoded password is", encoded_password, "and the original password is", decoded_password)
        elif option == 3:
            option_quit = True


if __name__ == "__main__":
    main()