import csv

employees = [["Name","Age","Job"],
             ["Ahsan",19,"Data Scientist"],
             ["Sachin",19,"Data Scientist"],
             ["Majid",20,"Developer"]]

file_path = "C:/Users/Lenovo/Desktop/Python/Filling/Users.csv" 

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv File '{file_path}' was created!")
except FileExistsError:
    print("That file already exists")