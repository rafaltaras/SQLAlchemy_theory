import sqlalchemy
from sqlalchemy import create_engine

print(sqlalchemy.__version__)


engine = create_engine('sqlite:///chinook.db')

print(engine.driver)
print(engine.table_names())
print(engine.execute("SELECT * FROM genres"))
results = engine.execute("SELECT * FROM genres")

for r in results:
   print(r)