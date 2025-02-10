#!/usr/bin/python3
"""
This module contains a script that 
adds all arguments to a Python list, and then saves them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    obj = load_from_json_file(filename)
except FileNotFoundError:
    obj = []
for arg in range(1, len(sys.argv)):
    obj.append(sys.argv[arg])
        
save_to_json_file(obj, filename)
