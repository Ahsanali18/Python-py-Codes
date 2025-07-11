import os   # os module allows us to interact with files

file_path = "C:/Users/Lenovo/Desktop/Python/Filling/Hello Test"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists!")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print("File doesn't exists")