def unique_sorted_letters(input_string):
    # Convert string to lowercase and remove duplicates by converting to set
    unique_letters = set(input_string.lower())
    # Filter out non-letter characters
    unique_letters = [letter for letter in unique_letters if letter.isalpha()]
    # Sort the list of unique letters
    unique_letters.sort()
    return unique_letters

# Testing the function with the string 'cheese'
if __name__ == "__main__":
    test_string = "cheese"
    print(unique_sorted_letters(test_string))

