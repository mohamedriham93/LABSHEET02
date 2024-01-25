char_input = (input("Enter a charecter: "))

if char_input.isalpha():
    char_type = char_input, ": is Alphabet"

else:
    char_type = char_input, ": is not an Alphabet"

print (char_type)
