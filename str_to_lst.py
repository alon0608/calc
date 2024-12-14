from xmlrpc.client import boolean
from Custom_Exception_Class import *
from Minus_Check import minus_checker
from Operators_dict import Operators

def splitter(expression):
    final_list=[]
    current=""
    decimal_point_count=0
    counter=0
    index=0
    for index,char in enumerate(expression):
        if char.isdigit() or char==".":
            if char==".":
                if index==0 or (not expression[index-1].isdigit() and not char=="."):
                    raise InvalidDecimalPlacementError()
                decimal_point_count+=1
            if decimal_point_count>1:
                raise ConsecutiveDecimalsError()
            current+=char
        else:
            decimal_point_count=0
            if char==" ":
                current=current
            elif current:
                final_list.append(current)
                current=""
            if char!=" ":
                final_list.append(char)


    if current:
        final_list.append(current)
    final_list1=minus_checker(final_list)
    exceptions_checker(final_list)
    return final_list1

def exceptions_checker(final_list):
    if len(final_list)==0:
        raise CalculatorInputError()

    for index in range(len(final_list) - 1):
        if final_list[index] == "/" and final_list[index + 1] == "0":
            raise DivisionByZeroError()

    for char in final_list:
        if not char.find(".") and not char.isdigit() and not char.lstrip("-").rstrip("!").isdigit() and not char.lstrip("-").isdigit() and not char[0].isdigit() and char[0] != "~" and char!="(" and char!=")"and char not in Operators:
            raise IllegalCharacterError(char)


    left_parenthesis = 0
    is_num_between=False
    for char in final_list:
        if char == "(":
            left_parenthesis += 1
        elif char not in ["(",")"]:
            is_num_between=True
        elif char == ")":
            if is_num_between==False:
                raise EmptyParentheses()
            left_parenthesis -= 1
        if left_parenthesis < 0:
            raise ParenthesisMismatchError("Closing parenthesis found before an opening parenthesis.")
    if left_parenthesis > 0:
        raise ParenthesisMismatchError("One or more opening parentheses are not closed.")
    count=0
    op=""
    op2=""
    for char in final_list:
        if  char in["~","!","#"] or char=="-" and count==1 :
            continue
        elif char in Operators and count==0:
            count+=1
            op=char
        elif char in Operators and count>=1:
            count+=1
            op2=char
        else:
            if count>1:
                raise TooMuchOperatorsInARow(op2,op)
            elif count==1:
                count-=1
    if count==1:
        raise MissingOperandError(op)



