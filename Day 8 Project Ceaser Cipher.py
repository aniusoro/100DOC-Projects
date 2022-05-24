
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter.isalpha():
            position = ord(letter)
            new_position = position + shift
            new_letter = chr(new_position)
            encrypted_text += new_letter
    print(f"The encoded text is {encrypted_text}")

def decrypt(text, shift):
    decrypyted_text = ""
    for letter in text:
        if letter.isalpha():
            position = ord(letter)
            new_position = position - shift
            new_letter = chr(new_position)
            decrypyted_text += new_letter
    print(f"The original text is {decrypyted_text}")

if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)



