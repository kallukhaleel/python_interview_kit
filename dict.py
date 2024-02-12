# Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json

indian_states = {
    "Uttar Pradesh": "Lucknow",
    "Maharashtra": "Mumbai",
    "Bihar": "Patna",
    "West Bengal": "Kolkata",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Rajasthan": "Jaipur"
}


with open('states.json', "w+")as f:
    json.dump(indian_states, f)
    print("Data  written to states.json file successfully.")