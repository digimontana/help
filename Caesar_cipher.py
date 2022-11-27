from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceaser(start_text,shift_amount,cipher_direction ):
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"Here's the {direction}d result : {cipher_text}")
yes = True


print(logo)
while yes:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(start_text=text, shift_amount=shift , cipher_direction=direction)
    result = input("Write yes if you want to continue if you want to quit just write no\n").lower()
    if result == "no":
        yes = False
        print('Goodbye!')


####################################################################################################
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
# def decrypt(plain_text,shift_amount):
#     real_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         new_position=position - shift_amount
#         new_letter=alphabet[new_position]
#         real_text += new_letter
#     print(f"Your decode text is {real_text}")


# if (direction == "encode"):
#     encrypt(plain_text=text,shift_amount=shift)
# elif(direction == "decode"):
#     decrypt(plain_text=text,shift_amount=shift)
# else :
#     print('Choose "encode" or "decode"')
#     exit()

