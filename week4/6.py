def celsius_to_fahrenheit(celsius_temp):
    # Convert Celsius to Fahrenheit
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return fahrenheit_temp

def main():
    # Take input in the format 'XXC'
    temp_input = input("Enter temperature in Celsius (e.g., 25C): ").strip()
    
    # Check if the input is valid
    if temp_input[-1].lower() == 'c' and temp_input[:-1].replace('.', '', 1).isdigit():
        celsius_temp = float(temp_input[:-1])  # Convert the input to a number
        fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
        print(f"{fahrenheit_temp:.2f}F")  # Display the temperature in Fahrenheit with 2 decimal points
    else:
        print("Invalid input. Please enter a number followed by 'C' (e.g., 25C).")

if __name__ == "__main__":
    main()

