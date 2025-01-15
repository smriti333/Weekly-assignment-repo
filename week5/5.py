import sys

def process_temperatures(temperatures):
    if not temperatures:
        print("No temperature readings provided.")
        return

    # Convert input strings to floats
    temperatures = list(map(float, temperatures))
    
    # Calculate maximum, minimum, and mean
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    # Display results
    print(f"Maximum Temperature: {max_temp:.2f}°C")
    print(f"Minimum Temperature: {min_temp:.2f}°C")
    print(f"Mean Temperature: {mean_temp:.2f}°C")

if __name__ == "__main__":
    # Exclude the first argument which is the script name
    temperature_readings = sys.argv[1:]
    process_temperatures(temperature_readings)