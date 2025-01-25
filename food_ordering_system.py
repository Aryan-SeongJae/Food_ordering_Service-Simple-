import os
import platform
import pymysql


mydb = pymysql.connect(host = "localhost", user = "root", passwd = "#Teamwork987", database = "Food_Ordering_System")

mycursor = mydb.cursor()


def Customer () :
    L = []
    print("Welcome to the Food Ordering System")
    Customer_Id = input("Enter your Customer ID: ")
    Customer_name = input("Enter your Name: ")
    Customer_address = input("Enter your Address: ")
    Customer_phone = input("Enter your Phone Number: ")
    Customer_email = input("Enter your Email: ")
    Customer_Order_Id = input("Enter your Order ID: ")
    Date_of_order = input("Enter your Order Date: ")
    Customer_Payment_method = input("Enter your Payment Method: ")
    Customer_Payment_status = input("Enter your Payment Status: ")

    L.append(Customer_Id)
    L.append(Customer_name)
    L.append(Customer_address)
    L.append(Customer_phone)
    L.append(Customer_email)
    L.append(Customer_Payment_method)
    L.append(Customer_Payment_status)
    L.append(Customer_Order_Id)
    L.append(Date_of_order)


    cust = (L)

    sql = ("INSERT INTO Customer (Customer_Id, Customer_name, Customer_address, Customer_phone, Customer_email, Customer_Order_Id, Date_of_order, Customer_Payment_method, Customer_Payment_status) "
           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

    mycursor.execute(sql, cust)
    mydb.commit()

    print("Customer Details Added Successfully")


def Employee():
    L = []
    Employee_Id = input("Enter your Employee ID: ")
    Employee_Name = input("Enter your Name: ")
    Employee_Gender = input("Enter your gender: ")
    Employee_Age = input("Enter your Age: ")
    Employee_Phone = input("Enter your Phone Number: ")

    L.append(Employee_Id)
    L.append(Employee_Name)
    L.append(Employee_Gender)
    L.append(Employee_Age)
    L.append(Employee_Phone)

    emp = (L)

    sql = ("INSERT INTO Employee (Employee_Id, Employee_Name, Employee_Gender, Employee_Age, Employee_Phone) "
              "VALUES (%s, %s, %s, %s, %s)")

    mycursor.execute(sql, emp)
    mydb.commit()

    print("Employee Details Added Successfully")


def Food():
    L = []
    Food_Id = input("Enter your Food ID: ")
    Food_Name = input("Enter your Food Name: ")
    Food_Price = input("Enter the Price: ")
    Food_Category = input("Enter the Category: ")
    Food_Description = input("Enter the Description: ")

    L.append(Food_Id)
    L.append(Food_Name)
    L.append(Food_Price)
    L.append(Food_Category)
    L.append(Food_Description)

    food = (L)

    sql = ("INSERT INTO Food (Food_Id, Food_Name, Food_Price, Food_Category, Food_Description) "
           "VALUES (%s, %s, %s, %s, %s)")

    mycursor.execute(sql, food)
    mydb.commit()

    print("Food Details Added Successfully")


def Order_Food():
    L = []
    Order_Id = input("Enter your Order ID: ")
    Customer_Id = input("Enter your Food ID: ")
    Employee_Id = input("Enter the Quantity: ")
    Food_Id = input("Enter the Total Price: ")
    Food_qty = input("Enter the Quantity: ")
    Total_Price = input("Enter the Total Price: ")

    L.append(Order_Id)
    L.append(Customer_Id)
    L.append(Employee_Id)
    L.append(Food_Id)
    L.append(Food_qty)
    L.append(Total_Price)

    order = (L)

    sql = ("INSERT INTO Order_Food (Order_Id, Customer_Id, Employee_Id, Food_Id, Food_qty, Total_Price) "
           "VALUES (%s, %s, %s, %s, %s, %s)")

    mycursor.execute(sql, order)
    mydb.commit()

    print("Order Details Added Successfully")


def View():
    print("Welcome to the Food Ordering System")
    print("1. Employee")
    print("2. Customer")
    print("3. Food")
    print("4. Ordered Food")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        s = input("Enter the Employee ID or 'ALL' to view all: ")
        if s.lower() == 'all':
            sql = "SELECT * FROM Employee"
            mycursor.execute(sql)
        else:
            rl = (int(s),)
            sql = "SELECT * FROM Employee WHERE Employee_Id = %s"
            mycursor.execute(sql, rl)
        res = mycursor.fetchall()
        for x in res:
            print(x)

    elif ch == 2:
        s = input("Enter the Customer ID or 'ALL' to view all: ")
        if s.lower() == 'all':
            sql = "SELECT * FROM Customer"
            mycursor.execute(sql)
        else:
            rl = (int(s),)
            sql = "SELECT * FROM Customer WHERE Customer_Id = %s"
            mycursor.execute(sql, rl)
        res = mycursor.fetchall()
        for x in res:
            print(x)

    elif ch == 3:
        s = input("Enter the Food ID or 'ALL' to view all: ")
        if s.lower() == 'all':
            sql = "SELECT * FROM Food"
            mycursor.execute(sql)
        else:
            rl = (int(s),)
            sql = "SELECT * FROM Food WHERE Food_Id = %s"
            mycursor.execute(sql, rl)
        res = mycursor.fetchall()
        for x in res:
            print(x)

    elif ch == 4:
        s = input("Enter the Order ID or 'ALL' to view all: ")
        if s.lower() == 'all':
            sql = "SELECT * FROM Order_Food"
            mycursor.execute(sql)
        else:
            rl = (int(s),)
            sql = "SELECT * FROM Order_Food WHERE Order_Id = %s"
            mycursor.execute(sql, rl)
        res = mycursor.fetchall()
        for x in res:
            print(x)



def MenuSet():
    print("Welcome to the Food Ordering System")
    print("1. Add Employee")
    print("2. Add Customer")
    print("3. Add Food")
    print("4. Add Ordered Food")
    print("5. View")

    try:
        user_input = int(input("Enter your choice: "))

    except ValueError:
        exit("\nHy! That's not a number")

    else:
        print("\n")
        if user_input == 1:
            Employee()

        elif user_input == 2:
            Customer()

        elif user_input == 3:
            Food()

        elif user_input == 4:
            Order_Food()

        elif user_input == 5:
            View()

        else:
            print("Enter a valid number")




def RunAgain():
    runAgn = input("\nwant to run again Y/n: ")
    while runAgn.lower() == 'y':
        if platform.system() == "Windows":
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        MenuSet()
        runAgn = input("\nwant to run again Y/n: ")
        print("Goodbye! Have a nice day")
        exit()


MenuSet()
RunAgain()













