def decrypt_message(encrypted_message, interval):
    decrypted_message = ""
    counter = 0  # To track every nth character
    
    # Iterate through the encrypted message
    for char in encrypted_message:
        if char.isalpha():  # Only consider alphabetic characters
            if counter % interval == 0:
                decrypted_message += char
            counter += 1
    
    return decrypted_message

# Example usage:
encrypted_message = "sxyexynxydxy cxyhxyexyexysxye"  # Example encrypted message
interval = 7  # Example interval used during encryption

decrypted_message = decrypt_message(encrypted_message, interval)

print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
