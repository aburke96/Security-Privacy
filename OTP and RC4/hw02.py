import os

#main menu
def menu(): 
	print("1: encrypt")
	print("2: decrypt")
	print("3: break")
	print("4: exit")
 
#sub menu 
def display_menu():
    print("1: One Time Pad")
    print("2: RC4")
    print("3: Quit")

def main():
    user_input= "1"
    while user_input != "3":
        display_menu()
        user_input = input("What would you like to do?")
    if user_input == "1":
        plaintext, key = inputForOTP()
        print("Encrypted message: " + oneTimePad(plaintext, key))
def generate_key(length):
    	
    return os.urandom(length)

def xor_strings(s, key):

    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s, key))

def encrypt(message):

    key = generate_key(len(message))
    cipher = xor_strings(message, key)
    return cipher, key

def decrypt(cipher, key):

    decrypted_message = xor_strings(cipher, key)
    return decrypted_message

# Example Usage
message = "Hello, World!"
cipher, key = encrypt(message)
print("Encrypted:", cipher)

decrypted_message = decrypt(cipher, key)
print("Decrypted:", decrypted_message)

"""
