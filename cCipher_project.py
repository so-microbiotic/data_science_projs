def cCipher(message, shift):
    message = input("What is your message: ")
    shift = input("Enter a whole number: ")
    int(shift)
    new_string = ""
    for i in range(len(message)):
        char = new_string[i]
        new_string = chr(ord(char) + shift)
    return message
    return new_string

