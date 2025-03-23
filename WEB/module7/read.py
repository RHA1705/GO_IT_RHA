from rel_one_to_many import User, Article, session


# user = session.query(User).get({'id': 1})
# print(user.id, user.name)

# users = session.query(User).all()
# for user in users:
#     print(user.id, user.name)

# user = session.query(User).filter(User.name == "Boris Johnson")
# print(user.id, user.name)

# user1 = session.query(User).filter_by(name='Boris Johnson').first()
# user2 = session.query(User).filter(User.name == 'Boris Johnson').scalar()
# print(user1.id, user1.name)
# print(user2.id, user2.name)

articles = session.query(Article).all()
for article in articles:
    print(article.id, article.title, article.content, article.user_id)
