def manage_capitals():
    # Dictionary to store countries and their capitals
    capitals = {
        "france": "Paris",
        "germany": "Berlin",
        "spain": "Madrid",
        "italy": "Rome",
        "uk": "London",
    }

    while True:
        # Prompt the user to enter a country
        country = input("Enter the name of a country (or 'quit' to exit): ").strip().lower()

        if country == 'quit':
            print("Exiting the program.")
            break

        # Check if the country is in the dictionary
        if country in capitals:
            print(f"The capital of {country.title()} is {capitals[country]}.")
        else:
            print(f"I don't know the capital of {country.title()}.")
            capital = input(f"Please enter the capital of {country.title()}: ").strip()
            capitals[country] = capital
            print(f"Got it! The capital of {country.title()} is now {capital}.")

if __name__ == "__main__":
    manage_capitals()
