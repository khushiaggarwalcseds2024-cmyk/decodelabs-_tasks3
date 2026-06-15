# Project 3: Data Analysis Using Python and SQLite

## Project Overview

This project demonstrates how to load data from an Excel file into a SQLite database using Python. After storing the data in the database, SQL queries are executed to perform basic data analysis such as counting records, viewing sample data, calculating averages, and grouping data by category.

---

## Objectives

* Load Excel data using Pandas
* Create a SQLite database
* Store dataset in a database table
* Execute SQL queries using Python
* Retrieve and analyze data
* Perform aggregation operations
* Display query results

---

## Technologies Used

* Python
* Pandas
* SQLite3
* OpenPyXL
* Visual Studio Code

---

## Required Libraries

Install the required packages:

```bash
pip install pandas openpyxl
```

> Note: SQLite3 is included with Python by default and does not require separate installation.

---

## Project Structure

```text
Project Folder/
│
├── Dataset for Data Analytics (3).xlsx
├── project3.py
├── project3.db
└── README.md
```

---

## Features

### 1. Load Excel Dataset

The dataset is loaded using Pandas:

```python
df = pd.read_excel("Dataset for Data Analytics (3).xlsx")
```

### 2. Create SQLite Database

A database named:

```text
project3.db
```

is created automatically.

### 3. Store Data into Database

The dataset is stored in a table named:

```text
sales
```

using:

```python
df.to_sql("sales", conn, if_exists="replace", index=False)
```

### 4. Total Records Count

Displays the total number of records available in the dataset.

SQL Query:

```sql
SELECT COUNT(*) FROM sales;
```

### 5. Display Top 10 Records

Shows the first 10 records from the table.

SQL Query:

```sql
SELECT * FROM sales LIMIT 10;
```

### 6. Average Total Price

If a `TotalPrice` column exists, the script calculates the average value.

SQL Query:

```sql
SELECT AVG(TotalPrice) FROM sales;
```

### 7. Category-wise Analysis

If a `Category` column exists, records are grouped by category and counted.

SQL Query:

```sql
SELECT Category, COUNT(*) AS Total
FROM sales
GROUP BY Category
ORDER BY Total DESC;
```

---

## How to Run

### Step 1: Open VS Code

Open the project folder in Visual Studio Code.

### Step 2: Install Required Libraries

```bash
pip install pandas openpyxl
```

### Step 3: Run the Script

```bash
python project3.py
```

---

## Expected Output

The terminal displays:

* Total Number of Records
* First 10 Records
* Average Total Price (if available)
* Category-wise Record Counts (if available)

Example:

```text
===== TOTAL RECORDS =====
(500,)

===== TOP 10 RECORDS =====
...

===== AVG TOTAL PRICE =====
(2450.75,)

===== GROUP BY CATEGORY =====
...
```

---

## Learning Outcomes

After completing this project, you will learn:

* Reading Excel files using Pandas
* Creating SQLite databases
* Importing data into SQL tables
* Running SQL queries from Python
* Data aggregation and grouping
* Database-driven data analysis

---

## Author

Khushi Aggarwal

---

## Project Type

Data Analytics Project | Python | SQLite Database | SQL Query Analysis
Yeh **Project 3 (Python + SQLite Database Analysis)** ke liye README.md content hai:

# Project 3: Data Analysis Using Python and SQLite

## Project Overview

This project demonstrates how to load data from an Excel file into a SQLite database using Python. After storing the data in the database, SQL queries are executed to perform basic data analysis such as counting records, viewing sample data, calculating averages, and grouping data by category.

---

## Objectives

* Load Excel data using Pandas
* Create a SQLite database
* Store dataset in a database table
* Execute SQL queries using Python
* Retrieve and analyze data
* Perform aggregation operations
* Display query results

---

## Technologies Used

* Python
* Pandas
* SQLite3
* OpenPyXL
* Visual Studio Code

---

## Required Libraries

Install the required packages:

```bash
pip install pandas openpyxl
```

> Note: SQLite3 is included with Python by default and does not require separate installation.

---

## Project Structure

```text
Project Folder/
│
├── Dataset for Data Analytics (3).xlsx
├── project3.py
├── project3.db
└── README.md
```

---

## Features

### 1. Load Excel Dataset

The dataset is loaded using Pandas:

```python
df = pd.read_excel("Dataset for Data Analytics (3).xlsx")
```

### 2. Create SQLite Database

A database named:

```text
project3.db
```

is created automatically.

### 3. Store Data into Database

The dataset is stored in a table named:

```text
sales
```

using:

```python
df.to_sql("sales", conn, if_exists="replace", index=False)
```

### 4. Total Records Count

Displays the total number of records available in the dataset.

SQL Query:

```sql
SELECT COUNT(*) FROM sales;
```

### 5. Display Top 10 Records

Shows the first 10 records from the table.

SQL Query:

```sql
SELECT * FROM sales LIMIT 10;
```

### 6. Average Total Price

If a `TotalPrice` column exists, the script calculates the average value.

SQL Query:

```sql
SELECT AVG(TotalPrice) FROM sales;
```

### 7. Category-wise Analysis

If a `Category` column exists, records are grouped by category and counted.

SQL Query:

```sql
SELECT Category, COUNT(*) AS Total
FROM sales
GROUP BY Category
ORDER BY Total DESC;
```

---

## How to Run

### Step 1: Open VS Code

Open the project folder in Visual Studio Code.

### Step 2: Install Required Libraries

```bash
pip install pandas openpyxl
```

### Step 3: Run the Script

```bash
python project3.py
```

---

## Expected Output

The terminal displays:

* Total Number of Records
* First 10 Records
* Average Total Price (if available)
* Category-wise Record Counts (if available)

Example:

```text
===== TOTAL RECORDS =====
(500,)

===== TOP 10 RECORDS =====
...

===== AVG TOTAL PRICE =====
(2450.75,)

===== GROUP BY CATEGORY =====
...
```

---

## Learning Outcomes

After completing this project, you will learn:

* Reading Excel files using Pandas
* Creating SQLite databases
* Importing data into SQL tables
* Running SQL queries from Python
* Data aggregation and grouping
* Database-driven data analysis

---

## Author

Khushi Aggarwal

---

## Project Type

Data Analytics Project | Python | SQLite Database | SQL Query Analysis

**Suggested File Names:**

* Python Script → `project3.py`
* Database File → `project3.db`
* Documentation → `README.md`
