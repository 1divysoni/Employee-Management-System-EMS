import pandas as pd
import ANSI_codes as Text
from Pdf_Maker import *

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 6000)


def list_all_employees(df):
    return df


def list_employees_by_department(df, department):
    return df[df['Department'] == department]


def average_salary_by_department(df):
    return df.groupby('Department')['Salary'].mean().reset_index()


def employees_hired_within_date_range(df, start_date, end_date):
    df['Hire_Date'] = pd.to_datetime(df['Hire_Date'])
    return df[(df['Hire_Date'] >= start_date) & (df['Hire_Date'] <= end_date)]


def top_n_highest_paid_employees(df):
    df_sorted = df.sort_values(by='Salary', ascending=False)
    top_100_highest_paid = df_sorted.head(100)
    return top_100_highest_paid.to_string(col_space=10)


def main(file_path):
    df = pd.read_csv(file_path)
    while True:
        print(f'{Text.UNDERLINE}{Text.CYAN}Select Command To Generate Report{Text.RESET}')
        print('\t1-List of all employees.\n\t2-List of employees in a specific department.'
              '\n\t3-Average salary by department.\n\t4-Employees hired within a certain date range.\n\t'
              '5-Top highest-paid employees.\n\t6-Exit')
        command = int(input())
        if command == 1:
            print(f'{Text.BLUE}All Employees:{Text.RESET}')
            Case1 = list_all_employees(df)
            print(Case1)
            while True:
                print(f'{Text.YELLOW}You Want To Download PDF File For It? [Y/N]{Text.RESET}')
                check = input()
                if check == 'Y':
                    print(f'Wait Process In Progress')
                    create_pdf_from_csv(Case1, 'All Employees Data.pdf', title="All Employees Data")
                    print(f'{Text.GREEN}PDF Downloaded Successfully{Text.RESET}')
                    break
                elif check == "N":
                    break
                else:
                    print(f'{Text.RED}Select Correct Command{Text.RESET}')
        elif command == 2:
            while True:
                print(f'{Text.UNDERLINE}{Text.CYAN}Select Department{Text.RESET}\n\t1-Human Resources (HR).\n\t2-Finance.\n\t3-Marketing.\n\t'
                      '4-Sales.\n\t5-Information Technology (IT).\n\t'
                      '6-Operations.\n\t7-Customer Service.\n\t8-Product Development.\n\t9-Legal.')
                commandF = int(input())
                if commandF == 1:
                    department = 'Human Resources (HR)'
                    break
                elif commandF == 2:
                    department = 'Finance'
                    break
                elif commandF == 3:
                    department = 'Marketing'
                    break
                elif commandF == 4:
                    department = 'Sales'
                    break
                elif commandF == 5:
                    department = 'Information Technology (IT)'
                    break
                elif commandF == 6:
                    department = 'Operations'
                    break
                elif commandF == 7:
                    department = 'Customer Service'
                    break
                elif commandF == 8:
                    department = 'Product Development'
                    break
                elif commandF == 9:
                    department = 'Legal'
                    break
                else:
                    print('Select Correct Command')
            print(f'{Text.BLUE}\nEmployees in {department} Department:{Text.RESET}')
            Case2 = list_employees_by_department(df, department)
            print(Case2)
            while True:
                print(f'{Text.YELLOW}You Want To Download PDF File For It? [Y/N]{Text.RESET}')
                check = input()
                if check == 'Y':
                    print(f'Wait Process In Progress')
                    create_pdf_from_csv(Case2, f'{department} Data.pdf', title=f"{department} Data")
                    print(f'{Text.GREEN}PDF Downloaded Successfully{Text.RESET}')
                    break
                elif check == "N":
                    break
                else:
                    print(f'{Text.RED}Select Correct Command{Text.RESET}')
        elif command == 3:
            print(f"{Text.BLUE}\nAverage Salary by Department:{Text.RESET}")
            Case3 = average_salary_by_department(df)
            print(Case3)
            while True:
                print(f'{Text.YELLOW}You Want To Download PDF File For It? [Y/N]{Text.RESET}')
                check = input()
                if check == 'Y':
                    print(f'Wait Process In Progress')
                    create_pdf_from_csv(Case3, 'Average Salary Data.pdf', title="Average Salary Data")
                    print(f'{Text.GREEN}PDF Downloaded Successfully{Text.RESET}')
                    break
                elif check == "N":
                    break
                else:
                    print(f'{Text.RED}Select Correct Command{Text.RESET}')
        elif command == 4:
            print('Enter Date If YYYY-MM-DD Formate')
            start_date = input('Enter Start Date')
            end_date = input('Enter End Date')
            print(f"{Text.BLUE}\nEmployees hired between {start_date} and {end_date}:{Text.RESET}")
            Case4 = employees_hired_within_date_range(df, start_date, end_date)
            print(Case4)
            while True:
                print(f'{Text.YELLOW}You Want To Download PDF File For It? [Y/N]{Text.RESET}')
                check = input()
                if check == 'Y':
                    print(f'Wait Process In Progress')
                    create_pdf_from_csv(Case4, f'Employees hired between {start_date} and {end_date}.pdf', title=f'Employees hired between {start_date} and {end_date}')
                    print(f'{Text.GREEN}PDF Downloaded Successfully{Text.RESET}')
                    break
                elif check == "N":
                    break
                else:
                    print(f'{Text.RED}Select Correct Command{Text.RESET}')
        elif command == 5:
            print(f"{Text.BLUE}\nTop Highest Paid Employees:{Text.RESET}")
            Case5 = top_n_highest_paid_employees(df)
            print(Case5)
            while True:
                print(f'{Text.YELLOW}You Want To Download PDF File For It? [Y/N]{Text.RESET}')
                check = input()
                if check == 'Y':
                    print(f'Wait Process In Progress')
                    create_pdf_from_csv(Case5, 'Top Highest Paid Employees.pdf', title="Top Highest Paid Employees")
                    print(f'{Text.GREEN}PDF Downloaded Successfully{Text.RESET}')
                    break
                elif check == "N":
                    break
                else:
                    print(f'{Text.RED}Select Correct Command{Text.RESET}')
        elif command == 6:
            print('Report System Terminated')
            break
        else:
            print(f'{Text.RED}Select Correct Command{Text.RESET}')


if __name__ == "__main__":
    print('ERROR')
