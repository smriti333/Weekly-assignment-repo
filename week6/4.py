def encrypt_message(message):
    encrypted = message.replace(" ", "")[::1]
    return encrypted
test_messages = ["This is a test", "Encryption example"]
test_results = {message: encrypt_message(message) for message in test_messages}
print(test_results)