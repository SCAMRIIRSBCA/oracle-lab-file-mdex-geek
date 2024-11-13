import sqlite3
conn = sqlite3.connect('bite.db')

cursor = conn.cursor()


def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                        CustomerID INT PRIMARY KEY,
                        Name VARCHAR(100),
                        Phone VARCHAR(15) UNIQUE,
                        Email VARCHAR(100)
                    );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Bikes (
                        BikeID INT PRIMARY KEY,
                        RegistrationNumber VARCHAR(15) UNIQUE,
                        Model VARCHAR(50),
                        Year INT,
                        CustomerID INT,
                        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
                    );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Appointments (
                        AppointmentID INT PRIMARY KEY,
                        BikeID INT,
                        AppointmentDate DATE,
                        AppointmentStatus TEXT DEFAULT 'Pending',
                        Description TEXT,
                        FOREIGN KEY (BikeID) REFERENCES Bikes(BikeID),
                        CHECK (AppointmentStatus IN ('Pending', 'In-Progress', 'Completed'))
                    );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS ServiceHistory (
                        ServiceID INTEGER PRIMARY KEY,
                        AppointmentID INT,
                        ServiceDate DATE,
                        Cost DECIMAL(10, 2),
                        Remarks TEXT,
                        FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
                    );''')
    conn.commit()
    print("Tables created successfully.")

def add_customer(customer_id, name, phone, email):
    cursor.execute("INSERT INTO Customers (CustomerID, Name, Phone, Email) VALUES (?, ?, ?, ?);",
                   (customer_id, name, phone, email))
    conn.commit()
    print("Customer added successfully.")

def view_customers():
    cursor.execute("SELECT * FROM Customers;")
    for row in cursor.fetchall():
        print(row)

def add_bike(bike_id, reg_number, model, year, customer_id):
    cursor.execute("INSERT INTO Bikes (BikeID, RegistrationNumber, Model, Year, CustomerID) VALUES (?, ?, ?, ?, ?);",
                   (bike_id, reg_number, model, year, customer_id))
    conn.commit()
    print("Bike added successfully.")

def view_bikes():
    cursor.execute("SELECT * FROM Bikes;")
    for row in cursor.fetchall():
        print(row)

def add_appointment(appointment_id, bike_id, date, status, description):
    cursor.execute("INSERT INTO Appointments (AppointmentID, BikeID, AppointmentDate, AppointmentStatus, Description) VALUES (?, ?, ?, ?, ?);",
                   (appointment_id, bike_id, date, status, description))
    conn.commit()
    print("Appointment added successfully.")

def view_appointments():
    cursor.execute("SELECT * FROM Appointments;")
    for row in cursor.fetchall():
        print(row)

def add_service(service_id, appointment_id, date, cost, remarks):
    cursor.execute("INSERT INTO ServiceHistory (ServiceID, AppointmentID, ServiceDate, Cost, Remarks) VALUES (?, ?, ?, ?, ?);",
                   (service_id, appointment_id, date, cost, remarks))
    conn.commit()
    print("Service record added successfully.")

def view_services():
    cursor.execute("SELECT * FROM ServiceHistory;")
    for row in cursor.fetchall():
        print(row)

# Basic command-line interface
def menu():
    while True:
        print("\nBike Shop Management System")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Add Bike")
        print("4. View Bikes")
        print("5. Add Appointment")
        print("6. View Appointments")
        print("7. Add Service History")
        print("8. View Service History")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            id = int(input("Customer ID: "))
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_customer(id, name, phone, email)
        elif choice == '2':
            view_customers()
        elif choice == '3':
            id = int(input("Bike ID: "))
            reg = input("Registration Number: ")
            model = input("Model: ")
            year = int(input("Year: "))
            customer_id = int(input("Customer ID: "))
            add_bike(id, reg, model, year, customer_id)
        elif choice == '4':
            view_bikes()
        elif choice == '5':
            id = int(input("Appointment ID: "))
            bike_id = int(input("Bike ID: "))
            date = input("Appointment Date (YYYY-MM-DD): ")
            status = input("Status (Pending/In-Progress/Completed): ")
            description = input("Description: ")
            add_appointment(id, bike_id, date, status, description)
        elif choice == '6':
            view_appointments()
        elif choice == '7':
            id = int(input("Service ID: "))
            app_id = int(input("Appointment ID: "))
            date = input("Service Date (YYYY-MM-DD): ")
            cost = float(input("Cost: "))
            remarks = input("Remarks: ")
            add_service(id, app_id, date, cost, remarks)
        elif choice == '8':
            view_services()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

create_tables()
menu()

conn.close()
