#simple loop creating for running the code 6 times
"""for i in range(6):
      celsius=float(input("Enter the temperature in celsius: "))
      fahrenheit = (celsius * 9/5) + 32
      print(f"the temperature in fahrenheit is {fahrenheit} F")
"""
def celsius_to_fahrenheit(celsius_temp):
    # Convert Celsius to Fahrenheit
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return fahrenheit_temp

def main():
    temperatures = []  # List to store the temperatures in Celsius
    
    # Read 6 temperatures
    for i in range(6):
        temp_input = input(f"Enter temperature {i+1} in Celsius (e.g., 25C): ").strip()
        
        # Check if the input is valid
        if temp_input[-1].lower() == 'c' and temp_input[:-1].replace('.', '', 1).isdigit():
            celsius_temp = float(temp_input[:-1])  # Convert the input to a number
            temperatures.append(celsius_temp)
        else:
            print("Invalid input. Please enter a number followed by 'C' (e.g., 25C).")
            return
    
    # Calculate the max, min, and mean temperatures
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)
    
    # Convert the temperatures to Fahrenheit
    max_temp_f = celsius_to_fahrenheit(max_temp)
    min_temp_f = celsius_to_fahrenheit(min_temp)
    mean_temp_f = celsius_to_fahrenheit(mean_temp)
    
    # Display the results
    print(f"Maximum Temperature: {max_temp_f:.2f}F")
    print(f"Minimum Temperature: {min_temp_f:.2f}F")
    print(f"Mean Temperature: {mean_temp_f:.2f}F")

if __name__ == "__main__":
    main()
