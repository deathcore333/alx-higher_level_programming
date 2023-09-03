# OBJECT RELATIONAL MAPPING ORM
# Object-Relational Mapping (ORM) in Python

## Table of Contents
- [Introduction](#introduction)
- [Why Use ORM?](#why-use-orm)
- [Popular Python ORM Libraries](#popular-python-orm-libraries)
- [Getting Started with SQLAlchemy](#getting-started-with-sqlalchemy)
  - [Installation](#installation)
  - [Basic Usage](#basic-usage)
- [Defining Models](#defining-models)
  - [Creating a SQLAlchemy Model](#creating-a-sqlalchemy-model)
  - [Mapping to a Database Table](#mapping-to-a-database-table)
- [CRUD Operations](#crud-operations)
  - [Creating Records](#creating-records)
  - [Reading Records](#reading-records)
  - [Updating Records](#updating-records)
  - [Deleting Records](#deleting-records)
- [Querying](#querying)
  - [Filtering](#filtering)
  - [Joins](#joins)
  - [Aggregation](#aggregation)
- [Conclusion](#conclusion)

## Introduction

Object-Relational Mapping (ORM) is a programming technique that allows you to interact with relational databases using Python objects. ORM libraries abstract the database interaction, making it more Pythonic and easier to work with databases.

In Python, SQLAlchemy is one of the most popular ORM libraries. This README will primarily focus on SQLAlchemy, but the concepts are applicable to other Python ORM libraries as well.

## Why Use ORM?

- **Abstraction**: ORM provides a higher-level abstraction over SQL, allowing developers to work with databases using Python classes and objects.
- **Database Independence**: You can switch between different database backends (e.g., SQLite, PostgreSQL, MySQL) without changing your Python code significantly.
- **Security**: ORM libraries often provide built-in protection against SQL injection attacks.
- **Productivity**: ORM simplifies database operations, reducing the amount of boilerplate code required for database interactions.

## Popular Python ORM Libraries

Besides SQLAlchemy, some other popular Python ORM libraries include:

- **Django ORM**: Part of the Django web framework, it provides a built-in ORM for web applications.
- **Peewee**: A lightweight and expressive ORM.
- **Django REST framework**: An extension of Django ORM specifically designed for building RESTful APIs.

## Getting Started with SQLAlchemy

### Installation

You can install SQLAlchemy using pip:

```bash
pip install SQLAlchemy
```

### Basic Usage

Here's a basic example of how to use SQLAlchemy:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an SQLite database in memory
engine = create_engine('sqlite:///:memory:')

# Create a Session class
Session = sessionmaker(bind=engine)

# Create a new session
session = Session()

# Define and create a new table
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    birthdate = Column(Date)

Base.metadata.create_all(engine)
```

## Defining Models

### Creating a SQLAlchemy Model

In SQLAlchemy, a model is defined as a Python class that inherits from `declarative_base()`. Each attribute in the class corresponds to a column in the database table.

```python
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    birthdate = Column(Date)
```

### Mapping to a Database Table

To create the corresponding table in the database, use `Base.metadata.create_all(engine)`, where `engine` is your database engine.

```python
from sqlalchemy import create_engine

# Create an SQLite database
engine = create_engine('sqlite:///mydatabase.db')

# Create the table
Base.metadata.create_all(engine)
```

## CRUD Operations

### Creating Records

```python
# Creating a new user
new_user = User(username='john_doe', birthdate='1990-01-01')
session.add(new_user)
session.commit()
```

### Reading Records

```python
# Querying for a user by ID
user = session.query(User).get(1)

# Querying for all users
all_users = session.query(User).all()
```

### Updating Records

```python
# Updating a user's information
user = session.query(User).filter_by(username='john_doe').first()
user.username = 'johndoe'
session.commit()
```

### Deleting Records

```python
# Deleting a user
user = session.query(User).filter_by(username='johndoe').first()
session.delete(user)
session.commit()
```

## Querying

### Filtering

```python
# Querying users with a specific condition
users = session.query(User).filter(User.username.like('%doe%')).all()
```

### Joins

```python
from sqlalchemy import join

# Joining two tables
from_table = session.query(User)
joined_table = join(from_table, other_table, from_table.c.id == other_table.c.user_id)
result = session.execute(joined_table).fetchall()
```

### Aggregation

```python
from sqlalchemy import func

# Performing aggregation
total_users = session.query(func.count(User.id)).scalar()
```

## Conclusion

Object-Relational Mapping in Python, using libraries like SQLAlchemy, simplifies database interactions and makes it easier to work with databases in a Pythonic way. By defining models, you can create, read, update, and delete records in the database using Python objects and queries. This approach enhances productivity and maintainability when working with relational databases in Python applications.
