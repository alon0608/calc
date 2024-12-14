from lib2to3.fixer_util import String
from os import remove
from Custom_Exception_Class import TwoOrMoreTildas, MissingOperandError,NegativeFactorial,NegativeFactorialSum,NegativeSqrt
import Operators_dict
from Operators_dict import Operators


def minus_checker(lst):
    count=0
    number=1
    index=0
    tilda_check=0
    while index<len(lst) :
        if index==len(lst)-1 and lst[index]=="~":
            raise MissingOperandError("~")
        elif lst[index]=="~"  and (lst[index+1] in("-","~")or lst[index+1] not in Operators):
            if tilda_check==1:
                raise TwoOrMoreTildas()
            tilda_check=1
            lst.pop(index)
        elif lst[index] in Operators and count==0 and index!=0 and lst[index] not in ("!","#") :
            count+=1
            index+=1
        elif lst[index]=="-" :
            number*=-1
            count+=1
            lst.pop(index)
        elif isinstance(lst[index],int) or isinstance(lst[index],float)or lst[index].isdigit():
            lst[index] = int(lst[index])
            lst[index] *= number
            number=1
            count=0
            if tilda_check:
                if index!=len(lst)-1 and lst[index+1]=="!":
                    raise NegativeFactorial ()
                if index!=len(lst)-1 and lst[index+1]=="#":
                    raise NegativeFactorialSum()
                if index<len(lst)-2 and lst[index+1]=="^" and 0 < float(lst[index + 2]) < 1:
                    raise NegativeSqrt()
                lst[index]*=-1
                tilda_check=0
            lst[index]=str(lst[index])
            index+=1
        else:
            index+=1
    return lst
