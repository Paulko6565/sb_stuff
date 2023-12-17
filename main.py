import sqlalchemy.orm
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///memory:', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age='{self.age}')>"

Base.metadata.create_all(bind=engine)

Session = sessionmaker()

session = Session()

user1 = User(name="Winnie the Pooh", age=51)
user2 = User(name="Hong Kong", age=64)

session.add(user1)
session.add(user2)

session.commit()

users = session.query(User).all()

for user in users:
    print(user)