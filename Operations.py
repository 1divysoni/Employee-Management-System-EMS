import pandas as pd
import uuid
import hashlib
import ANSI_codes as Text


def new_employee(file_path, emp_id, name, age, department, position, salary, hire_date):
    try:
        df = pd.read_csv(file_path)
        new_row = pd.DataFrame({'Employee_ID': [emp_id], 'Name': [name], 'Age': [age], 'Department': [department],
                                'Position': [position], 'Salary': [salary], 'Hire_Date': [hire_date]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(file_path, index=False)
        return True
    except Exception as e:
        return e


def delete_employee(file_path, emp_id):
    try:
        df = pd.read_csv(file_path)
        condition = (df['Employee_ID'] == emp_id)
        df = df[~condition]
        df.to_csv(file_path, index=False)
        return True
    except Exception as e:
        return e


def get_employee_data(file_path, emp_id):
    try:
        df = pd.read_csv(file_path)
        filtered_df = df[df['Employee_ID'] == emp_id]
        data = []
        if not filtered_df.empty:
             data.append(filtered_df['Employee_ID'].values[0])
             data.append(filtered_df['Name'].values[0])
             data.append(filtered_df['Age'].values[0])
             data.append(filtered_df['Department'].values[0])
             data.append(filtered_df['Position'].values[0])
             data.append(filtered_df['Salary'].values[0])
             data.append(filtered_df['Hire_Date'].values[0])
             return data
        else:
            print("Number not found in the Data.")
    except Exception as e:
        return e


def update_employee(file_path, emp_id, coloum_name, update_content):
    try:
        df = pd.read_csv(file_path)
        condition = (df['Employee_ID'] == emp_id)
        df.loc[condition, coloum_name] = update_content
        df.to_csv(file_path, index=False)
        return True
    except Exception as e:
        return e


def generate_employee_id(file_path, length=10):
    df = pd.read_csv(file_path)
    Employee_ids = set(df['Employee_ID'])
    while True:
        new_uuid = uuid.uuid4()
        new_id = hashlib.sha256(str(new_uuid).encode()).hexdigest()[:length]
        if new_id not in Employee_ids:
            return new_id


def department_position():
    while True:
        print(f'{Text.UNDERLINE}{Text.MAGENTA}Select Department Of Employee{Text.RESET}')
        print('\t1-Human Resources (HR).\n\t2-Finance.\n\t3-Marketing.\n\t4-Sales.'
              '\n\t5-Information Technology (IT).\n\t6-Operations.\n\t7-Customer Service.'
              '\n\t8-Product Development.\n\t9-Legal.')
        command_second = int(input())
        if command_second == 1:
            Emp_Department = 'Human Resources'
            while True:
                print(f'{Text.UNDERLINE}{Text.MAGENTA}Select Position Of Employee{Text.RESET}')
                print('\t1-Human Resources Manager.\n\t2-Recruiter.\n\t3-Human Resources Specialist')
                CH1 = int(input())
                if CH1 == 1:
                    Emp_Position = 'Human Resources Manager'
                    break
                elif CH1 == 2:
                    Emp_Position = 'Recruiter'
                    break
                elif CH1 == 3:
                    Emp_Position = 'Human Resources Specialist'
                    break
                else:
                    print('Select Correct Position Of Employee')
            break
        elif command_second == 2:
            Emp_Department = 'Finance'
            while True:
                print(f'{Text.UNDERLINE}{Text.MAGENTA}Select Position Of Employee{Text.RESET}')
                print('\t1-Chief Financial Officer (CFO).\n\t2-Accountant.\n\t3-Financial Analyst')
                CH2 = int(input())
                if CH2 == 1:
                    Emp_Position = 'Chief Financial Officer (CFO)'
                    break
                elif CH2 == 2:
                    Emp_Position = 'Accountant'
                    break
                elif CH2 == 3:
                    Emp_Position = 'Financial Analyst'
                    break
                else:
                    print(f'{Text.RED}Select Correct Position Of Employee{Text.RESET}')
            break
        elif command_second == 3:
            Emp_Department = 'Marketing'
            while True:
                print(f'{Text.UNDERLINE}{Text.MAGENTA}Select Position Of Employee{Text.RESET}')
                print('\t1-Marketing Manager.\n\t2-Content Creator.\n\t3-SEO Specialist')
                CH3 = int(input())
                if CH3 == 1:
                    Emp_Position = 'Marketing Manager'
                    break
                elif CH3 == 2:
                    Emp_Position = 'Content Creator'
                    break
                elif CH3 == 3:
                    Emp_Position = 'SEO Specialist'
                    break
                else:
                    print(f'{Text.RED}Select Correct Position Of Employee{Text.RESET}')
            break
        elif command_second == 4:
            Emp_Department = 'Sales'
            while True:
                print(f'{Text.UNDERLINE}{Text.MAGENTA}Select Position Of Employee{Text.RESET}')
                print('\t1-Sales Manager.\n\t2-Sales Representative.\n\t3-Account Manager')
                CH4 = int(input())
                if CH4 == 1:
                    Emp_Position = 'Sales Manager'
                    break
                elif CH4 == 2:
                    Emp_Position = 'Sales Representative'
                    break
                elif CH4 == 3:
                    Emp_Position = 'Account Manager'
                    break
                else:
                    print(f'{Text.RED}Select Correct Position Of Employee{Text.RESET}')
            break
        elif command_second == 5:
            Emp_Department = 'Information Technology (IT)'
            while True:
                print(f'{Text.UNDERLINE}{Text.MAGENTA}Select Position Of Employee{Text.RESET}')
                print('\t1-Information Technology IT Manager.\n\t2-Network Administrator.\n\t3-Software Developer')
                CH5 = int(input())
                if CH5 == 1:
                    Emp_Position = 'Information Technology Manager'
                    break
                elif CH5 == 2:
                    Emp_Position = 'Network Administrator'
                    break
                elif CH5 == 3:
                    Emp_Position = 'Software Developer'
                    break
                else:
                    print(f'{Text.RED}Select Correct Position Of Employee{Text.RESET}')
            break
        elif command_second == 6:
            Emp_Department = 'Operations'
            while True:
                print(f'{Text.UNDERLINE}{Text.MAGENTA}Select Position Of Employee{Text.RESET}')
                print('\t1-Operations Manager.\n\t2-Logistics Coordinator.\n\t3-Quality Assurance Specialist')
                CH6 = int(input())
                if CH6 == 1:
                    Emp_Position = 'Operations Manager'
                    break
                elif CH6 == 2:
                    Emp_Position = 'Logistics Coordinator'
                    break
                elif CH6 == 3:
                    Emp_Position = 'Quality Assurance Specialist'
                    break
                else:
                    print(f'{Text.RED}Select Correct Position Of Employee{Text.RESET}')
            break
        elif command_second == 7:
            Emp_Department = 'Customer Service'
            while True:
                print(f'{Text.UNDERLINE}{Text.MAGENTA}Select Position Of Employee{Text.RESET}')
                print('\t1-Customer Service Manager.\n\t2-Customer Service Representative.'
                      '\n\t3-Technical Support Specialist')
                CH7 = int(input())
                if CH7 == 1:
                    Emp_Position = 'Customer Service Manager'
                    break
                elif CH7 == 2:
                    Emp_Position = 'Customer Service Representative'
                    break
                elif CH7 == 3:
                    Emp_Position = 'Technical Support Specialist'
                    break
                else:
                    print(f'{Text.RED}Select Correct Position Of Employee{Text.RESET}')
            break
        elif command_second == 8:
            Emp_Department = 'Product Development'
            while True:
                print(f'{Text.UNDERLINE}{Text.MAGENTA}Select Position Of Employee{Text.RESET}')
                print('\t1-Product Manager.\n\t2-Product Designer.'
                      '\n\t3-R&D Specialist')
                CH8 = int(input())
                if CH8 == 1:
                    Emp_Position = 'Product Manager'
                    break
                elif CH8 == 2:
                    Emp_Position = 'Product Designer'
                    break
                elif CH8 == 3:
                    Emp_Position = 'R&D Specialist'
                    break
                else:
                    print(f'{Text.RED}Select Correct Position Of Employee{Text.RESET}')
            break
        elif command_second == 9:
            Emp_Department = 'Legal'
            while True:
                print(f'{Text.UNDERLINE}{Text.MAGENTA}Select Position Of Employee{Text.RESET}')
                print('\t1-General Counsel.\n\t2-Corporate Lawyer.\n\t3-Paralegal')
                CH9 = int(input())
                if CH9 == 1:
                    Emp_Position = 'General Counsel'
                    break
                elif CH9 == 2:
                    Emp_Position = 'Corporate Lawyer'
                    break
                elif CH9 == 3:
                    Emp_Position = 'Paralegal'
                    break
                else:
                    print(f'{Text.RED}Select Correct Position Of Employee{Text.RESET}')
            break
        else:
            print(f'{Text.RED}Select Correct Department Of Employee{Text.RESET}')
    return [Emp_Department, Emp_Position]


if __name__ == "__main__":
    print('ERROR')
