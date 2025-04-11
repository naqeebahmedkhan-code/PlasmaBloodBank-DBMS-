import pymysql
from datetime import datetime, date

# Global connection and cursor
con = pymysql.connect(host="localhost", user="root", password="your_password", database="your_database", cursorclass=pymysql.cursors.DictCursor)
cur = con.cursor()

def executeQuery(query, values=None):
    cur.execute(query, values)
    con.commit()

def excepting(e):
    con.rollback()
    print("Failed to insert/delete/update/find database")
    print(">>>>>>>>>>>>>", e)

def calculateAge(birthDate): 
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def UpdateBloodCost():
    try:
        bloodId = int(input("Enter Plasma_bag_number whose cost is to be Updated: "))
        new_cost = int(input("Enter updated cost: "))
        
        query_check = "SELECT COUNT(*) AS cnt FROM BLOOD WHERE Plasma_bag_number = %s"
        cur.execute(query_check, (bloodId,))
        val = cur.fetchone()['cnt']
        
        if val == 0:
            print("Input plasma_bag_number does not exist. Please enter valid input")
            return
        
        query_update = "UPDATE BLOOD_COST SET cost = %s WHERE plasma_bag_number = %s"
        executeQuery(query_update, (new_cost, bloodId))
        print("Blood cost updated successfully")
        
    except Exception as e:
        excepting(e)

def deleteBlood():
    try:
        delete_id = int(input("Enter Plasma bag number to be deleted: "))
        query_check = "SELECT COUNT(*) AS cnt FROM BLOOD WHERE plasma_bag_number = %s"
        cur.execute(query_check, (delete_id,))
        val = cur.fetchone()['cnt']
        
        if val != 0:
            query_delete = "DELETE FROM BLOOD WHERE plasma_bag_number = %s"
            executeQuery(query_delete, (delete_id,))
            print("Deleted successfully")
        else:
            print("Input plasma_bag_number does not exist. Please enter a valid plasma_bag_number")

    except Exception as e:
        excepting(e)

def addBlood():
    try:
        print("Enter new Plasma details: ")
        plasma_bag_number = int(input("plasma_bag_number: "))
        blood_type = input("Plasma blood_type: ")
        blood_amount = int(input("blood_amount: "))
        platelets_count = float(input("platelets_count (in thousands): "))

        query = "INSERT INTO BLOOD(plasma_bag_number, blood_type, blood_amount, platelets_count) VALUES (%s, %s, %s, %s)"
        executeQuery(query, (plasma_bag_number, blood_type, blood_amount, platelets_count))
        print("Inserted Into Database")

    except Exception as e:
        excepting(e)

def addPaymentTnx():
    try:
        print("Enter transaction details: ")
        rec_id = int(input("rec_id: "))
        payment_amt = int(input("Payment Amount: "))
        payment_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("Time of Txn =", payment_time)
        query = "INSERT INTO PAYMENT_TRANSACTION(rec_id, payment_amt, payment_time) VALUES (%s, %s, %s)"
        executeQuery(query, (rec_id, payment_amt, payment_time))
        print("Inserted Into Database")

    except Exception as e:
        excepting(e)

def addDonorInfo():
    try:
        print("Enter new donor's details: ")
        name = input("Name (Fname Lname): ").split()
        fname, lname = name[0], name[1]
        donor_id = int(input("Donor_id: "))
        blood_type = input("Plasma Blood_type: ")
        dob_input = input("DOB (YYYY-MM-DD): ")
        dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
        age = calculateAge(dob)
        print("Age:", age, "years")
        sex = input("Sex: ")
        phone_no = input("phone_no: ")
        address = input("Address: ")

        query = """INSERT INTO DONOR_INFO(donor_id, blood_type, phone_no, dOB, age, sex, fname, lname, address)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        executeQuery(query, (donor_id, blood_type, phone_no, dob.strftime("%Y-%m-%d"), age, sex, fname, lname, address))
        print("Inserted Into Database")

    except Exception as e:
        excepting(e)

def addRecipient():
    try:
        print("Enter new recipient's details: ")
        name = input("Name (Fname Lname): ").split()
        fname, lname = name[0], name[1]
        rec_id = int(input("Rec_id: "))
        blood_type = input("Plasma Blood_type: ")
        quantity_needed = int(input("Quantity_needed: "))
        date_of_request = input("Date of request (YYYY-MM-DD): ")
        dob_input = input("DOB (YYYY-MM-DD): ")
        dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
        age = calculateAge(dob)
        print("Age:", age, "years")
        sex = input("Sex: ")
        address = input("Address: ")

        query = """INSERT INTO RECIPIENT(rec_id, blood_type, quantity_needed, date_of_request, fname, lname, dOB, sex, age, address)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        executeQuery(query, (rec_id, blood_type, quantity_needed, date_of_request, fname, lname, dob.strftime("%Y-%m-%d"), sex, age, address))
        print("Inserted Into Database")

    except Exception as e:
        excepting(e)

def addDonor():
    try:
        print("Enter new donation details: ")
        donor_id = int(input("Donor-id: "))
        date_of_donation = input("Date of donation (YYYY-MM-DD): ")

        query = "INSERT INTO DONORS(donor_id, date_of_donation) VALUES (%s, %s)"
        executeQuery(query, (donor_id, date_of_donation))
        print("Inserted Into Database")

    except Exception as e:
        excepting(e)

def Supervisors():
    try:
        supervisor_name = input("Enter supervisor name: ")
        query = "SELECT * FROM STAFF WHERE supervisor = %s"
        cur.execute(query, (supervisor_name,))
        rows = cur.fetchall()

        if rows:
            print("Employees under Supervisor", supervisor_name, "are:")
            for emp in rows:
                print(f"ID: {emp['emp_id']}, Name: {emp['fname']} {emp['lname']}, Address: {emp['address1']}, Phone: {emp['phone_no']}, Salary: {emp['salary']}")
        else:
            print("No staff found under this supervisor.")

    except Exception as e:
        excepting(e)

def hireStaff():
    try:
        print("Enter new staff member's details: ")
        emp_id = int(input("emp_id: "))
        fname = input("Name: ")
        supervisor = input("supervisor: ")
        address = input("address: ")
        phone_no = int(input("phone_no: "))
        salary = int(input("salary: "))

        query = "INSERT INTO STAFF(emp_id, fname, supervisor, address1, phone_no, salary) VALUES (%s, %s, %s, %s, %s, %s)"
        executeQuery(query, (emp_id, fname, supervisor, address, phone_no, salary))
        print("Inserted Into Database")

    except Exception as e:
        excepting(e)

def TotalBlood():
    try:
        query = "SELECT SUM(blood_amount) AS total FROM BLOOD"
        cur.execute(query)
        row = cur.fetchone()
        print("The total Plasma available is:", row["total"])
    except Exception as e:
        excepting(e)

def TotalBloodOfGiven():
    try:
        blood_type = input("Enter the Plasma type: ")
        query = "SELECT SUM(blood_amount) AS total FROM BLOOD WHERE blood_type = %s"
        cur.execute(query, (blood_type,))
        row = cur.fetchone()
        print(f"The total available Plasma of type {blood_type} is:", row["total"])
    except Exception as e:
        excepting(e)

def ViewBlood():
    try:
        query = "SELECT * FROM BLOOD"
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        excepting(e)

def AddBloodCost():
    try:
        plasma_bag_number = int(input("Plasma bag number: "))
        cost = int(input("Plasma Cost: "))
        query = "INSERT INTO BLOOD_COST(plasma_bag_number, cost) VALUES (%s, %s)"
        executeQuery(query, (plasma_bag_number, cost))
        print("Inserted Into Database")
    except Exception as e:
        excepting(e)

# Always close the connection at end (example purpose only)
# con.close()
