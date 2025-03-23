from rel_one_to_many import User, Article, session


# user = session.query(User).get(2)
# user.id = 1
# session.add(user)
# session.commit()

article = session.query(Article).get(1)
article.content = 'Very important content for the article'
article.user_id = 1
session.add(article)
session.commit()