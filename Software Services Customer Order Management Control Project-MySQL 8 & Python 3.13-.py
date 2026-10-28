import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jmfxk12986!"
    )

    if mydb.is_connected():
        cursor = mydb.cursor()

        # Create new database
        cursor.execute("CREATE DATABASE IF NOT EXISTS sales_customer_order_project")
        print("Database 'sales_customer_order_project' created successfully!")

        # Connect to the new database
        mydb.database = "sales_customer_order_project"

        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Salespeople (
            snum INT PRIMARY KEY,
            sname VARCHAR(50),
            city VARCHAR(50),
            comm INT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            cnum INT PRIMARY KEY,
            cname VARCHAR(50),
            city VARCHAR(50),
            snum INT,
            FOREIGN KEY (snum) REFERENCES Salespeople(snum)
        )
        """)


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            onum INT PRIMARY KEY,
            odate DATE,
            oamount INT,
            cnum INT,
            snum INT,
            FOREIGN KEY (cnum) REFERENCES Customers(cnum),
            FOREIGN KEY (snum) REFERENCES Salespeople(snum)
        )
        """)


        print("Tables created successfully!")

        # 1) Add 10 salespeople
        cursor.execute("""
        INSERT IGNORE INTO Salespeople (snum, sname, city, comm) VALUES
        (1001, 'John', 'London', 12),
        (1002, 'Ravi', 'Bengaluru', 15),
        (1003, 'Marie', 'Paris', 10),
        (1004, 'Amit', 'Mumbai', 11),
        (1005, 'Sophia', 'London', 9),
        (1006, 'David', 'Paris', 13),
        (1007, 'Kiran', 'Bengaluru', 14),
        (1008, 'Emma', 'Mumbai', 8),
        (1009, 'Alex', 'London', 16),
        (1010, 'Nina', 'Paris', 12)
        """)

        mydb.commit()
        print("10 Salespeople added.")


        # 2) Add 7 customers
        cursor.execute("""
        INSERT IGNORE INTO Customers (cnum, cname, city, snum) VALUES
        (2001, 'Alice', 'London', 1001),
        (2002, 'Amit', 'Mumbai', 1002),
        (2003, 'Claire', 'Paris', 1003),
        (2004, 'Rohan', 'Bengaluru', 1002),
        (2005, 'Meera', 'London', 1005),
        (2006, 'George', 'Paris', 1006),
        (2007, 'Sita', 'Mumbai', 1008)
        """)

        mydb.commit()
        print("7 Customers added.")

        # 3) Display all salespeople
        print("\nSalespeople Records:")
        cursor.execute("SELECT * FROM Salespeople")
        for row in cursor.fetchall():
            print(row)

        # 4) Increase incentive by Rs. 1500 for all salespeople
        cursor.execute("UPDATE Salespeople SET comm = comm + 1500")
        mydb.commit()
        print("\nIncentives increased by Rs. 1500.")

        # 5) Display all customers
        print("\nCustomer Records:")
        cursor.execute("SELECT * FROM Customers")
        for row in cursor.fetchall():
            print(row)

        # 6) Display customers in London, Bengaluru, Paris, Mumbai
        print("\nCustomers in London, Bengaluru, Paris, Mumbai:")
        cursor.execute("SELECT * FROM Customers WHERE city IN ('London','Bengaluru','Paris','Mumbai')")
        for row in cursor.fetchall():
            print(row)

        # Adding 9 orders
        cursor.execute("""
        INSERT IGNORE INTO Orders (onum, odate, oamount, cnum, snum) VALUES
        (3001, '2026-10-28', 2500, 2001, 1001),
        (3002, '2026-10-28', 1800, 2002, 1002),
        (3003, '2026-10-28', 3200, 2003, 1003),
        (3004, '2026-10-28', 1500, 2004, 1002),
        (3005, '2026-10-28', 2200, 2005, 1005),
        (3006, '2026-10-28', 2700, 2006, 1006),
        (3007, '2026-10-28', 1900, 2007, 1008),
        (3008, '2026-10-28', 3100, 2001, 1001),
        (3009, '2026-10-28', 2800, 2002, 1002)
        """)

        mydb.commit()
        print("9 Orders added in one go.")

        # 7) Displaying all orders
        print("\nOrders Records:")
        cursor.execute("SELECT * FROM Orders")
        for row in cursor.fetchall():
            print(row)


finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("\nMySQL connection closed.")
