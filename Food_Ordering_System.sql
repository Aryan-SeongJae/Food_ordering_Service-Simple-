show databases ;

create database Food_Ordering_System;

use Food_Ordering_System;

create table Customer(
    Customer_ID int primary key,
    Customer_Name varchar(50),
    Customer_Address varchar(100),
    Customer_Phone varchar(15),
    Customer_Email varchar(50),
    Customer_Payment_method varchar(50),
    Customer_Payment_status varchar(50),
    Customer_Order_ID varchar(50),
    Date_of_order date
);

show tables;

create table Employee(
    Employee_ID int primary key,
    Employee_Name varchar(50),
    Employee_Gender varchar(10),
    Employee_Age int(2),
    Employee_Phone varchar(15)

);

show tables;


create table Food(
    Food_ID int primary key,
    Food_Name varchar(50),
    Food_Size varchar(50),
    Food_Price int(5)
);

show tables;

create table Food_Order(
    Order_ID int primary key,
    Customer_ID int,
    Employee_ID int,
    Food_ID int,
    Food_Quantity int,
    Total_Price int
);

show tables;



INSERT INTO Customer VALUES
                         (1, 'Alice Johnson', '123 Main St', '1234567890', 'alice@example.com', 'Credit Card', 'Paid', 'ORD001', '2023-12-01'),
                         (2, 'Bob Smith', '456 Elm St', '9876543210', 'bob@example.com', 'Cash', 'Unpaid', 'ORD002', '2023-12-02'),
                         (3, 'Charlie Brown', '789 Oak St', '1231231234', 'charlie@example.com', 'Debit Card', 'Paid', 'ORD003', '2023-12-03'),
                         (4, 'Diana Prince', '321 Maple St', '4564564567', 'diana@example.com', 'Credit Card', 'Paid', 'ORD004', '2023-12-04'),
                         (5, 'Ethan Hunt', '654 Pine St', '7897897890', 'ethan@example.com', 'Cash', 'Unpaid', 'ORD005', '2023-12-05');



INSERT INTO Employee VALUES
    (1, 'John Doe', 'Male', 30, '1234567890'),
    (2, 'Jane Smith', 'Female', 28, '9876543210'),
    (3, 'Michael Clark', 'Male', 35, '1231231234'),
    (4, 'Sarah Connor', 'Female', 32, '4564564567'),
    (5, 'Bruce Wayne', 'Male', 40, '7897897890');



INSERT INTO Food VALUES
    (1, 'Burger', 'Medium', 150),
    (2, 'Pizza', 'Large', 300),
    (3, 'Pasta', 'Regular', 200),
    (4, 'Salad', 'Small', 100),
    (5, 'Sandwich', 'Medium', 120);


INSERT INTO Food_Order VALUES
    (1, 1, 1, 1, 2, 300),
    (2, 2, 2, 2, 1, 300),
    (3, 3, 3, 3, 3, 600),
    (4, 4, 4, 4, 1, 100),
    (5, 5, 5, 5, 2, 240);
