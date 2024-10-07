from datetime import datetime
from Operations import *
from GenerateReports import main
import ANSI_codes as Text


if __name__ == '__main__':
    print(f'{Text.CYAN}Welcome Sir/Mam.\nEmployee Management System{Text.RESET}')
    Data_file_path = 'Employee_Data.csv'
    while True:
        print(f'{Text.UNDERLINE}{Text.MAGENTA}Select Command TO Execute.{Text.RESET}\n\t1-Add Employee.'
              '\n\t2-Update Employee.\n\t3-Get Record Of Employee.\n\t4-Delete Employee.'
              '\n\t5-Generate Employee Report.\n\t6-Exit')
        command = int(input())
        if command == 1:
            Id = generate_employee_id(Data_file_path)
            print(f'New Employee Id-{Id}')
            Emp_Name = input('Enter Name Of Employee')
            Emp_Age = int(input('Enter Age Of Employee'))
            DepartmentPosition = department_position()
            Emp_Department = DepartmentPosition[0]
            Emp_Position = DepartmentPosition[1]
            Emp_Salary = int(input('Enter Salary Of Employee'))
            now = datetime.now()
            Emp_Hire_Date = now.date()
            print(f'Hire_Date is {Emp_Hire_Date}')
            if new_employee(Data_file_path, Id, Emp_Name, Emp_Age, Emp_Department,
                            Emp_Position, Emp_Salary, Emp_Hire_Date):
                print(f'{Text.GREEN}Employee Added Successfully. ID={Id}, Name={Emp_Name}{Text.RESET}')
            else:
                print(f'{Text.RED}Error{Text.RESET}')
        elif command == 2:
            Emp_id = input('Enter Employee Id For Update.')
            while True:
                print(f'{Text.UNDERLINE}{Text.MAGENTA}Select What You Want To Update Employee Id-{Emp_id}{Text.RESET}')
                print('\t1-Update Name.\n\t2-Update Age.\n\t3-Update Department And Position.'
                      '\n\t4-Update Salary.\n\t5-Exit.')
                ch = int(input())
                if ch == 1:
                    column_name = 'Name'
                    update_content = input('Enter New Name')
                    if update_employee(Data_file_path, Emp_id, column_name, update_content):
                        print(f'{Text.GREEN}Data Updated Successfully{Text.RESET}')
                    else:
                        print(f'{Text.RED}Error{Text.RESET}')
                elif ch == 2:
                    column_name = 'Age'
                    update_content = int(input('Enter New Age'))
                    if update_employee(Data_file_path, Emp_id, column_name, update_content):
                        print(f'{Text.GREEN}Data Updated Successfully')
                    else:
                        print(f'{Text.RED}Error{Text.RESET}')
                elif ch == 3:
                    DepartmentPosition = department_position()
                    column_name = 'Department'
                    update_content = DepartmentPosition[0]
                    if update_employee(Data_file_path, Emp_id, column_name, update_content):
                        column_name1 = 'Position'
                        update_content1 = DepartmentPosition[1]
                        if update_employee(Data_file_path, Emp_id, column_name1, update_content1):
                            print(f'{Text.GREEN}Data Updated Successfully{Text.RESET}')
                        else:
                            print(f'{Text.RED}Error Cant Update Position{Text.RESET}')
                    else:
                        print(f'{Text.RED}Error Cant Update Department{Text.RESET}')
                elif ch == 4:
                    column_name = 'Salary'
                    update_content = int(input('Enter New Salary'))
                    if update_employee(Data_file_path, Emp_id, column_name, update_content):
                        print(f'{Text.GREEN}Data Updated Successfully{Text.RESET}')
                    else:
                        print(f'{Text.RED}Error{Text.RESET}')
                elif ch == 5:
                    print('Update System Terminated!')
                    break
                else:
                    print(f'{Text.RED}Select Correct Command{Text.RESET}')
        elif command == 3:
            Emp_id = input('Enter Employee Id To Get Data.')
            EMP_DATA = get_employee_data(Data_file_path, Emp_id)
            if EMP_DATA:
                print(f'\tId-{EMP_DATA[0]}\n\tName-{EMP_DATA[1]}\n\tAge-{EMP_DATA[2]}\n\tDepartment-{EMP_DATA[3]}'
                      f'\n\tPosition-{EMP_DATA[4]}\n\tSalary-{EMP_DATA[5]}\n\tHire Date-{EMP_DATA[6]}\n')
            else:
                print(f'{Text.RED}Employee Not Found With {Emp_id} ID{Text.RESET}')
        elif command == 4:
            Emp_id = input('Enter Employee Id To Delete.')
            while True:
                print(f'{Text.YELLOW}You Want To Delete {Emp_id}? (Y/N){Text.RESET}')
                command_second = input()
                if command_second == 'Y':
                    delete_employee(Data_file_path, Emp_id)
                    print(f'{Text.GREEN}{Emp_id} deleted Successfully{Text.RESET}')
                    break
                elif command_second == 'N':
                    print(f'{Text.YELLOW}Delete Request Rejected{Text.RESET}')
                    break
                else:
                    print(f'{Text.RED}Select Correct Command{Text.RESET}')
        elif command == 5:
            main(Data_file_path)
        elif command == 6:
            print('System Terminated!')
            break
        else:
            print(f'{Text.RED}Select Correct Command{Text.RESET}')
# -------------------------------------------------------END------------------------------------------------------------
