PlasmaBloodBank-DBMS

PlasmaBloodBank-DBMS is a Database Management System designed for handling end-to-end operations of a Plasma Blood Bank. This was developed as a course project for the subject Data and Applications.

The system is built using MySQL for database management and Python as the interface layer, allowing users to interact with the database using a CLI-based menu-driven system.

FEATURES
--------
The system provides comprehensive support for plasma blood bank management through the following key functionalities:

Donor & Donation Management:
- Add new donor information with detailed profile
- Record new donations with timestamp and bag details
- Add companion details for donors (e.g., emergency contact)

Plasma Inventory:
- Add new plasma samples to inventory
- View all existing plasma records
- Delete a plasma bag from the system
- Change or update cost of plasma
- Add plasma cost information

Recipient & Transactions:
- Register new recipients
- Record payment transactions
- Link recipients with employees via the receives relation

Staff Management:
- Add a new employee
- View list of supervisors

Reports:
- Display total plasma donated
- Show total plasma donated by blood type

GETTING STARTED
---------------

1. Clone the Repository:
   git clone https://github.com/naqeebahmedkhan-code/PlasmaBloodBank-DBMS.git
   cd PlasmaBloodBank-DBMS

2. Load the MySQL Database:
   Ensure MySQL is installed and running. Then execute the following:
   mysql -u <your-username> -p
   source PlasmaBank.sql;
   This sets up the database schema and inserts sample data.

3. Run the Python Interface:
   python3 PlasmaBank.py
   Ensure required Python packages like mysql-connector-python are installed.

FUNCTIONAL MENU (Python Interface)
----------------------------------
Upon running the Python script, the system displays a menu with these options:

1. Add new donation
2. Add new donor information
3. Add new Plasma
4. Add new recipient
5. Hire a new employee
6. Delete a Plasma sample
7. Change Plasma Cost
8. Total Plasma Donated
9. Total Plasma of given type Donated
10. View Plasma
11. Add Plasma cost
12. Supervisor List
13. Add Transaction Details
14. Logout

All changes are directly reflected in the MySQL database.

TECH STACK
----------
- Database: MySQL
- Backend Scripting: Python 3
- Libraries: mysql-connector-python

TEAM
----
Name                     GitHub Profile
Naqeeb Ahmed Khan       https://github.com/naqeebahmedkhan-code
Mohammed Yaseer         –
Mohammed Rehan Sheikh   –
Nikitha                 –
