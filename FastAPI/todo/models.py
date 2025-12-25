from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) # Unique identifier for each todo item. Here index=True creates an index on this column to optimize query performance.
    email = Column(String, unique=True) # Title of the todo item
    username = Column(String, unique=True) # Description of the todo item
    hashed_password = Column(String) # Description of the todo item
    first_name = Column(String) # Description of the todo item
    last_name = Column(String) # Description of the todo item
    is_active = Column(Boolean, default=True) # Priority level of the todo item
    role = Column(String) # Completion status of the todo item. We should not use index=True here as it can lead to inefficient indexing for boolean fields with low cardinality.
    phone_no = Column(String) # Completion status of the todo item. We should not use index=True here as it can lead to inefficient indexing for boolean fields with low cardinality.

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, username={self.username}, first_name={self.first_name}, last_name={self.last_name}, is_active={self.is_active}, role={self.role})>"

class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True) # Unique identifier for each todo item. Here index=True creates an index on this column to optimize query performance.
    title = Column(String, index=True) # Title of the todo item
    description = Column(String, index=True) # Description of the todo item
    priority = Column(Integer) # Priority level of the todo item
    complete = Column(Boolean, default=False) # Completion status of the todo item. We should not use index=True here as it can lead to inefficient indexing for boolean fields with low cardinality.
    owner_id = Column(Integer, ForeignKey("users.id")) # Foreign key to link todo item to a user (assuming a user management system exists)

    def __repr__(self):
        return f"<Todo(id={self.id}, title={self.title}, description={self.description}, priority={self.priority}, complete={self.complete})>"