from stack import Stack
from str_to_lst import ExpressionSplitter

def main():
    lst=ExpressionSplitter("-5!+6")
    print(lst.splitter())
main()