import pandas as pd
from faker import Faker
import random
import mysql.connector
from datetime import datetime, timedelta

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="dashboard",
    port=3306,
)
print("Database is connected successfully")
cursor = conn.cursor()

# Simulate data
fake = Faker()
num_records = 1000

# Function to generate and insert orders
def generate_orders(num_records=1000):
    for _ in range(num_records):
        order_id = fake.uuid4()  # Generate a unique order ID (UUID)
        customer_id = random.randint(1, 100)  # Simulate customer IDs
        product_id = random.randint(1, 50)  # Simulate product IDs
        quantity = random.randint(1, 10)  # Simulate quantity
        price = round(random.uniform(10, 500), 2)  # Simulate price
        total = round(quantity * price, 2)  # Calculate total price
        order_date = fake.date_time_between(start_date="-30d", end_date="now")  # Simulate order date
        
        # Insert data into the orders table
        cursor.execute("""
            INSERT INTO orders (OrderID, CustomerID, ProductID, Quantity, Price, Total, OrderDate)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (str(order_id), customer_id, product_id, quantity, price, total, order_date))
    
    conn.commit()
    print(f"{num_records} orders inserted.")

# Run Data Generation
generate_orders(num_records)

# Close Connection
cursor.close()
conn.close()
