'''

@Author: Nagashree C R
@Date: 2024-07-22
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-22  
@Title : Calculates daily wage based on employee's attendance.

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
        print("Employee is absent.")
    else:
        print("Employee is present.")
    return is_present


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



def main():
    is_present = check_presence()
    print(calculate_daily_wage(is_present))

if __name__ == '__main__':
    main()