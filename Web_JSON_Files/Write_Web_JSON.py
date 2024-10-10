import json

# Open File. With statement automatically closes it 
with open("webResults.json", "r") as infoFile:
    data = json.load(infoFile)

# Use dump function to encode the JSON file
    with open("webResultsFinalResults.json", "w") as infoFile:
        json.dump(data, infoFile)
