from math import pow
from postfix_calculator import post_calc
from infix_to_postfix import in_to_post
from math_operations import Calculator
from str_to_lst import splitter
from Operators_dict import Operators
from Custom_Exception_Class import *
from  str_to_lst import exceptions_checker
def main():
    try:
        lst = input("Enter your expression: ")
        lst3 = splitter(lst)
        exceptions_checker(lst3)
        print(lst3)
        lst2 = in_to_post(lst3)
        print(lst2)
        result = post_calc(lst2)
        print(f"The result is: {result}")
    except CalculatorError as e:
        print(f"Calculator Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    main()

main()
