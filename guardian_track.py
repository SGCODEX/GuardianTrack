from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://guardian-track.vercel.app/"}})

#  (Code from Canvas)
class Cargo:
    def __init__(self, cargo_id, cargo_type, location, hazard_label="None"):
        self.cargo_id = cargo_id
        self.cargo_type = cargo_type
        self.location = location
        self.hazard_label = hazard_label

    def __str__(self):
        return f"Cargo ID: {self.cargo_id}, Type: {self.cargo_type}, Location: {self.location}, Hazard: {self.hazard_label}"
#  (Code from Canvas)
class Airport:
    def __init__(self, name="Example Airport"):
        self.name = name
        self.cargo_list = []
        self.layout = {
            "Receiving": {"x": 0, "y": 0},
            "Storage A": {"x": 2, "y": 1},
            "Storage B": {"x": 2, "y": 3},
            "Loading Bay 1": {"x": 4, "y": 2},
            "Loading Bay 2": {"x": 4, "y": 4},
            "Exit": {"x": 6, "y": 2},
        }

    def add_cargo(self, cargo):
        self.cargo_list.append(cargo)

    def get_cargo_by_id(self, cargo_id):
        for cargo in self.cargo_list:
            if cargo.cargo_id == cargo_id:
                return cargo
        return None

    def identify_hazard(self, cargo):
        if "Flammable" in cargo.cargo_type:
            return "Flammable"
        elif "Chemical" in cargo.cargo_type:
            return "Chemical"
        elif "Toxic" in cargo.cargo_type:
            return "Toxic"
        else:
            return "None"
    def update_location(self, cargo_id, new_location):
        cargo = self.get_cargo_by_id(cargo_id)
        if cargo:
            cargo.update_location(new_location)
            print(f"Cargo {cargo_id} location updated to {new_location}.")
        else:
            print(f"Cargo with ID {cargo_id} not found.")

    def get_cargo_location(self, cargo_id):
        cargo = self.get_cargo_by_id(cargo_id)
        if cargo:
            return cargo.location
        return None

# Create an Airport instance and add cargo
my_airport = Airport(" মহানগর Airport")
cargo1 = Cargo("C001", "Chemical A", "Receiving", "Chemical")
cargo2 = Cargo("F002", "Flammable Liquid B", "Receiving", "Flammable")
cargo3 = Cargo("G003", "General Goods", "Receiving")
cargo4 = Cargo("T004", "Toxic Waste", "Receiving", "Toxic")
cargo5 = Cargo("F005", "Flammable Solid", "Receiving", "Flammable")
my_airport.add_cargo(cargo1)
my_airport.add_cargo(cargo2)
my_airport.add_cargo(cargo3)
my_airport.add_cargo(cargo4)
my_airport.add_cargo(cargo5)

@app.route('/api/cargo')
def get_cargo():
    """
    Returns all cargo data as JSON.
    """
    cargo_data = []
    for cargo in my_airport.cargo_list:
        cargo_data.append({
            'cargo_id': cargo.cargo_id,
            'cargo_type': cargo.cargo_type,
            'location': cargo.location,
            'hazard_label': cargo.hazard_label
        })
    return jsonify(cargo_data)

if __name__ == '__main__':
    app.run(debug=True)
