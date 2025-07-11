import json

employee = {
    "name":"Ahsan Ali",
    "age": 19,
    "job":"Data scientist"
}

file_path = "C:/Users/Lenovo/Desktop/Python/Filling/UserData.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee,file, indent=4)
        print(f"Json file {file_path} was created!")
except FileExistsError:
    print("That file doesn't exists!")