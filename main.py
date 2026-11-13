import hashlib

def hash_message(message):
    hash_result = hashlib.sha256(message.encode()).hexdigest()
    return hash_result

message = input("Enter a message to hash: ")

result = hash_message(message)

print("\nOriginal message:", message)
print("SHA-256 Hash:", result)

def hash_file(filename):
    with open(filename, "rb") as file:
        file_hash = hashlib.sha256(file.read()).hexdigest()
    return file_hash

filename = input("\nEnter a file name to hash: ")

try:
    print("File SHA-256 Hash:", hash_file(filename))
except FileNotFoundError:
    print("File not found. Please check the file name.")

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isascii() and char.isalpha():
            if char.isupper():
                start = ord("A")
            else:
                start = ord("a")

            new_position = (ord(char) - start + shift) % 26
            result += chr(start + new_position)
        else:
            result += char

    return result  

secret_message = input("\nEnter a message to encrypt: ")

encrypted_message = caesar_cipher(secret_message, 3)
decrypted_message = caesar_cipher(encrypted_message, -3)

print("\nEncrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)

