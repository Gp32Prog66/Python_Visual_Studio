import json

# Python Object. Display a user's Basic Info.
info = {
    "name": "Raymond",
    "age": 25,
    "university": "Carlow University"
    }

# converting JSON
convertingJSON = json.dumps(info)

# Print
print(convertingJSON)
