'''

@Author: Nagashree C R
@Date: 2024-07-22
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-22  
@Title :Computes and saves the total wage for each company.

'''

import random

class Employee:
    def __init__(self, name):
        self.name = name
        self.is_present = False
         
    @staticmethod
    def check_presence():
        """
        Description: Simulates employee presence or absence randomly.
        
        Returns:
            tuple: (presence_message, is_present_flag)
        """
        is_present = random.randint(0, 1)
        if is_present == 0:
            return "Employee is absent.", is_present
        else:
            return "Employee is present.", is_present
    
    @staticmethod
    def calculate_daily_wage(is_present):
        """
        Description: Calculates daily wage based on employee's attendance.
        
        Parameters:
            is_present (int): 0 for absent, 1 for present.
        
        Returns:
            str: Daily wage message.
        """
        if is_present == 0:
            return "Daily wage: 0 rupees."
        else:
            daily_hours = 8  # Assuming 8 hours of work per day
            wage = daily_hours * 20  # Assuming wage rate per hour is 20
            return f"Daily wage: {wage} rupees."
    
    @staticmethod
    def add_part_time_employee(name, is_present):
        """
        Description: Adds a part-time employee and calculates wages.
        
        Parameters:
            name (str): Name of the employee.
            is_present (int): 0 for absent, 1 for present.
        
        Returns:
            str: Confirmation message with total earnings.
            
        """
        if is_present == 1:
            return f"{name} earned 0 rupees. Employee is absent today."
        else:
            part_time = random.randint(0, 1)
            if part_time:
                hours = 4  # Assuming 4 hours of work for part-time employee
            else:
                hours = 8  # Assuming 8 hours of work for Full-time employee
            
            wage = hours * 20  # Assuming wage rate per hour is 20
            if part_time:
                return f"{name} earned {wage} rupees & he/she is Part-time employee."
            else:
                return f"{name} earned {wage} rupees & he/she is Full-time employee."
    
    @staticmethod
    def monthly_wage(name, working_days):
        """
        Description: Calculates monthly wages based on random daily hours worked.
        
        Parameters:
            name (str): Name of the employee.
            working_days (int): Number of working days in a month.
        
        Returns:
            str: Monthly wage message.
        """
        total_days = 0
        total_hours = 0
        for _ in range(working_days):
            is_present = random.randint(0, 1)
            if is_present:
                part_time = random.randint(0, 1)
                if part_time:
                    total_hours += 4
                else:
                    total_hours += 8
                total_days += 1
        
        wage = total_hours * 20  # Assuming wage rate per hour is 20
        return f"The monthly wage for {name} in {total_days} days worked for {total_hours} hours is {wage} rupees."
    
    @staticmethod
    def calculate_hourly_wages(name, max_hours):
        """
        Description: Calculates wages based on total hours worked.
        
        Parameters:
            name (str): Name of the employee.
            max_hours (int): Maximum hours employee can work in a month.
        
        Returns:
            str: Earnings based on hours worked.
        """
        total_hours = 0
        while total_hours < max_hours:
            is_present = random.randint(0, 1)
            if is_present:
                part_time = random.randint(0, 1)
                if part_time:
                    total_hours += 4
                else:
                    total_hours += 8
        wage = total_hours * 20  # Assuming wage rate per hour is 20
        d={}
        d[name]=wage
        return f"The monthly wage for {name} in {total_hours} hours worked is {wage} rupees.",d

class Company:
    def __init__(self, name, wage_per_hr, working_days_per_month, max_working_hours):
        self.name = name
        self.wage_per_hr = wage_per_hr
        self.working_days_per_month = working_days_per_month
        self.max_working_hours = max_working_hours 
    
    def display_menu(self):
        """
        Description: Displays menu options to the user.
        
        Returns:
            int: User's choice.
        """
        print(f"""
        Menu for {self.name}:
        1. Check Employee Presence
        2. Calculate Daily Employee Wage
        3. Add Part-time Employee & Wage
        4. Calculate Monthly Wage
        5. Calculate Hourly Wages
        6.Display company wages details
        """)

        try:
            option = int(input("Enter your choice: "))
            return option
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None
    
    def process_choice(self, option, employee_name):
        """
        Description: Processes user's choice and executes corresponding functionality using match statement.
        
        Parameters:
            option (int): User-selected option from the menu.
            employee_name (str): Name of the employee.
        
        Returns: None
        """
        employee = Employee(employee_name)  # Create an Employee instance for this company

        match option:
            case 1:
                result, is_present = employee.check_presence()
                print(result)
                if is_present==0:
                    return 0
            case 2:
                result, is_present = employee.check_presence()
                print(employee.calculate_daily_wage(is_present))
            case 3:
                result, is_present = employee.check_presence()
                print(employee.add_part_time_employee(employee_name, is_present))
            case 4:
                print(employee.monthly_wage(employee_name, self.working_days_per_month))
            case 5:
                   result,dic=(employee.calculate_hourly_wages(employee_name, self.max_working_hours))
                   print(result)
            case 6:
                result,dic=(employee.calculate_hourly_wages(employee_name, self.max_working_hours))
                print(dic)
            case _:
                print("Invalid input. Please choose a valid option.")
    
    def main(self):
        """
        Description: Main function to run the program for this company.
        
        Returns: None
        """
        employee_name = input(f"Enter the name of the employee for {self.name}: ")
        exit_code = 1
        while exit_code:
            result = self.display_menu()
            if self.process_choice(result, employee_name)==0:
                exit_code=0
            else:
                exit_code = int(input("Do you want to continue (1-yes / 0-No): "))
        
        print(f"Thank you for using the {self.name} Employee Wage Computation Program.")

def main():
    # Define companies with their specific parameters
    company1 = Company("Amazon", 20, 22, 100)
    company2 = Company("Zono", 25, 20, 110)

    # Run the main function for each company
    company1.main()
    company2.main()

if __name__ == '__main__':
    main()