"""
CTEC 121
Matthew Bly
Module 3 Lab 1
Code for Module 3 Lab 1
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    '''
    # conditional expressions

    # literal
    print("\nboolean literals")
    print(True)
    print(False)
    print(type(True))
    print()

    # relational operators
    print("Relation operators")
    print("3 < 5", 3 < 5)
    print("3 <= 3", 3 <= 3)
    print("3 == 3", 3 == 3)
    print("3 >= 5", 3 >= 5)
    print("3 != 5", 3 != 5)
    print()

    # using variables
    x = 3
    y = 5
    print("Using variables")
    print('x:', x, 'y:', y)
    print('x < y', x < y)
    print('x != y', x != y)
    print()

    # simple if statement
    print('x:', x, 'y:', y)
    if x < y:
        print('x < y')

    if x > y:
        print('x > y')

    print('end simple if example')
    print()

    # if/else statement
    print(' if/else statement')
    print('x:', x, 'y:', y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")

    x = 6
    print('x:', x, 'y:', y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")

    print('end if/else example')
    print()

    # exercise 3-1
    print('Exercise')
    for i in range(1,11):
        if (i % 2) == 0:
            ouputString = "even"
        else:
            ouputString = "odd"
        print(i, ouputString)
    print()

    # alphabetize names
    name = 'Bill'
    firstLetterOfName = 'B'

    print('Multi-way if example')
    if firstLetterOfName == 'A':
        print("A")
    elif firstLetterOfName == 'B':
        print("B")
    elif firstLetterOfName == 'C':
        print("C")
    # ...
    elif firstLetterOfName == 'Y':
        print("Y")
    else:       # default case: name starts with z
        print("Z")
    print()
    '''
    try:
        print(4/0)
    except:
        print("\nThere was a divide by zero error. Exiting\n")
        exit()

main()    