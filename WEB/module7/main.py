"""SQLAlchemy"""
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql import select

engine = create_engine('sqlite:///:memory:', echo=True)
"""Робота з ORM починається зі створення об'єкта, що інкапсулює доступ до бази даних, 
в SQLAlchemy він називається engine. У цьому прикладі ми використовуємо SQLite базу даних у пам'яті,
на диск нічого не записується."""

metadata = MetaData()
"""об'єкт-міст між базою даних та Python кодом. 
Завдання цього об'єкту синхронізувати базу даних та опис цієї бази в Python об'єктах."""

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String),
)

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', Integer, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
)

metadata.create_all(engine)

ins = users.insert().values(name='jack', fullname='Jack Jones')
print(str(ins)) # INSERT INTO users (name, fullname) VALUES (:name, :fullname)

with engine.connect() as conn:
    result = conn.execute(ins)

    s = select(users)
    result = conn.execute(s)
    for row in result:
        print(row)
