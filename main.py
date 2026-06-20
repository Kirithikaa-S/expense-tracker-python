from db import connection

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Search Expense")
    print("6. Category Summary")
    print("7. Monthly Summary")
    print("8. Exit")

    choice = input("Enter your choice: ")

    cursor = connection.cursor()

    # ADD EXPENSE
    if choice == "1":

        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))
        description = input("Enter Description: ")

        query = """
        INSERT INTO expenses
        (expense_date, category, amount, description)
        VALUES
        (CURDATE(), %s, %s, %s)
        """

        values = (category, amount, description)

        cursor.execute(query, values)
        connection.commit()

        print("Expense Added Successfully!")

    # VIEW EXPENSES
    elif choice == "2":

        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()

        if not expenses:
            print("No Expenses Found")

        else:
            for expense in expenses:
                print("\nID:", expense[0])
                print("Date:", expense[1])
                print("Category:", expense[2])
                print("Amount:", expense[3])
                print("Description:", expense[4])
                print("-" * 30)

    # UPDATE EXPENSE
    elif choice == "3":

        expense_id = input("Enter Expense ID: ")

        category = input("Enter New Category: ")
        amount = float(input("Enter New Amount: "))
        description = input("Enter New Description: ")

        query = """
        UPDATE expenses
        SET category=%s,
            amount=%s,
            description=%s
        WHERE id=%s
        """

        values = (category, amount, description, expense_id)

        cursor.execute(query, values)
        connection.commit()

        print("Expense Updated Successfully!")

    # DELETE EXPENSE
    elif choice == "4":

        expense_id = input("Enter Expense ID to Delete: ")

        query = "DELETE FROM expenses WHERE id=%s"

        cursor.execute(query, (expense_id,))
        connection.commit()

        print("Expense Deleted Successfully!")

    # SEARCH EXPENSE
    elif choice == "5":

        category = input("Enter Category to Search: ")

        query = """
        SELECT * FROM expenses
        WHERE category=%s
        """

        cursor.execute(query, (category,))
        expenses = cursor.fetchall()

        if not expenses:
            print("No Expenses Found")

        else:
            for expense in expenses:
                print("\nID:", expense[0])
                print("Date:", expense[1])
                print("Category:", expense[2])
                print("Amount:", expense[3])
                print("Description:", expense[4])
                print("-" * 30)

            
    elif choice == "6":

        query = """
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        """

        cursor.execute(query)

        result = cursor.fetchall()

        print("\n===== CATEGORY SUMMARY =====")

        for row in result:
            print(f"{row[0]} : ₹{row[1]}")

    # MONTHLY SUMMARY
    elif choice == "7":

        month = input("Enter Month (1-12): ")

        query = """
        SELECT SUM(amount)
        FROM expenses
        WHERE MONTH(expense_date)=%s
        """

        cursor.execute(query, (month,))
        total = cursor.fetchone()

        print("\nTotal Expense:", total[0] if total[0] else 0)


    # EXIT
    elif choice == "8":

        print("Thank You!")
        break

    else:
        print("Invalid Choice")