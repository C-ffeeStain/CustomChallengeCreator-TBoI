import xml.etree.ElementTree as ET

items = {}

with open("items.xml") as f:
    tree = ET.parse(f)
    root = tree.getroot()
    for item in root.findall("passive"):
        items[item.attrib["name"]] = item.attrib["id"]
    for item in root.findall("active"):
        items[item.attrib["name"]] = item.attrib["id"]

print(items["Spoon Bender"])
