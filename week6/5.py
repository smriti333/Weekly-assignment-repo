import random
import string

def random_encryption(message):
    # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    
    encrypted_message = ""
    counter = 0  # Track the number of characters added
    
    for char in message:
        if char.isalpha():  # Only process alphabetic characters
            if counter > 0 and counter % interval == 0:
                # Insert a random letter every 'interval' characters
                encrypted_message += random.choice(string.ascii_lowercase)
            encrypted_message += char
            counter += 1
            
    return encrypted_message, interval

# Example usage:
message = "send cheese"
encrypted_message, interval = random_encryption(message)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Interval used: {interval}")
