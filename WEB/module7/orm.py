from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///:memory:')
"""objekt dla inkasulacji bazy dnych w pamięci podręcznej, na dysk nie piszemy danych,
jest również możliwiść tworzenia obiektu engine bazy danych w loklnej directory"""
DBSession = sessionmaker(bind=engine) # objekt dla tworzenia zbioru sesji dostępu do bazy
session = DBSession()

Base = declarative_base()
"""klasa odpowidada za tworzenie "magii", 
czyli synchronizuje tabele bazy i ich opisy w klasach które te tabele definiują"""

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

Base.metadata.create_all(engine) # obiekt metadata za pomocą crete_all() tworzy nową bazę danych na podstawie ścieżki w engine
Base.metadata.bind = engine

new_person = Person(name="Bill") # definiujemy nowy wpis w tabeli Person
session.add(new_person) # dadajemy wpis w tabeli Person
session.commit() # za każdym razem musimy wykonać metodę commit() dla implementacji danych do tabeli

new_address = Address(post_code="00000", person=new_person) # definiujemy nowy wpis w tabeli Address
session.add(new_address) # dadajemy wpis w tabeli Address
session.commit() # za każdym razem musimy wykonać metodę commit() dla implementacji danych do tabeli


for person in session.query(Person).all():
    """za pomocą obiektu session tworzymy zapytnia do bazy, w tym przypadku query() zwraca SELECT na tabelę Person,
    metoda all() zwraca wszystki wpisy w tabeli"""
    print(person.name) # zwracamy imię z wpisu w tbeli Person
    