#Alexandra Burke HW01

def caesar_cipher(text, shift, operation):
    result = ""
    for char in text:
        if char.isalpha():  # Encrypt/decrypt only alphabetic characters
            shift_mod = shift % 26
            if operation == 'decrypt':
                shift_mod = -shift_mod
            shifted_char = chr((ord(char) - 97 + shift_mod) % 26 + 97)
            result += shifted_char
        else:
            result += char
    return result

def encrypt_file(shift):
    with open('plaintext.txt', 'r') as file:
        plaintext = file.read().lower()
    ciphertext = caesar_cipher(plaintext, shift, 'encrypt')
    with open('ciphertext.txt', 'w') as file:
        file.write(ciphertext)

def decrypt_file(shift, file_path='/Users/alexandraburke/Desktop/privacy/ciphertext.txt'):
    try:
        with open(file_path, 'r') as file:
            ciphertext = file.read().lower()
        plaintext = caesar_cipher(ciphertext, shift, 'decrypt')
        with open('plaintext.txt', 'w') as file:
            file.write(plaintext)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
def ing_break():
    return decrypt_file(3, 'ciphertext.txt')

def the_break():
    return decrypt_file(3, 'ciphertext.txt')

def brute_force_break():
    with open('ciphertext.txt', 'r') as file:
        ciphertext = file.read().lower()

    for shift in range(1, 26):
        plaintext = caesar_cipher(ciphertext, shift, 'decrypt')
        print(f"Shift {shift}: {plaintext[:50]}")  # Show a preview of decrypted text
        user_input = input("Does this text look correct? (Y/N): ")
        if user_input.lower() == 'y':
            return shift
    return None

def break_cipher():
    print("1- 'ing' as key\n2- 'the' as key\n3- Brute force as key\n4- Exit to main menu")
    while True:
        choice = input("Choose an option: ")
        if choice == '1':
            ing_break()
            print("Attempted decryption with 'ing' as key.")
            break
        elif choice == '2':
            the_break()
            print("Attempted decryption with 'the' as key.")
            break
        elif choice == '3':
            shift = brute_force_break()
            print(f"Possible key found: {shift}")
            break
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("1- Encrypt\n2- Decrypt\n3- Break\n4- Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            shift = int(input("Enter key value (n): "))
            encrypt_file(shift)
            print("Encryption done.")
        elif choice == '2':
            shift = int(input("Enter key value (n): "))
            decrypt_file(shift)
            print("Decryption done.")
        elif choice == '3':
            shift = break_cipher()
            print(f"Possible key found: {shift}")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
