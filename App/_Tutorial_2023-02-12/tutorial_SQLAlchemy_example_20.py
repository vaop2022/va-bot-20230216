from sqlalchemy import URL, create_engine, select, Table, MetaData
from sqlalchemy.sql import select, and_ 

hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'Postg!2408'
port_id = 5432

url_object = URL.create(
    "postgresql",
    username=username,
    password=pwd,  # plain (unescaped) text
    host=hostname,
    database=database,
)

engine = create_engine(url_object, echo = False)
meta = MetaData(engine)

authors = Table('Authors', meta)
#payments = Table('payments', meta)

conn = engine.connect()
#ins_author_query = authors.insert().values(name = 'Val_test')
#conn.execute(ins_author_query)

s = select(authors).where(True)
result = conn.execute(s)

print('\nResult\n')
for row in result:
    print('test_row', row)

print('\nThe end')

