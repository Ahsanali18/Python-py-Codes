# import os
# import json
import csv

# file_path = "C:/Users/Lenovo/Desktop/Python/Filling/Output.txt"
# file_path = "C:/Users/Lenovo/Desktop/Python/Filling/UserData.json"
file_path = "C:/Users/Lenovo/Desktop/Python/Filling/Users.csv"

try:
    with open(file_path, "r") as file:
        content =  file.read()    # to read the txt  file
        # content =  json.load(file)  # to read the json file
        """
        content = csv.reader(file)  # to read the csv file
        for line in content:
            print(line)"""
        
        print(content)

except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You don't have permission to read that file")