from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker

DATABASE_URL = "sqlite:///team_management.db"

engine = create_engine(DATABASE_URL)
db_session = scoped_session(sessionmaker(bind=engine))
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
Base.query = db_session.query_property()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    name = Column(String)
    tasks = relationship("Task", back_populates="user")
    events = relationship("Event", back_populates="user")
    files = relationship("File", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, telegram_id={self.telegram_id}, name={self.name})>"

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    description = Column(String(1000))
    deadline = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, deadline={self.deadline}, user_id={self.user_id})>"

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    description = Column(String(1000))
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="events")

    def __repr__(self):
        return f"<Event(id={self.id}, title={self.title}, date={self.date}, user_id={self.user_id})>"

class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True)
    file_id = Column(String(500))
    file_name = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="files")

    def __repr__(self):
        return f"<File(id={self.id}, file_id={self.file_id}, file_name={self.file_name}, user_id={self.user_id})>"


def create_tables():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    Base.metadata.create_all(engine)