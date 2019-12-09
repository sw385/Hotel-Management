import connection as conn

"""
The purpose of the following functions are to create and load the following tables:

1. Bookings   			3. Inventory 		5. RoomClasses 		7. Staff
2. Customers 			4. Paystubs 		6. Rooms 			8. TransactionLog

in the Database by using the methods implemented in connection.py 

"""
def GenerateBookings():
	table_name = "Bookings"
	columns_c = "BookingIDNum int, CustomerIDNum int, RoomIDNum int, CheckIn date, CheckOut date, Guests int, Primary Key(BookingIDNum)"
	columns_i = "BookingIDNum, CustomerIDNum, RoomIDNum, CheckIn, CheckOut, Guests"
	conn.CreateTable(table_name, columns_c)
	insert_query ="INSERT INTO Bookings(BookingIDNum, CustomerIDNum, RoomIDNum, CheckIn, CheckOut, Guests) VALUES (%s, %s, %s, %s, %s, %s)"
	conn.LoadCSV('Bookings.csv', insert_query)


def GenerateCustomers():
	table_name = "Customers"
	columns_c = "CustomerIDNum int, Name varchar(50), CreditCardNum varchar(16), SecCode varchar(4), ExpDate date, Primary Key (CustomerIDNum)"
	columns_i = "CustomerIDNum, Name, CreditCardNum, SecCode, ExpDate"
	conn.CreateTable(table_name, columns_c)
	insert_query ="INSERT INTO Customers(CustomerIDNum,Name, CreditCardNum, SecCode, ExpDate) values (%s, %s, %s, %s, %s)"
	conn.LoadCSV('Customers.csv', insert_query)

def GenerateInventory():
	table_name = "Inventory"
	columns_c = "ItemIDNum int, ItemDescription varchar(50), Quantity int, Primary Key(ItemIDNum)"
	columns_i = "ItemIDNum, ItemDescription, Quantity"
	conn.CreateTable(table_name, columns_c)
	insert_query ="INSERT INTO Inventory(ItemIDNum, ItemDescription, Quantity) VALUES (%s, %s, %s)"
	conn.LoadCSV('Inventory.csv', insert_query)

def GeneratePayStubs():
	table_name = "PayStubs"
	columns_c = "StubIDNum int, StaffIDNum int, Payment float, Date date, Primary Key(StubIDNum)"
	columns_i = "StubIDNum, StaffIDNum, Payment, Date"
	conn.CreateTable(table_name, columns_c)
	insert_query ="INSERT INTO PayStubs(StubIDNum, StaffIDNum, Payment, Date) VALUES (%s, %s, %s, %s)"
	conn.LoadCSV('PayStubs.csv', insert_query)

def GenerateRoomClasses():
	table_name = "RoomClasses"
	columns_c = "TypeIDNum int, Bed int, Bathroom int, Amenities varchar(50), Price float, Primary Key(TypeIDNum)"
	columns_i = "TypeIDNum, Bed, Bathroom, Amenities, Price"
	conn.CreateTable(table_name, columns_c)
	insert_query ="INSERT INTO RoomClasses(TypeIDNum, Bed, Bathroom, Amenities, Price) VALUES (%s, %s, %s, %s, %s)"
	conn.LoadCSV('RoomClasses.csv', insert_query)

def GenerateRooms():
	table_name = "Rooms"
	columns_c = "RoomIDNum int,TypeID varchar(5),Floor int, Primary Key(RoomIDNum)"
	columns_i = "RoomIDNum, TypeID, Floor"
	conn.CreateTable(table_name, columns_c)
	insert_query ="INSERT INTO Rooms(RoomIDNum, TypeID, Floor) VALUES (%s, %s, %s)"
	conn.LoadCSV('Rooms.csv', insert_query)

def GenerateStaff():
	table_name = "Staff"
	columns_c = "StaffIDNum int, FirstName varchar(20), LastName varchar(20), ShiftStart time, ShiftEnd time, PayRate float, Primary Key (StaffIDNum)"
	columns_i = "StaffIDNum, FirstName, LastName, ShiftStart, ShiftEnd, PayRate"
	conn.CreateTable(table_name, columns_c)
	insert_query ="INSERT INTO Staff(StaffIDNum, FirstName, LastName, ShiftStart, ShiftEnd, PayRate) VALUES (%s, %s, %s, %s, %s, %s)"
	conn.LoadCSV('Staff.csv', insert_query)

def GenerateTransactionLog():
	table_name = "TransactionLog"
	columns_c = " TransactionIDNum int, ItemIDNum int, Quantity int, UnitPrice float, TotalCost float, PurchaseDate date, Primary Key(TransactionIDNum)"
	columns_i = "TransactionIDNum, ItemIDNum, Quantity, UnitPrice, TotalCost, PurchaseDate"
	conn.CreateTable(table_name, columns_c)
	insert_query ="INSERT INTO TransactionLog(TransactionIDNum, ItemIDNum, Quantity, UnitPrice, TotalCost, PurchaseDate) VALUES (%s, %s, %s, %s, %s, %s)"
	conn.LoadCSV('TransactionLog.csv', insert_query)
 
