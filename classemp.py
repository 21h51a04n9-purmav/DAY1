class employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
    def set_salary(self,salary):
        self._salary=salary
    def get_salary(self):
        return self._salary
emp=employee("Alice",5000)
print("Salary before update:",emp.get_salary())
employee_get_salary=int(input("enter salary after update"))
emp.set_salary(employee_get_salary)
print("updated salary:",emp.get_salary())