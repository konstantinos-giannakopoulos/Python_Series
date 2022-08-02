import sqlite3
#import Person

class Person():

    def __init__(self, first=None, last=None, age=None):
        self.first = first
        self.last = last
        self.age = age

    def clone_person(self,result):
        self.first = result[0]
        self.last = result[1]
        self.age = result[2]

        

# Start connection
conn = sqlite3.connect('mydata.db')
c = conn.cursor()

'''
# Create table
c.execute("""CREATE TABLE persons (
            first_name TEXT,
            last_name TEXT,
            age INTEGER
            )""")
'''
'''
# Insert into table
c.execute("""INSERT INTO persons VALUES
            ('John', 'Smith', 25),
            ('Anna', 'Smith', 30),
            ('Mike', 'Johnson', 40)
            """)
'''

'''
# Select
#From Table to Object
c.execute("""SELECT * FROM persons 
            WHERE last_name = 'Smith'
            """)
#print(c.fetchall())
person1 = Person()
person1.clone_person(c.fetchone())

print(person1.first)
print(person1.last)
print(person1.age)

# From Object to Table
person2 = Person("Bob", "Davis", 23)
c.execute("""INSERT INTO persons VALUES
            ('{}', '{}', {})"""
          .format(person2.first,
                  person2.last,
                  person2.age))

'''
c.execute("SELECT * FROM persons")
print(c.fetchall())


# Close connection
conn.commit()
conn.close()
