import sqlite3

#Create Connector and cursor
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

#Creating Tables
cur.execute("CREATE TABLE IF NOT EXISTS cars(car_id INTEGER PRIMARY KEY, car_name TEXT, car_price REAL)")
cur.execute("CREATE TABLE IF NOT EXISTS suppliers(supplier_id INTEGER PRIMARY KEY, supplier_name TEXT, supplier_location TEXT)")
cur.execute("""CREATE TABLE IF NOT EXISTS parts(part_id INTEGER PRIMARY KEY,part_name TEXT, part_price REAL,
 car_id INTEGER, supplier_id INTEGER, FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id),
 FOREIGN KEY(car_id) REFERENCES cars(car_id))""")

#Create classes for the tables objects
class Cars:
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price


class Suppliers:
    def __init__(self,id,name,location):
        self.id = id
        self.name = name
        self.location = location


class Parts:
    def __init__(self,id,name,price,car_id,supplier_id):
        self.id = id
        self.name = name
        self.price = price
        self.car_id = car_id
        self.supplier_id = supplier_id

#Create the methods to deal with CRUD operations
def insert_car(car):
    with conn:
        cur.execute("""
        INSERT INTO cars 
        VALUES(:car_id,:car_name,:car_price)""",
                       {'car_id': car.id, 'car_name': car.name, 'car_price': car.price})

def insert_supplier(supplier):
    with conn:
        cur.execute("""
        INSERT INTO suppliers 
        VALUES(:supplier_id,:supplier_name,:supplier_location)""",
                       {'supplier_id': supplier.id, 'supplier_name': supplier.name,
                        'supplier_location': supplier.location})

def insert_part(part):
    with conn:
        cur.execute("""
        INSERT INTO parts
        VALUES(:part_id,:part_name,:part_price,:car_id,:supplier_id)""",
                       {'part_id': part.id, 'part_name': part.name, 'part_price': part.price, 'car_id': part.car_id,
                        'supplier_id': part.supplier_id});

car1 = Cars(12,'Premio',20000)
car2 = Cars(13,'Prado',40000)

supplier1 = Suppliers(12,'Toyota','China')
supplier2 = Suppliers(17,'Jaguar','Japan')

part1 = Parts(10, 'Gears', 20, 12, 10)
part2 = Parts(13,'Wheel',17,1,11)

# create methods to access these data
def get_car_by_price(price):
    cur.execute("""
    SELECT * 
    FROM cars
    WHERE car_price=:car_price""",
                   {'car_price': price})
    print(cur.fetchall())

def get_supplier_by_id(supplier_id):
    cur.execute("""
    SELECT *
    FROM suppliers
    WHERE supplier_id=:supplier_id""",
                {'supplier_id': supplier_id})


def get_all_parts():
    cur.execute("""
    SELECT *
    FROM parts""")

    print(cur.fetchall())


#Updating elements in our three tables
def upate_car_price(car,price):
    with conn:
        cur.execute("""
        UPDATE cars
        SET car_price=:car_price
        WHERE car_name=:car_name""",
                    {'car_price':price, 'car_name':car.name})


def update_name_of_part(part,name):
    with conn:
        cur.execute("""
        UPDATE parts
        SET part_name=:part_name
        WHERE part_id=:part_id
        """, {'part_name': name, 'part_id': part.id})

#DELETING Elements from our tables
def delete_all_parts_not_supplied_by_our_supplier(supplier):
    with conn:
        cur.execute("""
        DELETE FROM parts
        WHERE supplier_id<>:supplier_id """,
                       {'supplier_id': supplier.id})

insert_car(car1)
insert_car(car2)

insert_part(part1)
insert_part(part2)

insert_supplier(supplier1)
insert_supplier(supplier2)
#get_car_by_price(20000)
upate_car_price(car1,17000)
get_car_by_price(17000)
#get_all_parts()
delete_all_parts_not_supplied_by_our_supplier(supplier1)
get_all_parts()