from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///:memory:')
"""objekt dla inkasulacji bazy dnych w pamięci podręcznej, na dysk nie piszemy danych"""
DBSession = sessionmaker(bind=engine) # objekt dla 
session = DBSession()

Base = declarative_base()

class Person(Base):
    """Klasa definuje elementy tabeli"""
    __tablename__ = 'persons' # dodajemy nazwę tabeli
    id = Column(Integer, primary_key=True) # dodajemy kolumnę(Column) id, typ int
    name = Column(String(250), nullable=False) # dodajemy kolumnę(Column) imię, typ str, pole nie może być puste(nullable=False)

class Address(Base):
    """Klasa definuje elementy tabeli"""
    __tablename__ = 'addresses' # dodajemy nazwę tabeli
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship(Person)

Base.metadata.create_all(engine)
Base.metadata.bind = engine

new_person = Person(name="Bill")
session.add(new_person)

session.commit()

new_address = Address(post_code="00000", person=new_person)
session.add(new_address)
session.commit()

for person in session.query(Person).all():
    print(person.name)
    