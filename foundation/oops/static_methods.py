# 07 - Class Methods and Static Methods
# OOP Concept: @classmethod (cls), @staticmethod, alternative constructors

from datetime import date


class Employee:
    _id_counter = 1000
    company = "NeuralTech Inc."

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
        self.emp_id = Employee._next_id()

    # Alternative constructors via @classmethod
    @classmethod
    def from_string(cls, data_str):
        """Create Employee from 'Name,Role,Salary' string."""
        name, role, salary = data_str.split(",")
        return cls(name.strip(), role.strip(), float(salary.strip()))

    @classmethod
    def from_dict(cls, data: dict):
        """Create Employee from a dictionary."""
        return cls(data["name"], data["role"], data["salary"])

    @classmethod
    def get_company(cls):
        return cls.company

    @classmethod
    def _next_id(cls):
        emp_id = cls._id_counter
        cls._id_counter += 1
        return emp_id

    # Pure utility — no access to instance or class state
    @staticmethod
    def is_valid_salary(salary):
        return isinstance(salary, (int, float)) and salary > 0

    @staticmethod
    def calculate_tax(salary, rate=0.2):
        return round(salary * rate, 2)

    def annual_package(self):
        return self.salary * 12

    def __str__(self):
        return f"[{self.emp_id}] {self.name} | {self.role} | ${self.salary:,.0f}/mo"


if __name__ == "__main__":
    e1 = Employee("Alice", "ML Engineer", 9000)
    e2 = Employee.from_string("Bob, Data Scientist, 8500")
    e3 = Employee.from_dict(
        {"name": "Carol", "role": "DevOps", "salary": 7800})

    for emp in [e1, e2, e3]:
        print(emp)

    print(f"\nCompany: {Employee.get_company()}")
    print(f"Tax for {e1.name}: ${Employee.calculate_tax(e1.salary)}")
    print(f"Valid salary (9000): {Employee.is_valid_salary(9000)}")
    print(f"Valid salary (-1): {Employee.is_valid_salary(-1)}")
    print(f"Annual Package for {e1.name}: ${e1.annual_package():,}")
