# 데이터 베이스 테이블 정의
from sqlalchemy import Column, Integer, String
from database import Base
class User(Base): # 테이블 Base를 상속받아야만 sqlite 테이블 생성
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(string, unique = True, index=True)
    password = Column(String) # 일단 보안은 나중에