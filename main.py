from entitys import Entity
import json

with open("Data/EntityData.json", "r") as file:
    data = file.read()
bob = Entity(json.loads(data))
print(bob.attack())
print(bob.resources)