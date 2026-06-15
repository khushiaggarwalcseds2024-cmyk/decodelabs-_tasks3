import pandas as pd
import sqlite3

# Excel file load
df = pd.read_excel("Dataset for Data Analytics (3).xlsx")

# SQLite database create
conn = sqlite3.connect("project3.db")

# Data table mein save
df.to_sql("sales", conn, if_exists="replace", index=False)

cursor = conn.cursor()

print("\n===== TOTAL RECORDS =====")
query = "SELECT COUNT(*) FROM sales"
print(cursor.execute(query).fetchone())

print("\n===== TOP 10 RECORDS =====")
query = "SELECT * FROM sales LIMIT 10"
print(pd.read_sql(query, conn))

# Agar TotalPrice column hai
try:
    print("\n===== AVG TOTAL PRICE =====")
    query = "SELECT AVG(TotalPrice) FROM sales"
    print(cursor.execute(query).fetchone())
except:
    pass

# Agar Category column hai
try:
    print("\n===== GROUP BY CATEGORY =====")
    query = """
    SELECT Category, COUNT(*) as Total
    FROM sales
    GROUP BY Category
    ORDER BY Total DESC
    """
    print(pd.read_sql(query, conn))
except:
    pass

conn.close()

print("\nProject 3 Completed Successfully!")