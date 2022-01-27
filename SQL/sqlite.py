import sqlite3

# create connection and cursor
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create the three tables
cursor.execute("CREATE TABLE IF NOT EXISTS cars(car_id INTEGER PRIMARY KEY, car_name TEXT, car_price REAL)")
cursor.execute("CREATE TABLE IF NOT EXISTS suppliers(supplier_id INTEGER PRIMARY KEY, supplier_name TEXT, supplier_location TEXT)")
cursor.execute("""CREATE TABLE IF NOT EXISTS parts(part_id INTEGER PRIMARY KEY,part_name TEXT, part_price REAL,
 car_id INTEGER, supplier_id INTEGER, FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id),
 FOREIGN KEY(car_id) REFERENCES cars(car_id))""")


#Inserting data into our tables
cursor.execute("""INSERT INTO cars
VALUES(1,'Mercedes',30000)""")

cursor.execute("""INSERT INTO suppliers
VALUES(11,'General_motors','Japan')""")

cursor.execute("""INSERT INTO parts
VALUES(121,'Sproket',12,1,11)""")


conn.commit()

#Using python objects with :+  dictionary placeholder

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
car1 = Cars(12,'Premio',20000)

cursor.execute("""
INSERT INTO cars 
VALUES(:car_id,:car_name,:car_price)""",
{'car_id':car1.id,'car_name':car1.name,'car_price':car1.price})

conn.commit()

supplier1 = Suppliers(12,'Toyota','China')
cursor.execute("""
INSERT INTO suppliers 
VALUES(:supplier_id,:supplier_name,:supplier_location)""",
{'supplier_id':supplier1.id,'supplier_name':supplier1.name,'supplier_location':supplier1.location})

conn.commit()

part1 = Parts(10, 'Gears', 20, 12, 10)
part2 = Parts(13,'Wheel',17,1,11)
cursor.execute("""
INSERT INTO parts
VALUES(:part_id,:part_name,:part_price,:car_id,:supplier_id)""",
               {'part_id':part1.id,'part_name':part1.name, 'part_price':part1.price, 'car_id':part1.car_id, 'supplier_id':part1.supplier_id} );

cursor.execute("""
INSERT INTO parts
VALUES(:part_id,:part_name,:part_price,:car_id,:supplier_id)""",
               {'part_id':part2.id,'part_name':part2.name, 'part_price':part2.price, 'car_id':part2.car_id, 'supplier_id':part2.supplier_id} );
conn.commit()

#Updating parts table
part1.name = 'Engine_block'
cursor.execute("""
UPDATE parts
SET part_name=:part_name
WHERE part_id=:part_id
""",{'part_name':part1.name,'part_id':part1.id})

conn.commit()

#Deleting Items
cursor.execute("""
DELETE FROM parts
WHERE car_id<>:car_id """,
               {'car_id':car1.id})

conn.commit()

cursor.execute("""SELECT * FROM cars""")
print(cursor.fetchall())
cursor.execute("""
SELECT * 
FROM cars
WHERE car_price=:car_price""",
               {'car_price':20000})
print(cursor.fetchall())


cursor.execute("""SELECT * FROM suppliers""")
print(cursor.fetchall())

cursor.execute("""
SELECT * 
FROM suppliers
WHERE supplier_name = :supplier_name""",
               {'supplier_name':supplier1.name})
print(cursor.fetchall())

cursor.execute("""SELECT * FROM parts""")
print(cursor.fetchall())


conn.close()