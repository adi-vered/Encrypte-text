secret = input("Enter your key: ")
text = input("Enter your txt")

def encrypte_text(secret, text):
    result = []
    for i in range(len(text)):
        text_char = text[i]
        secret_char = secret[i % len(secret)]
        char_to_add = ord(text_char) + ord(secret_char)
        result += [char_to_add]
    return result

print(encrypte_text(secret, text))