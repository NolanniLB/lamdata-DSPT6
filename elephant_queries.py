import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DB_Name = os.getenv('DB_Name')
DB_User = os.getenv('DB_User')
DB_Pass = os.getenv('DB_Pass')
DB_Host = os.getenv('DB_Host')

## Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_Name, user=DB_User,
                        password=DB_Pass, host=DB_Host)

### A "cursor", a structure to iterate over db records to perform queries
cursor = conn.cursor()

### An example query
cursor.execute('SELECT * from test_table;')

### Note - nothing happened yet! We need to actually *fetch* from the cursor
results = cursor.fetchall()
print(results)