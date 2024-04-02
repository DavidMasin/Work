import os
import sys

def calculator(num1,operator,num2):
    if(operator=='+'):
        return int(num1)+int(num2)
    elif operator=='-':
        return int(num1)-int(num2)
    elif operator == '*':
        return int(num1) * int(num2)
    elif operator == '/':
        return int(num1)/int(num2)
    return -1

def main():
    print(sys.argv)
    homework = sys.argv[1]
    solution = sys.argv[2]
    with open(homework,'r') as FILE_HOMEWORK:
        for line in FILE_HOMEWORK:
            list1 = line.split(" ")
            result = calculator(list1[0],list1[1],list1[2])
            with open(solution,'a') as FILE_SOLUTIONS:
                FILE_SOLUTIONS.write(str(result) + "\n")


main()