def validate_input(input_string):
    uppercase_count= sum(1 for char in input_string if char.isupper())
    lowercase_count= sum(1 for char in input_string if char.islower())
    return uppercase_count, lowercase_count

test_string=input("enter a string: ")
uppercase, lowercase = validate_input(test_string)

print(f"Uppercase letter: {uppercase}")
print(f"Lowercase letter: {lowercase}")