text_data = "I like pizza, and this is new file."

employees = ["Ahmed","Ali","Akbar","Sameer","Sachin"]

file_path = "C:/Users/Lenovo/Desktop/Python/Filling/Output.txt"

try:
    with open(file=file_path, mode="w") as file:   #modes : (w,x,a)
        for employee in employees:
            file.write(employee+" ")
        print(f"Text file {file_path} was created!")
except FileExistsError:
    print("That file already exists!")
