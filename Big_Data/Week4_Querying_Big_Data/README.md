# Week 4: Unit 4 - Querying Big Data

Welcome to Unit 4! Now that we understand Big Data storage and analytical methods, let's explore how to query these massive datasets to retrieve specific information.

## Challenges in Querying Big Data

Traditional SQL databases can struggle with the volume, velocity, and variety of Big Data. Querying Big Data often involves:
*   **Distributed Data:** Data is spread across multiple machines.
*   **Schema-on-Read:** The structure of the data might be defined when it's read, not when it's written (common in data lakes).
*   **Diverse Data Formats:** Handling structured, semi-structured, and unstructured data.

## Apache Hive and HiveQL

**Apache Hive** is a data warehouse software project built on top of Apache Hadoop for providing data query and analysis. Hive gives an SQL-like interface to query data stored in various databases and file systems that integrate with Hadoop.

*   **HiveQL (HQL):** Hive's query language, which is very similar to SQL. Hive translates HQL queries into MapReduce jobs (or Tez or Spark jobs).
*   **Use Cases:** Batch SQL queries on large datasets, data warehousing, ad-hoc analysis.
*   **How it Works:**
    1.  User submits an HQL query.
    2.  Hive compiler checks syntax and converts the query into a plan.
    3.  The execution engine (e.g., MapReduce, Tez, Spark) runs the jobs on the Hadoop cluster.
    4.  Results are returned to the user.

**Example HQL (Conceptual):**

```sql
-- This is a conceptual HQL example. You'd run this in a Hive environment.

-- Assuming you have a table 'user_logs' with columns 'user_id', 'action', 'timestamp'

-- Count the number of actions per user
SELECT user_id, COUNT(action) as action_count
FROM user_logs
WHERE date_format(timestamp, 'yyyy-MM-dd') = '2023-10-26' -- Example filter
GROUP BY user_id
ORDER BY action_count DESC;
```

## Apache Pig and Pig Latin

**Apache Pig** is a high-level platform for creating programs that run on Apache Hadoop. The language for this platform is called **Pig Latin**.

*   **Pig Latin:** A data flow language. It allows users to describe how data from one or more inputs should be read, processed, and then stored to one or more outputs in parallel.
*   **Use Cases:** ETL (Extract, Transform, Load) pipelines, complex data transformations that are harder to express in SQL.
*   **How it Works:** Pig Latin scripts are translated into MapReduce jobs.

**Example Pig Latin (Conceptual):**

```pig
-- This is a conceptual Pig Latin example.

-- Load data (e.g., from HDFS)
-- Format: user_id, age, city
users = LOAD 'user_data.txt' USING PigStorage(',') AS (user_id:chararray, age:int, city:chararray);

-- Filter users older than 30
older_users = FILTER users BY age > 30;

-- Group by city
grouped_by_city = GROUP older_users BY city;

-- Count users per city
user_count_by_city = FOREACH grouped_by_city GENERATE group AS city, COUNT(older_users) AS count;

-- Store the results
STORE user_count_by_city INTO 'output/city_counts' USING PigStorage(',');
```

## Querying NoSQL Databases

Querying NoSQL databases varies significantly based on the database type (Key-Value, Document, Column-Family, Graph).

1.  **Key-Value Stores (e.g., Redis):**
    *   Typically queried by key. `GET <key>` retrieves a value.
    *   Some offer more advanced querying on secondary indexes if supported.

2.  **Document Databases (e.g., MongoDB):**
    *   Query languages allow filtering based on fields within documents, often using JSON-like query structures.
    *   **Example MongoDB Query (Conceptual):**
        ```javascript
        // Find users with age greater than 25 in a 'users' collection
        db.users.find({ age: { $gt: 25 } })
        ```

3.  **Column-Family Stores (e.g., Cassandra):**
    *   Often use a query language like CQL (Cassandra Query Language), which is similar to SQL but designed for column-family data models.
    *   Queries are typically optimized for specific partition keys.

4.  **Graph Databases (e.g., Neo4j):**
    *   Use specialized query languages like Cypher (for Neo4j) to traverse relationships.
    *   **Example Cypher Query (Conceptual):**
        ```cypher
        // Find friends of a user named 'Alice'
        MATCH (person:Person {name: 'Alice'})-[:FRIENDS_WITH]->(friend:Person)
        RETURN friend.name;
        ```

## Python Example: Querying Data (Simulated with CSV and sqlite3)

For learning purposes, we can simulate querying structured data using Python's built-in `sqlite3` module with data from a CSV file. This demonstrates SQL-like querying concepts without needing a full Big Data setup.

First, let's imagine we have a CSV file named `sample_sales_data.csv`:
```csv
OrderID,Product,Category,Amount,Date
1,Laptop,Electronics,1200,2023-01-15
2,Mouse,Electronics,25,2023-01-15
3,Keyboard,Electronics,75,2023-01-16
4,Book,Literature,20,2023-01-16
5,Tablet,Electronics,300,2023-01-17
6,Book,Children,15,2023-01-17
7,Monitor,Electronics,400,2023-01-18
8,Book,Literature,22,2023-01-18
```

Now, the Python code to load and query this data:

```python
import sqlite3
import csv
import os # For file handling

# --- Setup: Create a dummy CSV file for the example ---
def create_dummy_csv(filename="sample_sales_data.csv"):
    data = [
        ["OrderID", "Product", "Category", "Amount", "Date"],
        [1, "Laptop", "Electronics", 1200, "2023-01-15"],
        [2, "Mouse", "Electronics", 25, "2023-01-15"],
        [3, "Keyboard", "Electronics", 75, "2023-01-16"],
        [4, "Book", "Literature", 20, "2023-01-16"],
        [5, "Tablet", "Electronics", 300, "2023-01-17"],
        [6, "Book", "Children", 15, "2023-01-17"],
        [7, "Monitor", "Electronics", 400, "2023-01-18"],
        [8, "Book", "Literature", 22, "2023-01-18"]
    ]
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    print(f"'{filename}' created for the example.")

# --- Main Querying Logic ---
def query_sales_data(db_name=":memory:", csv_filename="sample_sales_data.csv"):
    # Create the dummy CSV if it doesn't exist
    if not os.path.exists(csv_filename):
        create_dummy_csv(csv_filename)

    conn = sqlite3.connect(db_name)  # Use ":memory:" for an in-memory database
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        OrderID INTEGER PRIMARY KEY,
        Product TEXT,
        Category TEXT,
        Amount REAL,
        Date TEXT
    )
    ''')
    print("Table 'sales' created or already exists.")

    # Load data from CSV into the table
    # For simplicity, we'll clear the table first if it has data from a previous run (in-memory DB resets anyway)
    cursor.execute("DELETE FROM sales;")
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute('''
            INSERT INTO sales (OrderID, Product, Category, Amount, Date)
            VALUES (?, ?, ?, ?, ?)
            ''', (row['OrderID'], row['Product'], row['Category'], row['Amount'], row['Date']))
    conn.commit()
    print(f"Data loaded from '{csv_filename}' into 'sales' table.")

    # --- Example Queries ---

    # 1. Select all sales from 'Electronics' category
    print("\n--- Query 1: All sales from 'Electronics' ---")
    cursor.execute("SELECT * FROM sales WHERE Category = ?", ('Electronics',))
    for row in cursor.fetchall():
        print(row)

    # 2. Calculate total sales amount per category
    print("\n--- Query 2: Total sales amount per category ---")
    cursor.execute('''
    SELECT Category, SUM(Amount) as TotalAmount
    FROM sales
    GROUP BY Category
    ORDER BY TotalAmount DESC
    ''')
    for row in cursor.fetchall():
        print(row)

    # 3. Find sales with Amount > 100
    print("\n--- Query 3: Sales with Amount > 100 ---")
    cursor.execute("SELECT Product, Amount FROM sales WHERE Amount > ?", (100,))
    for row in cursor.fetchall():
        print(row)

    conn.close()

    # Clean up the dummy CSV file
    if os.path.exists(csv_filename):
        os.remove(csv_filename)
        print(f"Cleaned up '{csv_filename}'.")

# To run the example:
# query_sales_data()
```

This Python example uses `sqlite3` to demonstrate SQL querying on a small, structured dataset. In a Big Data context, tools like Hive, Presto, or Spark SQL would be used to run similar SQL-like queries on data stored in distributed file systems like HDFS or cloud storage.

Next week, we'll discuss the critical aspects of Big Data and privacy.
