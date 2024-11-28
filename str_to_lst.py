class ExpressionSplitter:
    def __init__(self,expression):
        self.expression=expression
    def splitter(self):
        final_list=[]
        current=""
        for char in self.expression:
            if char.isdigit() or char=="." or(char=="-" and current=="") or(char=="~" and current=="") or(char=="!" and current.isdigit()):
                current+=char
            else:
                if current:
                    final_list.append(current)
                    current=""
                if char!=" ":
                    final_list.append(char)
        final_list.append(current)
        exceptions_checker(final_list)
        return final_list
def exceptions_checker(final_list):
    if final_list==['']:
        raise ValueError("Please enter your exercise")
    for index in range(len(final_list)-1):
        if final_list[index]=="/" and final_list[index+1]=="0":
            raise ZeroDivisionError("You cant divide by zero")





