from Exercise_KTLT.Ex58.Employee58 import Employee


def enter_employee():
    last_name=input("Enter last name:")
    first_name=input("Enter first name:")
    number=int(input("Enter number of products:"))
    print("-"*30)
    return Employee(last_name,first_name,number)
def menu():
    while True:
        e1 = enter_employee()
        e2 = enter_employee()
        print("Salary of Employee 1:", e1.get_salary())
        print("Salary of Employee 2:", e2.get_salary())
        # cach 1
        if e1.IsHigher(e2):
            print("The salary/number of products of Employee 1 is higher than that of Employee 2")
        else:
            print("The salary/number of products of Employee 1 is lower (or equal) than that of Employee 2")
        # cach 2
        if e1.get_salary() > e2.get_salary():
            print("The salary/number of products of Employee 1 is higher than that of Employee 2")
        elif e1.get_salary() == e2.get_salary():
            print("The salary/number of products of Employee 1 is equal to that of Employee 2")
        else:
            print("The salary/number of products of Employee 1 is lower than that of Employee 2")
        ask = input("\nDo you want to continue? (y/n): ")
        if ask != 'y':
            print("Thank you for using the program. Goodbye!")
            break