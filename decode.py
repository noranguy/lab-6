#Nora Nguyen and Ava Heflin
def encode(string):
    encoded = []
    for i in string:
        x = int(i)
        x = (x+3)%10
        encoded.append(str(x))
        full_encoded = ''.join(encoded)
    print("Your password has been encoded and stored!\n")
    return full_encoded
def decode(string):
    decoded = []
    for j in string:
        y = int(j)
        y = (y-3)%10
        decoded.append(str(y))
        full_decoded = ''.join(decoded)
    print(f"The encoded password is {string}, and the original password is {full_decoded}.\n")
if __name__ == "__main__":
        while True:
            print("Menu")
            print("-"*13)
            print("1. Encode\n2. Decode\n3. Quit\n")
            user_option = input("Please enter an option: ")
            if user_option == "1":
                string_encode = input("Please enter your password to encode: ")
                encoded_str = encode(string_encode)
            elif user_option == '2':
                decode(encoded_str)
            elif user_option == '3':
                break


