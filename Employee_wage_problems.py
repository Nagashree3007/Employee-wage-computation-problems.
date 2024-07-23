'''

@Author: Nagashree C R
@Date: 2024-07-22
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-22  
@Title : Simulates employee presence or absence randomly.

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


def main():
        check_presence()


if __name__ == '__main__':
    main()