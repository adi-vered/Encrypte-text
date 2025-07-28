def encrypte_text(secret, text):
    result = ""
    for i in range(len(text)):
        text_char = text[i]
        secret_char = secret[i % len(secret)]
        char_to_add = chr(ord(text_char) + ord(secret_char))
        print(ord(char_to_add))
        result += char_to_add
    return result

print(encrypte_text("123456", "hello"))