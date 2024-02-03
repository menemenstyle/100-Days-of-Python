alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt (encode_text, shift_amount):
    cypher_text = ""
    
    for letters in encode_text:
        index = alphabet.index(letters)
        position = index + shift_amount
        if position > 26:
            position -= 26
        cypher_letters = alphabet[position]
        cypher_text += cypher_letters
        
    print(f"The encoded text is {cypher_text}")

encrypt(encode_text=text, shift_amount=shift)
