import sys
from decimal import Decimal, InvalidOperation
import textwrap

def load_drivers(file_name):
    """Load drivers from a file into a dictionary."""

    drivers = {} #stores drivers information
    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Remove leading/trailing whitespace and split the line by commas.
                parts = line.strip().split(',') 
                 # Ensure the line has exactly 4 parts: ID, Code, Name, and Team.
                if len(parts) == 4:
                    # Add the driver information to the dictionary using the driver code as the key.
                    drivers[parts[1]] = {
                        "id": parts[0],
                        "name": parts[2],
                        "team": parts[3]
                    }
    except FileNotFoundError:
        # Handle the case where the specified file does not exist.
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred while loading drivers: {e}")
        # Return the dictionary containing the loaded driver data.
    return drivers

def process_lap_times(file_names, drivers):
    """Process lap time files and display performance."""
    try:
        # Dictionary to store lap times for each driver.
        driver_times = {}
        # List to store the names of Grand Prix locations.
        grand_prix_locations = []

        # Iterate over each lap time file provided.
        for file_name in file_names:
            with open(file_name, 'r') as file:
                # Read all lines from the file into a list.
                lines = file.readlines()

            # Extract the Grand Prix location from the first line
            grand_prix_location = lines[0].strip()
            grand_prix_locations.append(grand_prix_location)

            # Process the rest of the file , process each line in the file subsequently (skiping the first line)
            for line in lines[1:]:
                # Skip empty lines or lines shorter than 4 characters (invalid data).
                if len(line.strip()) < 4:
                    print(f"Skipping invalid line in {file_name}: {line.strip()}")
                    continue
                driver_code = line[:3]
                try:
                    # Convert the lap time to a float.
                    lap_time = Decimal(line[3:].strip())
                except InvalidOperation:
                    # Skip lines where the lap time cannot be converted to a float.
                    print(f"Invalid lap time in {file_name}: {line.strip()}")
                    continue

                if driver_code not in driver_times:
                    driver_times[driver_code] = []
                    # Append the current lap time and location to the driver's data.
                driver_times[driver_code].append((grand_prix_location, lap_time))

        # Calculate overall average time
        total_time = Decimal(0)
        total_laps = 0
        for laps in driver_times.values():
            total_time += sum(lap[1] for lap in laps)
            total_laps += len(laps)
        overall_average_time = total_time / total_laps
        print(f"Overall Average Time: {overall_average_time:.3f}")

        # Display driver performance
        overall_fastest_lap = Decimal('Infinity')
        overall_fastest_driver = None

        print("+-----------------+----------------------+----------------+------------------+----------------+")
        print("| Driver          | Team                 | Best Lap Time  | Average Lap Time | Number of Laps |")
        print("+-----------------+----------------------+----------------+------------------+----------------+")
        
        # Iterate over each driver to calculate and display their performance metrics.
        for driver_code, laps in driver_times.items():
            times = [lap[1] for lap in laps]
            best_time = min(times)
            avg_time = sum(times) / len(times)
            lap_count = len(times)

            if best_time < overall_fastest_lap:
                overall_fastest_lap = best_time
                overall_fastest_driver = driver_code
             
            # textwrap.shorten is useful for formatting long driver or team names to fit within a fixed table column width.
            driver_info = drivers.get(driver_code, {"name": "Unknown", "team": "Unknown"})
            driver_name = textwrap.shorten(driver_info['name'], width=15, placeholder="...")
            team_name = textwrap.shorten(driver_info['team'], width=20, placeholder="...")
            print(f"| {driver_name:<15} | {team_name:<20} | {best_time:<14.3f} | {avg_time:<16.3f} | {lap_count:<14} |")

        print("+-----------------+----------------------+----------------+------------------+----------------+")

        # Display the overall fastest lap
        fastest_driver_info = drivers.get(overall_fastest_driver, {"name": "Unknown", "team": "Unknown"})
        print("\nOverall Fastest Lap:")
        print(f"Driver: {fastest_driver_info['name']} ({fastest_driver_info['team']}), Time: {overall_fastest_lap:.3f}")

    except FileNotFoundError as e:
        # Handle the case where one of the lap time files is missing.
        print(f"Error: A file was not found: {e}")
    except Exception as e:
        # Catch any other exceptions and display the error message.
        print(f"An error occurred: {e}")

if __name__ == "__main__":
     """
    Entry point for the program. Validates command-line arguments, loads driver data,
    and processes lap time files.
    """
    # Check if the required number of command-line arguments is provided.
     if len(sys.argv) < 3:
        # Display usage instructions if arguments are missing.
        print("Usage: python f1_lap_analysis.py <drivers_file> <lap_time_file1> [<lap_time_file2> ...]")
     else:
        drivers_file = sys.argv[1]
        lap_time_files = sys.argv[2:]
        drivers_data = load_drivers(drivers_file)
         # Call the function to process lap time files and display performance metrics.
        process_lap_times(lap_time_files, drivers_data)

#to run the program:
        #  python f1_lap_analysis.py drivers.csv lap_time_1.txt lap_time_2.txt lap_time_3.txt
        #  "drivers.txt" contains driver information.
        # "lap_time_1.txt" files contain lap times for different Grand Prix events 