#!/usr/bin/python3
"""
XML serialization module
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialize a python dictionary to xml"""
    root = ET.Element("data")
    for key, val in dictionary.items():
        tag = ET.Element(key)
        tag.text = val
        root.append(tag)
    xml_serial = ET.tostring(root, encoding="utf-8")
    xml_string = xml_serial.decode("utf-8")
    with open(filename, "w") as file:
        file.write(xml_string)

def deserialize_from_xml(filename):
    """deserialize an xml file into a python dictionary"""
    with open(filename, "r", encoding="utf-8") as file:
        tree = ET.parse(file)
        root = tree.getroot()
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        return dictionary
