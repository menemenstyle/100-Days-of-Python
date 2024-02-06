alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser_cypher(input_message, shift_amount, map):
    message = ""
    if map == "decode":
        shift_amount *= -1
    for letters in input_message:
        if letters in alphabet:
            index = alphabet.index(letters)
            position = index + shift_amount
            if position > 26:
                i = position % 26
                position = i
            elif position < -26:
                j = position % -26
                position = j
            message += alphabet[position]
        else:
            message += letters
    print(f"The {map}d text is {message}")

loop_input = True

while loop_input is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser_cypher(input_message=text, shift_amount=shift, map=direction)
    question = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if question == "no":
        loop_input = False
        print("Goodbye!")
