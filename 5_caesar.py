while True:
    alphabet = "abcdefghijklmnopqrstuvwxyza "
    encrypt = input("Enter the world:")
    key = int(input("Enter the key:"))
    encrypt = encrypt.lower()
    encrypted = ''
    for letter in encrypt:
        position_1 = alphabet.find(letter)
        position_2 = position_1 + key
        if letter in alphabet:
            encrypted = encrypted + alphabet[position_2]
        else:
            encrypted = encrypted + letter
    print("Your code", encrypted)
