class Stack:
    def __init__(self):
        self.items=[]
    def push(self,value):
        """push item into the stack"""
        self.items.append(value)
    def pop(self):
        """return the top value in the stack and return it"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from  empty stack")
    def is_empty(self):
        """return if the stack is empty"""
        return len(self.items)==0
    def peek(self):
        """return the top item of the stack"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peak from empty stack")
    def size(self):
        """return the size of the stack"""
        return len(self.items)