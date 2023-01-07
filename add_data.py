from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db', echo=True)

meta = MetaData()

students = Table(
   'teachers', meta,
   Column('id', Integer, primary_key=True),
   Column('name', String),
   Column('lastname', String),
)

meta.create_all(engine)
print(engine.table_names())

#  Add data
ins = students.insert()
ins = students.insert().values(name='Ericc', lastname='Idle')
conn = engine.connect()
result = conn.execute(ins)
conn.execute(ins, [
   {'name': 'John', 'lastname': 'Cleese'},
   {'name': 'Graham', 'lastname': 'Chapman'},
])
print(ins)

# Get data
conn = engine.connect()
s = students.select().where(students.c.id < 2)
result = conn.execute(s)

for row in result:
   print(row)



# update = students.update()
# print(update)

# select = students.select()
# print(select)

# delete  = students.delete()
# print(delete)

# comp = delete.compile().params
# print(comp)