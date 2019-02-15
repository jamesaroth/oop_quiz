import csv
import sqlite3
import schema

schema.create_schema()
conn = sqlite3.connect('tsla.db')
c = conn.cursor()
filename= "tsla.csv"
with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    # emp_dict = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO stock (Date, Open, High, Low, Close, Adj_Close, Volume) VALUES (?, ?, ?, ?, ?, ?, ?)", row)
    for row in c.execute("SELECT * FROM stock"):
        print(row)