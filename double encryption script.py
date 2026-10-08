def encrypted(plaintext,shift):
    result= ""
    for c in plaintext:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            c = chr((ord(c) - base + shift) %26 + base)
        result += c
    return result
print(encrypted("u decoded it", 6))
def text_to_numbers(text):
    number_list = []

    for c in text:
        number_list.append(str(ord(c)))
    return "-".join(number_list)
secret_code = text_to_numbers(encrypted("u decoded it",6))
print(secret_code)