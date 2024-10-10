import json

# Open File. With statement automatically closes it 
with open("bioInfo.json", "r") as infoFile:
    data = json.load(infoFile)

# Use dump function to encode the JSON file
    with open("bioInfoResults.json", "w") as infoFile:
        json.dump(data, infoFile)

