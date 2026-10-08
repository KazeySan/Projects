#Double Encryption Using Caesar Cipher and Substitution Cipher
def encrypted(plaintext,shift):
    result= ""
    for c in plaintext:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            c = chr((ord(c) - base + shift) %26 + base)
        result += c
    return result
print(encrypted("Enter Plaintext", [number you want to shift the letter by])) #Enter the text you want to encrypt and the shift
def text_to_numbers(text):
    number_list = []

    for c in text:
        number_list.append(str(ord(c)))
    return "-".join(number_list)
secret_code = text_to_numbers(encrypted("Enter Plaintext", [number you want to shift the letter by]))
print(secret_code)
