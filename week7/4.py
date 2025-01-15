from collections import defaultdict

def frequency_analysis(message):
    # Initialize a dictionary to store counts of each letter
    letter_count = defaultdict(int)

    # Convert the message to lowercase and iterate through each character
    for char in message.lower():
        if char.isalpha():  # Only consider alphabetic characters
            letter_count[char] += 1

    # Sort the dictionary by frequency in descending order and get the top 6 most common
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

    # Display the six most common letters and their frequencies
    print("The six most common letters and their frequencies:")
    for i in range(min(6, len(sorted_letters))):  # Avoid index error if there are less than 6 letters
        letter, count = sorted_letters[i]
        print(f"{letter.upper()}: {count}")

if __name__ == "__main__":
    # Example message (this could be any encrypted text)
    message = input("Enter a message: ")
    frequency_analysis(message)
