import random
import pandas as pd
from faker import Faker

fake = Faker()
departments = {
    1: ("Human Resources", ["Human Resources Manager", "Recruiter", "Human Resources Specialist"]),
    2: ("Finance", ["Chief Financial Officer (CFO)", "Accountant", "Financial Analyst"]),
    3: ("Marketing", ["Marketing Manager", "Content Creator", "SEO Specialist"]),
    4: ("Sales", ["Sales Manager", "Sales Representative", "Account Manager"]),
    5: ("Information Technology (IT)", ["Information Technology Manager", "Network Administrator", "Software Developer"]),
    6: ("Operations", ["Operations Manager", "Logistics Coordinator", "Quality Assurance Specialist"]),
    7: ("Customer Service",
        ["Customer Service Manager", "Customer Service Representative", "Technical Support Specialist"]),
    8: ("Product Development", ["Product Manager", "Product Designer", "R&D Specialist"]),
    9: ("Legal", ["General Counsel", "Corporate Lawyer", "Paralegal"])
}


def generate_employee_data(num_records):
    data = []
    for i in range(1, num_records + 1):
        emp_id = f"E{i:04d}"
        name = fake.name()
        age = random.randint(22, 60)
        dept_choice = random.choice(list(departments.keys()))
        department, positions = departments[dept_choice]
        position = random.choice(positions)
        salary = round(random.uniform(50000, 150000), 2)
        hire_date = fake.date_between(start_date='-10y', end_date='today')

        data.append([emp_id, name, age, department, position, salary, hire_date])
        print(i, 'done')
    return data


num_records = 1000
employee_data = generate_employee_data(num_records)
columns = ["Employee_ID", "Name", "Age", "Department", "Position", "Salary", "Hire_Date"]
df = pd.DataFrame(employee_data, columns=columns)
df.to_csv('employee_data.csv', index=False)
print("Data generation complete. Saved to employee_data.csv")
