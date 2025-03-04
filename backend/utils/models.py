from sqlalchemy import Column, Integer, String, ForeignKey
from  .database import  Base, engine




class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)

    # user = relationship('ChatHistory', back_populates='chats')
    
class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String, index=True)


class ChatHistory(Base):
    __tablename__ = 'chat_history'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(String)

    # chats = relationship('User', back_populates='user')
    



Base.metadata.create_all(bind=engine)

