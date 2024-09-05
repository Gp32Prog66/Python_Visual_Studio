import json

#JSON code

tools = '{"drill": "Dewalt", "screwdriver": "Commercial Electric", "headlamp": "Klein"}'

#Parse tools:

toolsDisplay = json.loads(tools)

print(toolsDisplay["drill"])
print(toolsDisplay["screwdriver"])
print(toolsDisplay["headlamp"])


#json.dumps method 

toolInventory = json.dumps(tools)

print(toolInventory)

#sort tools
json.dumps(tools, indent=10, sort_keys=True)
