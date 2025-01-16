
def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - shift_base +  shift) % 26 + shift_base))
        else:
            result.append(char)
    return ''.join(result)

while True:
    try:
        word = input("Enter a word to convert:")
        shift = int(input("Enter the shift value (or 0 to exit/cancel):"))
    except ValueError:
        print("Please input a valid integer")
        continue
    
    if shift == 0:
        print("Exiting Program. Goodbye!")
        break
    
    password =  caesar_cipher(word, shift)
    print(f"Your caesar cipher password with specific shift {shift} is: {password}")
                
        
