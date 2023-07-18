#  Lab 6: Software Engineering

def encode(raw_password_string):  # encodes password by adding 3 to each digit
    #  raw_password_string = '12345555'
    encoded_password_list = []
    raw_password_list = list(raw_password_string)
    for idx, elem in enumerate(raw_password_list):
        encoded_password_list.append(str(int(elem) + 3))
    encoded_password_string = ''.join(encoded_password_list)
    # encoded_password_string = '45678888'
    return encoded_password_string


def main():

    option_quit = False

    while not option_quit:
        print('\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        option = int(input('\nPlease enter an option: '))
        if option == 1:  # encode password
            decoded_password = input('Please enter your password to encode: ')
            encoded_password = encode(decoded_password)
            print(encoded_password)
            print('Your password has been encoded and stored!')
        elif option == 2:  # decode password
            pass  # write decode alg here
        elif option == 3:
            option_quit = True


if __name__ == "__main__":
    main()