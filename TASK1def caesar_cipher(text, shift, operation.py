def caesar_cipher(text, shift, operation):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26  # Normalize the shift to stay within the alphabet
            ascii_offset = 65 if char.isupper() else 97
            
            if operation == "encrypt":
                new_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            elif operation == "decrypt":
                new_char = chr((ord(char) - ascii_offset - shift_amount) % 26 + ascii_offset)
                
            result += new_char
        else:
            result += char  # Non-alphabet characters remain unchanged
    
    return result

def main():
    # Get input from the user
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    operation = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

    if operation in ['encrypt', 'decrypt']:
        result = caesar_cipher(message, shift, operation)
        print(f"The {operation}ed message: {result}")
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
