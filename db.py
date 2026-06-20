import mysql.connector
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Skirithi@3186",
        database="expense_tracker"
    )

    print("Database Connected Successfully")

except Exception as e:
    print("Database Connection Error:", e)