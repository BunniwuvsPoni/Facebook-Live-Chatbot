import sqlite3

db = r".\Exploration\learning-sqlite3.db"

# Connect to sqlite db
connection = sqlite3.connect(db)

print(connection.total_changes)

# Create cursor
cursor = connection.cursor()

# # Create Table
# cursor.execute("CREATE TABLE test (id INTERGER, name TEXT)")

# # Insert values
# cursor.execute("INSERT INTO test VALUES (1,'Apple')")
# cursor.execute("INSERT INTO test VALUES (2,'Banana')")
# cursor.execute("INSERT INTO test VALUES (3,'Cherry')")

# # Commit changes
# connection.commit()

# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table in tables:
    print(table[0])

# Read data
cursor.execute("SELECT * FROM test")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close connection
from contextlib import closing

with closing(sqlite3.connect(db)) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()
        print(rows)