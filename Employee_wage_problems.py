'''

@Author: Nagashree C R
@Date: 2024-07-22
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-22  
@Title :Refactoring the Code to write a Class Method to Compute Employee Wage - Using Class Method and Class.

'''


import random 

class Employee:
    def __init__(self, name):
        self.name = name
        self.is_present = False
    
    def check_presence(self):
        """
        Description: Simulates employee presence or absence randomly.
        
        Returns:
            str: Presence status message.
        """
        self.is_present = random.randint(0, 1)
        if self.is_present == 0:
            return "Employee is absent."
        else:
            return "Employee is present."
    
    def calculate_daily_wage(self):
        """
        Description: Calculates daily wage based on employee's attendance.
        
        Returns:
            str: Daily wage message.
        """
        if self.is_present == 0:
            daily_hours = 0
        else:
            daily_hours = 8  # Assuming 8 hours of work per day
        
        wage = daily_hours * 20  # Assuming wage rate per hour is 20
        return f"Daily wage: {wage} rupees."
    
    def add_part_time_employee(self):
        """
        Description: Adds a part-time employee and calculates wages.
        
        Returns:
            str: Confirmation message with total earnings.
        """
        part_time = random.randint(0, 1)
        
        if part_time and self.is_present:
            hours = 4  # Assuming 4 hours of work for part-time employee
            return f"{self.name} earned {hours * 20} rupees & he/she is Part-time employee."
        elif self.is_present:
            hours = 8  # Assuming 8 hours of work for Full-time employee
            return f"{self.name} earned {hours * 20} rupees he/she is full-time employee."
        else:
            return f"{self.name} earned 0 rupees he/she is absent today."
    
    def monthly_wage(self):
        """
        Description: Calculates monthly wages based on random daily hours worked.
        
        Returns:
            str: Monthly wage message.
        """
        days = hours = 0
        for i in range(20):
            part_time = random.randint(0, 1)
            if part_time:
                days += 1
                hours += 4
            else:
                days += 1
                hours += 8
        
        return f"The monthly wage for 20 days worked for {hours} hours is {hours * 20}"
    
    def calculate_hourly_wages(self):
        """
        Description: Calculates wages based on total hours worked.
        
        Returns:
            str: Earnings based on hours worked.
        """
        days = hours = 0
        while days <20 and hours <= 92:
            part_time = random.randint(0, 1)
            is_present = random.randint(0, 1)
            
            if is_present:
                if part_time:
                    days += 1
                    hours += 4
                else:
                    days += 1
                    hours += 8
        
        return f"The monthly wage for {self.name} in {days} out of 20 days worked for {hours} hours is {hours * 20}"

    def display_menu(self):
        """
        Description: Displays menu options to the user.
        
        Returns:
            int: User's choice.
        """
        print("""
        Menu:
        1. Check Employee Presence
        2. Calculate Daily Employee Wage
        3. Add Part-time Employee & Wage
        4. Calculate Monthly Wage
        5. Calculate Hourly Wages
        """)

        try:
            option = int(input("Enter your choice: "))
            return option
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None
    
    def process_choice(self, option):
        """
        Description: Processes user's choice and executes corresponding functionality using match statement.
        
        Parameters:
            option (int): User-selected option from the menu.
        
        Returns: None
        """
        match option:
            case 1:
                result = self.check_presence()
                print(result)
                if "absent" in result:  # Check if the employee is present
                    return 0  # Exit code 0 to stop the loop
            case 2:
                print(self.calculate_daily_wage())
            case 3:
                print(self.add_part_time_employee())
            case 4:
                print(self.monthly_wage())
            case 5:
                print(self.calculate_hourly_wages())
            case _:
                print("Invalid input. Please choose a valid option.")
    
    def main(self):
        """
        Description: Main function to run the program.
        
        Returns: None
        """
        exit_code = 1
        while exit_code:
            result = self.display_menu()
            if self.process_choice(result)== 0:
                exit_code = 0
            else:
                exit_code = int(input("Do you want to continue (1-yes / 0-No): "))
        
        print("Thank you for using the Employee Wage Computation Program.")


if __name__ == '__main__':
    name = input("Enter the name of the employee: ")
    emp = Employee(name)
    emp.main()
