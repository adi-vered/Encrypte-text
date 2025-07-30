secret = input("Enter your key: ")
text = input("Enter your txt: ")

result = ""
for i, text_char in enumerate(text):
    secret_char = secret[i % len(secret)]
    char_to_add = chr(ord(text_char) + ord(secret_char))
    result += char_to_add

print(result)