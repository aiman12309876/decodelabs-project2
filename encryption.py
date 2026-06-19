import string

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isdigit():
            result += str((int(char) + shift) % 10)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def display_menu():
    print("\n" + "=" * 60)
    print("   BASIC ENCRYPTION & DECRYPTION")
    print("=" * 60)
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Exit")
    print("=" * 60)

def main():
    print("\n" + "=" * 60)
    print("   CYBERSECURITY - BASIC ENCRYPTION")
    print("=" * 60)

    shift = 3

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            text = input("\nEnter text to encrypt: ")
            encrypted = caesar_encrypt(text, shift)
            print("\n" + "-" * 40)
            print(f"Original: {text}")
            print(f"Shift Key: {shift}")
            print(f"Encrypted: {encrypted}")
            print("-" * 40)

        elif choice == "2":
            text = input("\nEnter text to decrypt: ")
            decrypted = caesar_decrypt(text, shift)
            print("\n" + "-" * 40)
            print(f"Encrypted: {text}")
            print(f"Shift Key: {shift}")
            print(f"Decrypted: {decrypted}")
            print("-" * 40)

        elif choice == "3":
            print("\nExiting... Goodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    main()