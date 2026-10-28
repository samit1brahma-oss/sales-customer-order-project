# Sales Customer Order Management System

A database management project built using **Python 3.13 and MySQL 8** to manage salespeople, customer records, and customer orders. The project demonstrates Python–MySQL connectivity, relational database design, SQL queries, data insertion, and data updates.

## Project Overview

The Sales Customer Order Management System automates the creation and management of a sales database using Python and MySQL. It creates the database and its tables, inserts sample records, retrieves information, filters customers by city, and updates salesperson incentives.

## Features

- **Database Creation:** Automatically creates the `sales_customer_order_project` database if it does not exist.
- **Table Management:** Creates tables for Salespeople, Customers, and Orders.
- **Data Insertion:** Inserts sample records for 10 salespeople, 7 customers, and 9 orders.
- **Data Retrieval:** Displays salesperson, customer, and order records.
- **Customer Filtering:** Retrieves customers from London, Bengaluru, Paris, and Mumbai.
- **Incentive Updates:** Increases the `comm` value for all salespeople by 1,500.
- **Data Integrity:** Uses primary keys and foreign key constraints to maintain relationships between tables.
- **Transaction Management:** Uses `commit()` to save database changes.
- **Error Handling:** Uses Python's exception-handling mechanism for database operations.

## Technologies Used

- Python 3.13
- MySQL 8
- MySQL Connector/Python
- SQL

## Database Structure

The project contains three relational tables.

### 1. Salespeople

Stores salesperson information.

| Column | Data Type | Description |
|---|---|---|
| `snum` | INT | Primary key |
| `sname` | VARCHAR(50) | Salesperson name |
| `city` | VARCHAR(50) | City |
| `comm` | INT | Commission/incentive value |

### 2. Customers

Stores customer details and their assigned salespeople.

| Column | Data Type | Description |
|---|---|---|
| `cnum` | INT | Primary key |
| `cname` | VARCHAR(50) | Customer name |
| `city` | VARCHAR(50) | Customer city |
| `snum` | INT | Foreign key referencing Salespeople |

### 3. Orders

Stores customer order details.

| Column | Data Type | Description |
|---|---|---|
| `onum` | INT | Primary key |
| `odate` | DATE | Order date |
| `oamount` | INT | Order amount |
| `cnum` | INT | Foreign key referencing Customers |
| `snum` | INT | Foreign key referencing Salespeople |

## Entity Relationship

- One salesperson can be associated with multiple customers.
- One customer can have multiple orders.
- Each order references a customer and a salesperson.

```text
Salespeople
    |
    | snum
    v
Customers
    |
    | cnum
    v
Orders
```

## Prerequisites

Before running the project, install:

1. Python 3.13
2. MySQL Server 8
3. A MySQL account with permission to create databases and tables.

## Installation and Setup

### Step 1: Clone the repository

```bash
git clone <your-github-repository-url>
cd <your-repository-folder>
```

Replace the placeholders with your actual repository URL and folder name.

### Step 2: Install the MySQL connector

```bash
py -3.13 -m pip install mysql-connector-python
```

### Step 3: Configure MySQL credentials

Update the connection settings in your Python script to use your local MySQL username and a password supplied through an environment variable. Do not commit passwords or other secrets to GitHub.

For example, on Windows PowerShell:

```powershell
$env:MYSQL_HOST="localhost"
$env:MYSQL_USER="root"
$env:MYSQL_PASSWORD="your_mysql_password"
```

Modify the Python connection code to read these environment variables before running the project.

### Step 4: Run the project

```bash
py -3.13 "Software Services Customer Order Management Control Project-MySQL 8 & Python 3.13-.py"
```

The script creates the database and tables, inserts sample records, performs SQL operations, and displays the results in the terminal.

## SQL Operations Demonstrated

**Retrieve all salespeople**

```sql
SELECT * FROM Salespeople;
```

**Retrieve customers from selected cities**

```sql
SELECT *
FROM Customers
WHERE city IN ('London', 'Bengaluru', 'Paris', 'Mumbai');
```

**Update salesperson incentives**

```sql
UPDATE Salespeople
SET comm = comm + 1500;
```

**Retrieve all orders**

```sql
SELECT * FROM Orders;
```

## Learning Outcomes

Through this project, I practised:

- Connecting Python applications to MySQL databases.
- Creating relational databases and tables.
- Working with primary keys and foreign keys.
- Inserting and retrieving records using SQL.
- Filtering records using the `WHERE` and `IN` clauses.
- Updating database records.
- Committing transactions and handling database connections.
- Automating database operations using Python.

## Important Notes

- The project uses sample sales, customer, and order records.
- The script uses `INSERT IGNORE` to avoid inserting duplicate primary-key values. Existing records are not automatically refreshed.
- The incentive update runs each time the script executes, so the `comm` values can increase repeatedly.
- Database credentials should be configured securely before the project is published.
- Run this project only against a database you are authorised to modify.

## Author

**Samit Brahma**
*This project was developed for learning and practising Python, MySQL, relational database design, and SQL operations.*
