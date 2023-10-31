#Nora Nguyen and Ava Heflin
def encode(string):
    decoded = []
    for i in string:
        x = int(i)
        x += 3
        decoded.append(str(x))
        full_decoded = ''.join(decoded)
    print("Your password has been encoded and stored!\n")
def decode(string):
    encoded = []
    for j in string:
        x = int(j)
        x += 3
        encoded.append(str(x))
        full_encoded = ''.join(encoded)
        return full_encoded


if __name__ == "__main__":

        while True:
            print("Menu")
            print("-"*13)
            print("1. Encode\n2. Decode\n3. Quit\n")
            user_option = int(input("Please enter an option: "))
            if user_option == 1:
                string_encode = input("Please enter your password to encode: ")
                encode(string_encode)

            if user_option == 2:
                string_decode = decode(string_encode)
                print("The econded password is", string_decode, ", and the orginal password is", string_encode)

            if user_option == 3:
                break

