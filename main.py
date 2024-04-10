from Scratch import decode

def encode(pw):
    newstr = ""
    for i in pw:
        newnum = int(i) + 3
        newstr += str(newnum)[-1]
    
    return newstr

def main():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")
    option = int(input("Please enter an option: "))
    while option != 3:
        if option == 1:
            pw = input("Please enter the password you want to encode: ")
            encoded = encode(pw)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {encoded} and the original password is {decode(encoded)}")
        else:
            break
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")
        option = int(input("Please enter an option: "))

if __name__ == "__main__":
    main()
    
