# 데이터 베이스 테이블 정의
from sqlalchemy import Column, Integer, String
from database import Base
class User(Base): # 테이블 Base를 상속받아야만 sqlite 테이블 생성
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique = True, index=True)
    password = Column(String) # 일단 보안은 나중에
 
# 상품 테이블    
class Procuct(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer,foreign_keys = 'user.id')  # 사용자 id

# 장바구니 테이블
class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, foreign_keys='user.id')  # 사용자 id
    product_id = Column(Integer, foreign_keys='product.id')  # 상품 id
    quantity = Column(Integer)  # 수량
    
# 주문 테이블
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, foreign_keys='user.id')  # 사용자 id
    product_id = Column(Integer, foreign_keys='product.id')  # 상품 id
    quantity = Column(Integer)  # 수량
    status = Column(String)  # 주문 상태 (예: 'pending', 'shipped', 'delivered')
    
    