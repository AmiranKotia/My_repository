# def bubble(liist):
#     n = len(liist)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if liist[j] > liist[j+1]:
#                 liist[j], liist[j+1] = liist[j+1], liist[j]
#     return liist
# lst = [5,9,7,6,1,2,4,3,8,0]
# print(bubble(lst))



# OOP (classes and instances):
class Employee:

    num_of_emps = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.initial_pay = pay
        self.email = f"{first}.{last[5:]}@gmail.com"

        Employee.num_of_emps += 1
        self.emp_id = Employee.num_of_emps

    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def display_info(self):
        return f"Employee{self.emp_id}: {self.fullname()}. Initial pay: {self.initial_pay}. Raised to: {self.pay}"
    
    @classmethod
    def set_raise_amt(cls, ammount):
        cls.raise_amt = ammount


id1 = Employee("Gela", "Gelashvili", 55000)
id2 = Employee("Gocha", "Gochadze", 60000)
id3 = Employee("Giga", "Gigauri", 60000)
id4 = Employee("Gandon", "Gandonich", 60000)
id5 = Employee("Gandy", "Man", 60000)

Employee.set_raise_amt(1.1)

print(Employee.raise_amount)

print(f"Number of employees: {Employee.num_of_emps}")
print("----------------------")
id1.apply_raise()
id2.apply_raise()
print(id1.display_info())
print(id2.display_info())
print(id3.display_info())
print(id4.display_info())
print(id5.display_info())