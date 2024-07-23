'''

@Author: Nagashree C R
@Date: 2024-07-22
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-22  
@Title : Adds a part-time employee and calculates wages.

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

is_present=check_presence()
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
    
    
def main():
    name = input('Enter the Name of Employee: ')
    result = add_part_time_employee(name)
    print(result)

if __name__ == '__main__':
    main()