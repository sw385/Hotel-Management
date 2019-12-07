

import random
from datetime import datetime
from datetime import timedelta
from decimal import *

############################################################################################################################################

def generate_checkin():
    '''Generate a datetime between 2019-01-01 and the current date.'''
    start = datetime.strptime('2019-01-01', '%Y-%m-%d')
    end = datetime.today()
    duration = end - start
    output_date = start + timedelta(days=random.randint(0, duration.days))
    return output_date
    
def generate_checkout(CheckIn):
    '''Generate a datetime after the CheckIn date, up to 7 days after.'''
    start = CheckIn
    output_date = start + timedelta(days=random.randint(1, 7))
    return output_date

def generate_first_name():
    first_names = ['Oliver', 'Ethan', 'Amelia', 'Mia', 'Lucas', 'Chloe', 'Ava', 'Noah', 'Enzo', 'Mathias', 'Clara', 'Nathan', 'Youssef', 'Ines', 'Fatima', 'Santiago', 'Mohammad', 'Jade', 'Hugo', 'Felix', 'Diego', 'Maximilian', 'Javiera', 'Cristobal', 'Marek', 'Zofia', 'Ali', 'Oscar', 'Layla', 'Marta', 'Florian', 'Elzbieta', 'Tatiana', 'Tomasz', 'Beatriz', 'Yekaterina', 'Sanvi', 'Anika', 'Amina', 'Cornelius', 'Sofia', 'Harini', 'Aditya', 'Arnav', 'Ivan', 'Miriam', 'Devansh', 'Aarav', 'Camille', 'Arttu', 'Ridhi', 'Ishan', 'Tamar', 'Haruki', 'Rowena', 'Sosuke', 'Alvaro', 'Hinata', 'Momoka', 'Barack']
    return random.choice(first_names)
    
def generate_last_name():
    last_names = ['Wilson', 'Walker', 'Ryan', 'Singh', 'Harris', 'Bhoumik', 'Hasan', 'Tsui', 'Chen', 'Dahan', 'Wong', 'Suzuki', 'Yamamoto', 'Cho', 'Marquez', 'Lee', 'Kumara', 'Arslan', 'Garcia', 'Jones', 'Williams', 'Davis', 'Moore', 'Demir', 'Wagner', 'Kenobi', 'Novik', 'Miller', 'Rodriguez', 'Peeters', 'Brennan', 'Kamau', 'Beaumont', 'Andersen', 'Rebane', 'Kuznetsov', 'Lovelace', 'Babbage', 'Hopper', 'McClintock', 'Burnell', 'Holberton', 'Bilas', 'Bartik', 'Lichterman', 'McNulty', 'Snyder', 'Wescoff']
    return random.choice(last_names)

def generate_name():
    return generate_first_name() + ' ' + generate_last_name()

# def generate_shiftstart():

# def generate_shiftend(ShiftStart):
    '''Generate a shiftend after the shiftstart. Assume no shifts cross over midnight.'''

def generate_credit_card():
    '''Generates a string of 16 numbers.'''
    number = ''
    for x in range(16):
        number += str(random.randint(0, 9))
    return number
    
def generate_sec_code():
    '''Generates a string of 3 numbers.'''
    number = ''
    for x in range(3):
        number += str(random.randint(0, 9))
    return number

def generate_exp_date():
    '''Generates a datetime string in the future.'''
    output_date = datetime.today() + timedelta(days=random.randint(180, 365*4))
    return datetime.strftime(output_date, '%Y-%m-%d')
    
# def generate_purchasedate():
    #pass
    
def collide(booking1, booking2):
    '''Return True if the bookings are in the same room and at the same time/overlap, False otherwise.'''
    
    if booking1['fields']['RoomIDNum'] != booking2['fields']['RoomIDNum']:
        return False
        
    start1 = datetime.strptime(booking1['fields']['CheckIn'], '%Y-%m-%d')
    end1 = datetime.strptime(booking1['fields']['CheckOut'], '%Y-%m-%d')
    start2 = datetime.strptime(booking2['fields']['CheckIn'], '%Y-%m-%d')
    end2 = datetime.strptime(booking2['fields']['CheckOut'], '%Y-%m-%d')
    
    if start1 == start2 or end1 == end2:
        return True
    
    if start2 > start1 and start2 < end1:
        return True
    if end2 > start1 and end2 < end1:
        return True
    if start1 > start2 and start1 < end2:
        return True
    if end1 > start2 and end1 < end2:
        return True
    
    return False
    
    
############################################################################################################################################


def generate_Booking(count, customer_id, room_id):
    '''count is the number of existing Bookings, ids are strings'''
    
    data = {}
    # data['model'] = ''
    # data['pk'] = generate_uuid()

    fields = {}
    
    fields['BookingIDPrefix'] = 'B'
    fields['BookingIDNum'] = str(count + 1)
    fields['CustomerIDPrefix'] = 'C'
    fields['CustomerIDNum'] = customer_id
    fields['RoomIDPrefix'] = 'R'
    fields['RoomIDNum'] = room_id
    CheckIn = generate_checkin()
    fields['Paid'] = str(random.randint(0, 1))
    CheckOut = generate_checkout(CheckIn)
    fields['Guests'] = str(random.randint(1, 4))
    # logic to restrict the number of guests based on the room type

    fields['CheckIn'] = datetime.strftime(CheckIn, '%Y-%m-%d')
    fields['CheckOut'] = datetime.strftime(CheckOut, '%Y-%m-%d')

    # for key in fields:
        # print(key + ':    ', fields[key])

    data['fields'] = fields

    return data
    
def generate_Room(count, TypeID):

    data = {}
    # data['model'] = ''
    # data['pk'] = generate_uuid()

    fields = {}
    
    fields['RoomIDPrefix'] = 'R'
    fields['RoomIDNum'] = str(count + 1)
    fields['TypeID'] = TypeID
    # the TypeID of a particular RoomClass
    fields['Floor'] = str(random.randint(1, 3))
    fields['Occupied'] = str(random.randint(0, 1))
    fields['CleanedDate'] = 'NULL'
    fields['CleanedTime'] = 'NULL'
    
    # for key in fields:
        # print(key + ':    ', fields[key])

    data['fields'] = fields

    return data


def generate_RoomClass(count):

    data = {}
    # data['model'] = ''
    # data['pk'] = generate_uuid()

    fields = {}
    
    fields['TypeIDPrefix'] = 'L'
    fields['TypeIDNum'] = str(count + 1)
    fields['Bed'] = str(random.randint(1, 4))
    fields['Bathroom'] = str(random.randint(1, 2))
    fields['Amenities'] = '<amenities go here>'
    fields['Price'] = str(int(fields['Bed']) * random.randint(10, 30)) + random.choice(['.00', '.50', '.99', '.95'])
    
    # for key in fields:
        # print(key + ':    ', fields[key])

    data['fields'] = fields

    return data


def generate_InventoryItem(count):

    data = {}
    # data['model'] = ''
    # data['pk'] = generate_uuid()

    fields = {}
    
    fields['ItemIDPrefix'] = 'I'
    fields['ItemIDNum'] = str(count + 1)
    fields['ItemDescription'] = '<item description goes here>'
    if random.randint(1, 10) <= 2:
        fields['Quantity'] = '0'
    else:
        fields['Quantity'] = str(random.randint(1, 1000))
    
    # for key in fields:
        # print(key + ':    ', fields[key])

    data['fields'] = fields

    return data

def generate_PayStub(count, staff_dict, date_string):

    data = {}
    # data['model'] = ''
    # data['pk'] = generate_uuid()

    fields = {}
    
    fields['StubIDPrefix'] = 'P'
    fields['StubIDNum'] = str(count + 1)
    fields['StaffIDPrefix'] = 'S'
    fields['StaffIDNum'] = staff_dict['fields']['StaffIDNum']
    fields['Payment'] = str(14 * 6 * Decimal(staff_dict['fields']['PayRate'])) # 14 days * shift hours * pay rate
    fields['Date'] = date_string # every two weeks
    
    # for key in fields:
        # print(key + ':    ', fields[key])

    data['fields'] = fields

    return data


def generate_Staff(count):

    data = {}
    # data['model'] = ''
    # data['pk'] = generate_uuid()

    fields = {}
    
    fields['StaffIDPrefix'] = 'S'
    fields['StaffIDNum'] = str(count + 1)
    fields['FirstName'] = generate_first_name()
    fields['LastName'] = generate_last_name()
    # ShiftStart = generate_shiftstart()
    # ShiftEnd = generate_shiftend(ShiftStart)
    times = ['00:00:00', '06:00:00', '12:00:00', '18:00:00', '00:00:00']
    num = random.randint(0, 3)
    fields['ShiftStart'] = times[num]
    fields['ShiftEnd'] = times[num + 1]
    # hh:mm:ss.nnnnnnn
    # assuming that the shifts are the same for all days of the week
    fields['PayRate'] = str(random.randint(10, 20)) + random.choice(['.00', '.25', '.50', '.75'])
    
    # for key in fields:
        # print(key + ':    ', fields[key])

    data['fields'] = fields

    return data

def generate_Transaction(count, ItemIDNum):

    data = {}
    # data['model'] = ''
    # data['pk'] = generate_uuid()

    fields = {}
    
    fields['TransactionIDPrefix'] = 'T'
    fields['TransactionIDNum'] = str(count + 1)
    fields['ItemIDPrefix'] = 'I'
    fields['ItemIDNum'] = ItemIDNum
    fields['Quantity'] = str(random.randint(0, 100))
    price_dollars = random.randint(0, 20)
    price_cents = random.randint(0, 99)
    fields['UnitPrice'] = str(price_dollars) + '.' + str(price_cents)
    total_dollars = (int(fields['Quantity']) * price_dollars) + int(int(fields['Quantity']) * price_cents / 100)
    total_cents = (int(fields['Quantity']) * price_cents) % 100
    fields['TotalCost'] =  str(total_dollars) + '.' + str(total_cents)
    fields['PurchaseDate'] = 'NULL' # generate_purchasedate()
    
    # for key in fields:
        # print(key + ':    ', fields[key])

    data['fields'] = fields

    return data


def generate_Customer(count):

    data = {}
    # data['model'] = ''
    # data['pk'] = generate_uuid()

    fields = {}
    
    fields['CustomerIDPrefix'] = 'C'
    fields['CustomerIDNum'] = str(count + 1)
    fields['Name'] = generate_name()
    fields['CreditCardNum'] = generate_credit_card()
    fields['SecCode'] = generate_sec_code()
    fields['ExpDate'] = generate_exp_date()
    
    # for key in fields:
        # print(key + ':    ', fields[key])

    data['fields'] = fields

    return data



def write_csv(filename, columns, entries_list):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(','.join(columns) + '\n')
        for element in entries_list:
            string = ''
            for column in columns:
                string += element['fields'][column] + ','
            string = string.strip(',')
            file.write(string + '\n')

############################################################################################################################################


    
if __name__ == "__main__":

    # number of instances for each table
    num_of_bookings = 45
    num_of_rooms = 10           # number of rooms per roomclass
    num_of_roomclasses = 4
    num_of_inventory_items = 25
    num_of_paystubs = 24        # number of paystubs per staff member
    num_of_staff = 15
    num_of_transactions = 100
    num_of_customers = 30
    
    bookings = []
    rooms = []
    roomclasses = []
    inventory_items = []
    paystubs = []
    staff = []
    transactions = []
    customers = []
    
    for x in range(num_of_roomclasses):
        roomclasses.append(generate_RoomClass(x))
    for x in range(num_of_rooms):
        for roomclass in roomclasses:
            rooms.append(generate_Room(len(rooms), roomclass['fields']['TypeIDNum']))
    for x in range(num_of_staff):
        staff.append(generate_Staff(len(staff)))
    for x in range(num_of_customers):
        customers.append(generate_Customer(len(customers)))
    while len(bookings) < num_of_bookings:
        booking2 = generate_Booking(len(bookings), random.choice(customers)['fields']['CustomerIDNum'], random.choice(rooms)['fields']['RoomIDNum'])
        collision = False
        for booking1 in bookings:
            if collide(booking1, booking2) == True:
                collision = True
        if collision == False:
            bookings.append(booking2)
    for x in range(num_of_inventory_items):
        inventory_items.append(generate_InventoryItem(len(inventory_items)))
    for x in range(num_of_transactions):
        transactions.append(generate_Transaction(len(transactions), random.choice(inventory_items)['fields']['ItemIDNum']))
    for employee in staff:
        start = datetime.strptime('2018-01-06', '%Y-%m-%d') + timedelta(days=14*random.randint(0, 20))
        for x in range(num_of_paystubs):
            paystub_date = start + timedelta(days=14 * x)
            paystub_date_string = datetime.strftime(paystub_date, '%Y-%m-%d')
            paystubs.append(generate_PayStub(len(paystubs), employee, paystub_date_string))



    write_csv('Customers.csv', ['CustomerIDNum','Name','CreditCardNum','SecCode','ExpDate'], customers)
    write_csv('Bookings.csv', ['BookingIDNum','CustomerIDNum','RoomIDNum','CheckIn','Paid','CheckOut','Guests'], bookings)
    write_csv('Rooms.csv', ['RoomIDNum','TypeID','Floor','Occupied','CleanedDate','CleanedTime'], rooms)
    write_csv('RoomClasses.csv', ['TypeIDNum','Bed','Bathroom','Amenities','Price'], roomclasses)
    write_csv('Inventory.csv', ['ItemIDNum','ItemDescription','Quantity'], inventory_items)
    write_csv('PayStubs.csv', ['StubIDNum','StaffIDNum','Payment','Date'], paystubs)
    write_csv('Staff.csv', ['StaffIDNum','FirstName','LastName','ShiftStart','ShiftEnd','PayRate'], staff)
    write_csv('TransactionLog.csv', ['TransactionIDNum','ItemIDNum','Quantity','UnitPrice','TotalCost','PurchaseDate'], transactions)

        
