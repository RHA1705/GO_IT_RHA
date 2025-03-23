from rel_one_to_many import User, Article, session


# user = session.query(User).get(1)
# session.delete(user)
# session.commit()

article = session.query(Article).get(2)
session.delete(article)
session.commit()