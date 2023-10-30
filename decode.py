#Nora Nguyen
def encode(string):
    decoded = []
    for i in string:
        x = int(i)
        x += 3
        decoded.append(str(x))
        full_decoded = ''.join(decoded)
    print("Your password has been encoded and stored!\n")
def main():
    while True:
        print("Menu")
        print("-"*13)
        print("1. Encode\n2. Decode\n3. Quit\n")
        user_option = int(input("Please enter an option: "))
        if user_option == 1:
            string_encode = input("Please enter your password to encode: ")
            encode(string_encode)
        elif user_option == 3:
            break

if __name__ == "__main__":
    main()