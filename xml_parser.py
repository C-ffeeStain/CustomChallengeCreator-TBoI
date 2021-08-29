import xml.etree.ElementTree as ET

items = {}
trinkets = {}

with open("items.xml") as f:
    tree = ET.parse(f)
    root = tree.getroot()
    for item in root.findall("passive"):
        items[item.attrib["name"]] = item.attrib["id"]
    for item in root.findall("active"):
        items[item.attrib["name"]] = item.attrib["id"]
    for item in root.findall("familiar"):
        items[item.attrib["name"]] = item.attrib["id"]
    for item in root.findall("trinket"):
        trinkets[item.attrib["name"]] = item.attrib["id"]


string = "items = {"

for k, v in items.items():
    string += f'"{k}": {v},'

string += "}\n"
string += "trinkets = {"

for k, v in trinkets.items():
    string += f'"{k}": {v},'

with open("items.txt", "w") as f:
    f.write(string)
