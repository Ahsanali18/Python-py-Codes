class Employee:

    def __init__(self, name, position):
        self.name=name
        self.position=position
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):  #static method doesn't require any self argument because they are not related to particular instance/object
        valid_positions = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_positions


employee1= Employee("Ahmed","Manager")
employee2= Employee("Akbar","Cashier")
employee3= Employee("Sachin","Cook")


print(Employee.is_valid_position("Cook"))  #to call the static method we directly call it using the class name
print(Employee.is_valid_position("Scientist"))  #to call the static method we directly call it using the class name

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())