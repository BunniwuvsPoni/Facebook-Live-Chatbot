import sqlite3

connection = sqlite3.connect(".\Exploration\learning-sqlite3.db")

print(connection.total_changes)