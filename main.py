from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(plain_text=text, shift_amount=shift, direction=direction):
    result_text = ''
    for char in plain_text:
        if char in alphabet:
          if direction == "encode":
            position = alphabet.index(char) + shift_amount
            new_position = position % len(alphabet)
            result_text += alphabet[new_position]
          elif direction == "decode":
            position = alphabet.index(char) - shift_amount
            new_position = position % len(alphabet)
            result_text += alphabet[new_position]
        else:
          result_text += char
    print(f"The {direction}d text is {result_text}")
            
caesar()


should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")

while should_continue == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(plain_text=text, shift_amount=shift, direction=direction)
  should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
  if should_continue == 'no':
    print("Goodbye")


