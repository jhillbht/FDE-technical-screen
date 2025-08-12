"""
FDE Technical Screen - Package Sorting Solution
Thoughtful Automation Robotic Factory Package Dispatcher

Author: AI Assistant
Date: August 12, 2025
Time Allocation: 30 minutes
"""

def sort(width, height, length, mass):
    """
    Sorts packages into appropriate stacks based on volume and mass criteria.
    
    Args:
        width (float): Package width in centimeters
        height (float): Package height in centimeters  
        length (float): Package length in centimeters
        mass (float): Package mass in kilograms
    
    Returns:
        str: Stack name - "STANDARD", "SPECIAL", or "REJECTED"
    
    Rules:
        - BULKY: volume >= 1,000,000 cm³ OR any dimension >= 150 cm
        - HEAVY: mass >= 20 kg
        - REJECTED: both bulky AND heavy
        - SPECIAL: bulky OR heavy (but not both)
        - STANDARD: neither bulky nor heavy
    """
    
    # Input validation with ternary operator
    if not all(isinstance(param, (int, float)) and param >= 0 
               for param in [width, height, length, mass]):
        return "REJECTED"  # Invalid inputs are rejected
    
    # Calculate volume
    volume = width * height * length
    
    # Determine if package is bulky (using ternary operator as required)
    is_bulky = True if (volume >= 1_000_000 or 
                       max(width, height, length) >= 150) else False
    
    # Determine if package is heavy (using ternary operator as required)
    is_heavy = True if mass >= 20 else False
    
    # Package classification logic with ternary operators
    return ("REJECTED" if (is_bulky and is_heavy) else
            "SPECIAL" if (is_bulky or is_heavy) else
            "STANDARD")
