from sympy import *

init_printing(use_unicode=True)
print("Choose an option:")
print("1. Reduced Roe Echelon")
print("2. Determinant of a matrix")
print("3. Invert a Matrix")
menu_choice = input()


def get_matrix():
    print("Enter in the number of rows")
    numrows = input()
    print("Enter in the number of columns")
    numcols = input()
    print("Enter in all elements by row separated by a space")

    usr = input()
    split_array = usr.split(' ')
    row1 = []
    for i in range(0, len(split_array)):
        row1.append(int(split_array[i]))

    a = Matrix(int(numrows), int(numcols), row1)
    return a


if menu_choice == "1":
    B = get_matrix()
    print("Original Matrix")
    pprint(B)
    print("Rref of Matrix")
    pprint(B.rref())
elif menu_choice == "2":
    B = get_matrix()
    print("Original Matrix")
    pprint(B)
    print("Determinant:")
    pprint(B.det())
elif menu_choice == "3":
    B = get_matrix()
    print("Original Matrix")
    pprint(B)
    print("Inverse:")
    pprint(B**-1)
