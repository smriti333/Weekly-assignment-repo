def celsius_to_fahrenheit(celsius_temp):
    # Convert Celsius to Fahrenheit
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return fahrenheit_temp

def main():
    temperatures = []  # List to store the temperatures in Celsius
    
    # Read temperatures until the user presses Enter with no input
    while True:
        temp_input = input("Enter a temperature in Celsius (e.g., 25C) or press Enter to stop: ").strip()
        
        if temp_input == "":  # Stop if no input is provided
            break
        
        # Check if the input is valid
        if temp_input[-1].lower() == 'c' and temp_input[:-1].replace('.', '', 1).isdigit():
            celsius_temp = float(temp_input[:-1])  # Convert the input to a number
            temperatures.append(celsius_temp)
        else:
            print("Invalid input. Please enter a number followed by 'C' (e.g., 25C).")
    
    # Check if an
