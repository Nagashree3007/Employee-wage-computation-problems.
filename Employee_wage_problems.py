'''

@Author: Nagashree C R
@Date: 2024-07-22
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-22  
@Title : calculates monthly wages.

'''


import random



# UC1: Method to determine if employee is present or absent

def check_presence():
    """
        
    Description: Simulates employee presence or absence randomly.
    
    Parameters:None
    
    Returns:
        is_present: 0 for absent, 1 for present.
            
    """
        
        
    is_present = random.randint(0, 1)
    if is_present == 0:
        return "Employee is absent.",is_present
    else:
        return "Employee is present.",is_present

result,is_present=check_presence()
# UC2: Method to calculate daily wages based on attendance

def calculate_daily_wage(is_present):
    """
        
        Description: Calculates daily wage based on employee's attendance.
        
        parameters:
            is_present (int): 0 for absent, 1 for present.
        
        Returns:
            wage: Daily wage of the employee Assuming 8 hours of work per day.
            
    """
    
    if is_present == 0:
        daily_hours = 0
        wage=0
    else:
        daily_hours = 8  # Assuming 8 hours of work per day
        wage = daily_hours * 20  # Assuming wage rate per hour is 20
        
    return f"Daily wage: {wage} rupees."


# UC3: Method to add part-time employee and calculate wages

def add_part_time_employee(name):
    """
    
       Description:Adds a part-time employee and calculates wages.
       
       parameters:
            name (str): Name of the part-time employee.
        
        Returns:
            str: Confirmation message with total earnings.
            
    """
    
    part_time=random.randint(0, 1)
    if part_time and is_present:
        hours = 4  # Assuming 4  hours of work for part-time employee
        wages=(hours*20)
        return f"{name} earned {wages} rupees & he/she is Part-time employee."
    elif is_present:
        hours = 8  # Assuming 8 hours of work for Full-time employee
        wages=(hours*20)
        return f"{name} earned {wages} rupees he/she is full-time employee."
    else:
        wages=0
        return f"{name} earned {wages} rupees he is absent today"
    
#UC5: Function to calculate monthly wages

def monthly_wage():
    
    """
    
    
     Description: Give the monthly wage for a company
    
     Parameters:None
    
     Return: wages of a person based on part time or full time working hours
    
    
    """
    days=hours=0
    for _ in range(20):
        part_time=random.randint(0, 1)
        if part_time:
            days+=1
            hours+=4
        else :
            days+=1
            hours+=8
    return f"the monthly wage for employee in  20 days worked for {hours} hours is {hours*20}"
                
    
    
# UC4: Function to handle user input and execute corresponding functionality 
def display_menu():
    """
     Description: Give the menu to user and collect the option as an input to perform specific task
    
     Parameters:None
    
     Return: None
    
    """
    print("""
    Menu:
    1. Check Employee Presence
    2. Calculate Daily Employee Wage
    3. Add Part-time Employee & Wage
    4.calculate the monthly wage
    """)

    try:
        option = int(input("Enter your choice: "))
        return option
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


# Function to handle user input and execute corresponding functionality
def process_choice(option):
    """
    Description: Processes user choice and calls appropriate methods using match statement.
    
    Parameters:
        option (int): User-selected option from the menu.
    
    Return: None
    
    """
    
    match option:
        case 1:
            result,is_present =check_presence()
            print(result)
        case 2:
            result,is_present =check_presence()
            print(calculate_daily_wage(is_present))
        case 3:
            name = input("Enter the name of the employee: ")
            result = add_part_time_employee(name)
            print(result)
            
        case 4:
            print(monthly_wage())
            
        case _:
            print("Invalid input. Please choose a valid option.")


def main():
    exit_code=1
    while exit_code:
        result=display_menu()
        process_choice(result)
        exit_code=int(input("Do YOu Want To Comtinue....??(1-yes)or (0-No)"))
    print("Thank you for using the Employee Wage Computation Program.")
        
    

if __name__ == '__main__':
    main()