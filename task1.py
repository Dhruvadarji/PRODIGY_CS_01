# Task-01: Caesar Cipher Implementation
# Encrypt and Decrypt text using Caesar Cipher

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  # Non-letters remain unchanged
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# --- Main Program ---
print("=== Caesar Cipher ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("\nEncrypted Message:", encrypted)
print("Decrypted Message:", decrypted)