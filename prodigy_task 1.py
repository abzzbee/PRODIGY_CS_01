alphabets = 'abcdefghijklmnopqrstuvwxyz'

while True:
    encryptedMssg = ""
    decryptedMssg = ""

    operation = input("Do you want to encrypt(E) or decrypt(D)? ").upper()

    message = input("Enter message(lower-case): ")
    key = int(input("Enter the key (any one digit number): "))

    if operation == 'E':
        for character in message:
            if character in alphabets:
                position = alphabets.find(character)
                newPosition = (position + key) % 26
                newChar = alphabets[newPosition]
                encryptedMssg += newChar
            else:
                encryptedMssg += character
        print("The encrypted message is: ", encryptedMssg)

    elif operation == 'D':
        for character in message:
            if character in alphabets:
                position = alphabets.find(character)
                newPosition = (position - key) % 26
                newChar = alphabets[newPosition]
                decryptedMssg += newChar
            else:
                decryptedMssg += character
        print("The decrypted message is: ", decryptedMssg)

    else:
        print("Invalid operation! Please choose 'E' for encryption or 'D' for decryption.")

    cont = input("Do you want to perform another operation? (yes/no): ")
    if cont.lower() != 'yes':
        break
