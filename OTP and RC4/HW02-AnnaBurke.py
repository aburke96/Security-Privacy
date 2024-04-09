# Computer Security and Privacy
# Alexandra (Anna) Burke
# Homework 02
# OTP and RC4 

# op 1: One-Time Pad Encryption
def oneTimePad(plaintext, key):
    # check if plaintext and key are of the same length
    if len(plaintext) != len(key):
        return None  # return 'None' if lengths don't match
    # encrypt plaintext using the key
    # XOR each character in the plaintext with the corresponding character in the key
    ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return ciphertext     

# op 2: RC4 Encryption
def RC4(plaintext, key):
    # perform setupKeyArray to initialize the permutation in array S
    S = setupKeyArray(key)
    # generate keystream using the streamGenerator
    keystream = streamGenerator(S)
    # encrypt plaintext by XORing it with the generated keystream
    ciphertext = ''.join(chr(ord(c) ^ next(keystream)) for c in plaintext)
    return ciphertext

# algorithm for RC4
def setupKeyArray(key):
    key_length = len(key)
    # initialize the array S
    S = list(range(256))
    j = 0
    # does initial permutation of S
    for i in range(256):
        j = (j + S[i] + ord(key[i % key_length])) % 256
        S[i], S[j] = S[j], S[i]
    return S

# algorithm for RC4
def streamGenerator(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        # generate the next keystream value
        K = S[(S[i] + S[j]) % 256]
        yield K

# user menu for encryption 
def menu():
    while True:
        print("1- One-Time Pad\n2- RC4\n3- Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            # encrypt using One-Time Pad
            message = input("Enter the message: ")
            key = input("Enter the key (same length as message): ")
            if len(message) != len(key):
                print("Error: Message and key must be the same length.")
                continue
            ciphertext = oneTimePad(message, key)
            print("Encrypted:", ciphertext)
            # decrypt and print to verify
            print("Decrypted:", oneTimePad(ciphertext, key))
        elif choice == '2':
            # encrypt using RC4
            message = input("Enter the message: ")
            key = input("Enter a short key: ")
            ciphertext = RC4(message, key)
            print("Encrypted:", ciphertext)
            # decrypt and print to verify
            print("Decrypted:", RC4(ciphertext, key))
        elif choice == '3':
            # exit the program
            break
        else:
            print("Invalid option. Select 1, 2, or 3.")

if __name__ == "__main__":
    menu()