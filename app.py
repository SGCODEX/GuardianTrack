import random
import time

# Define the Cargo class to represent individual cargo items
class Cargo:
    """
    Represents a cargo item with its attributes.
    """
    def __init__(self, cargo_id, cargo_type, location, hazard_label="None"):
        """
        Initializes a Cargo object.

        Args:
            cargo_id (str): The unique identifier for the cargo.
            cargo_type (str): The type of cargo (e.g., "Chemical", "Flammable").
            location (str): The current location of the cargo.
            hazard_label (str, optional): The hazard label associated with the cargo. Defaults to "None".
        """
        self.cargo_id = cargo_id
        self.cargo_type = cargo_type
        self.location = location
        self.hazard_label = hazard_label

    def __str__(self):
        """
        Returns a string representation of the Cargo object.  Useful for printing.
        """
        return f"Cargo ID: {self.cargo_id}, Type: {self.cargo_type}, Location: {self.location}, Hazard: {self.hazard_label}"

    def update_location(self, new_location):
        """
        Updates the location of the cargo.

        Args:
            new_location (str): The new location of the cargo.
        """
        self.location = new_location

# Define the Airport class to manage cargo and their locations
class Airport:
    """
    Manages cargo items within an airport and their locations.
    """
    def __init__(self, name="Example Airport"):
        """
        Initializes the Airport object.

        Args:
            name (str, optional): The name of the airport. Defaults to "Example Airport".
        """
        self.name = name
        self.cargo_list = []
        # Define the airport layout.  This is a simplified representation.
        self.layout = {
            "Receiving": {"x": 0, "y": 0},
            "Storage A": {"x": 2, "y": 1},
            "Storage B": {"x": 2, "y": 3},
            "Loading Bay 1": {"x": 4, "y": 2},
            "Loading Bay 2": {"x": 4, "y": 4},
            "Exit": {"x": 6, "y": 2},
        }

    def add_cargo(self, cargo):
        """
        Adds a cargo item to the airport's cargo list.

        Args:
            cargo (Cargo): The Cargo object to add.
        """
        self.cargo_list.append(cargo)

    def get_cargo_by_id(self, cargo_id):
        """
        Retrieves a cargo item by its ID.

        Args:
            cargo_id (str): The ID of the cargo to retrieve.

        Returns:
            Cargo or None: The Cargo object if found, None otherwise.
        """
        for cargo in self.cargo_list:
            if cargo.cargo_id == cargo_id:
                return cargo
        return None

    def identify_hazard(self, cargo):
        """
        Simulates hazard identification based on cargo type.  This is a simplified example.

        Args:
            cargo (Cargo): The Cargo object to identify.

        Returns:
            str: The hazard label, or "None" if no hazard is detected.
        """
        if "Flammable" in cargo.cargo_type:
            return "Flammable"
        elif "Chemical" in cargo.cargo_type:
            return "Chemical"
        elif "Toxic" in cargo.cargo_type:
            return "Toxic"
        else:
            return "None"

    def update_location(self, cargo_id, new_location):
        """
        Updates the location of a cargo item.

        Args:
            cargo_id (str): The ID of the cargo to update.
            new_location (str): The new location.
        """
        cargo = self.get_cargo_by_id(cargo_id)
        if cargo:
            cargo.update_location(new_location)
            print(f"Cargo {cargo_id} location updated to {new_location}.")
        else:
            print(f"Cargo with ID {cargo_id} not found.")

    def display_map(self):
        """
        Displays a simplified text-based map of the airport and cargo locations.
        """
        # Determine the maximum x and y coordinates to set map size
        max_x = max(pos['x'] for pos in self.layout.values()) + 1
        max_y = max(pos['y'] for pos in self.layout.values()) + 1

        # Create an empty map
        grid = [[' ' for _ in range(max_x)] for _ in range(max_y)]

        # Place locations on the map
        for location, pos in self.layout.items():
            grid[pos['y']][pos['x']] = location[0]  # Use first letter for abbreviation

        # Place cargo on the map
        for cargo in self.cargo_list:
            cargo_location = self.get_cargo_location(cargo.cargo_id)  # Corrected method call
            if cargo_location:
                x, y = self.layout[cargo_location]['x'], self.layout[cargo_location]['y']
                # Use a number to represent cargo, or combine for multiple
                if grid[y][x].isdigit():
                  grid[y][x] = str(int(grid[y][x]) + 1)
                elif grid[y][x].isalpha():
                    grid[y][x] = '1'
                else:
                    grid[y][x] = '1' #simplification

        # Print the map
        print("-" * (max_x * 4 + 1))  # Adjusted for better formatting
        for row in grid:
            print("| " + " | ".join(row) + " |")
        print("-" * (max_x * 4 + 1))

        # Print cargo details below the map
        for cargo in self.cargo_list:
            print(cargo)

    def get_cargo_location(self, cargo_id):
        """
        Retrieves the current location of a cargo item.

        Args:
            cargo_id (str): The ID of the cargo.

        Returns:
            str or None: The location of the cargo, or None if not found.
        """
        cargo = self.get_cargo_by_id(cargo_id)
        if cargo:
            return cargo.location
        return None

def main():
    """
    Main function to run the simulation.
    """
    # Create an Airport instance
    my_airport = Airport(" মহানগর Airport")

    # Create Cargo instances with different types and initial locations
    cargo1 = Cargo("C001", "Chemical A", "Receiving", "Chemical")
    cargo2 = Cargo("F002", "Flammable Liquid B", "Receiving", "Flammable")
    cargo3 = Cargo("G003", "General Goods", "Receiving")
    cargo4 = Cargo("T004", "Toxic Waste", "Receiving", "Toxic")  # Added Toxic cargo
    cargo5 = Cargo("F005", "Flammable Solid", "Receiving", "Flammable")

    # Add cargo to the airport
    my_airport.add_cargo(cargo1)
    my_airport.add_cargo(cargo2)
    my_airport.add_cargo(cargo3)
    my_airport.add_cargo(cargo4)
    my_airport.add_cargo(cargo5)

    # Simulate cargo movement and hazard identification
    print("Initial Airport State:")
    my_airport.display_map()

    for cargo in my_airport.cargo_list:
        hazard_label = my_airport.identify_hazard(cargo)
        cargo.hazard_label = hazard_label  # Update cargo object with the label
        print(f"Cargo {cargo.cargo_id} identified as: {hazard_label}")

    time.sleep(2)
    my_airport.update_location("C001", "Storage A")
    time.sleep(1)
    my_airport.update_location("F002", "Storage B")
    time.sleep(1)
    my_airport.update_location("G003", "Loading Bay 1")
    time.sleep(1)
    my_airport.update_location("T004", "Storage B")  # Move Toxic cargo
    time.sleep(1)
    my_airport.update_location("F005", "Loading Bay 2")

    print("\nAirport State After Movement:")
    my_airport.display_map()

    print("\nFinal Cargo Details:")
    for cargo in my_airport.cargo_list:
        print(cargo)

if __name__ == "__main__":
    main()