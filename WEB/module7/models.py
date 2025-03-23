from sqlalchemy import create_engine, Integer, String, ForeignKey, select, Text, and_, desc, func
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship

engine = create_engine('sqlite:///:memory:', echo=False)  
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String)


class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[str] = mapped_column('user_id', Integer, ForeignKey('users.id'))
    user: Mapped['User'] = relationship(User)


Base.metadata.create_all(engine)

if __name__ == '__main__':
    names = ['Crystal Najera', 'Shaun Beck', 'Kathrin Reinhardt']
    for name in names:
        user = User(fullname=name)
        session.add(user)
    session.commit()
    
    stmt = select(User.id, User.fullname)
    result = session.execute(stmt)
    users = []
    for row in result:
        users.append(row)
    
    for user in users:
        post = Post(title=f'Title {user[1]}', body=f'Body post user {user[1]}', user_id=user[0])
        session.add(post)
    session.commit()
    
    stmt = (
        select(User.fullname, func.count(Post.id))  # створюємо об'єкт select із вибіркою імені користувача та кількості постів
        .join(Post)  # робимо join з моделлю Post за зовнішнім ключем user_id
        .group_by(User.fullname)  # групуємо результати за ім'ям користувача
    )
    results = session.execute(stmt).all()  # виконуємо запит і отримуємо список кортежів
    for name, count in results:  # перебираємо результати
        print(f"{name} has {count} posts")  # виводимо ім'я користувача та кількість постів
