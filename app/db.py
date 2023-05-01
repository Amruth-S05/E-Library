from sqlalchemy import Column, String, Integer, ForeignKey,  URL, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship

from .config import Config

import click


class Base(DeclarativeBase):
    pass


class Books(Base):
    """Books table to store books' data"""
    __tablename__ = "books"  # Table name is set as 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(100))
    qty = Column(Integer, nullable=False)
    genre = Column(String(100))


class User(Base):
    """User table to store user data"""
    __tablename__ = "user"  # Table name is set as 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    dept = Column(String(50), nullable=False)
    stu_staff = Column(String(10), nullable=False)


class Usage(Base):
    """Usage table to maintain data regarding the usage of library books"""
    __tablename__ = "usage"  # Table name is set as 'usage'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User)
    book = relationship(Books)


"""Database config data imported from config.py"""
dialect = Config.DIALECT
db_user = Config.DATABASE_USER
db_passwd = Config.DATABASE_PASSWORD
db_host = Config.HOST
database_name = Config.DATABASE_NAME

url_object = URL.create(  # creating database url for engine
    dialect,
    username=db_user,
    password=db_passwd,
    host=db_host,
    database=database_name
    )

engine = create_engine(url_object)


def init_db():  # Creates schema in the database
    Base.metadata.create_all(engine)
