# 요청 / 응답 모델 정의
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    
class UserResponse(BaseModel):
    id: int
    username: str
    
    # ORM 객체를 직렬화 할수 있도록 ==> DB에서 가져온 객체를 API응답으로 사용하기 위해서
    class Config:
        orm_mode = True  # SQLAlchemy 모델과 호환되도록 설정
        
# 상품 등록 데이터 객체
class ProductCreate(BaseModel):
    name: str
    price: int
class ProductOut(BaseModel):
    id: int
    name: str
    price: int
    
    class Config:
        orm_mode = True  # SQLAlchemy 모델과 호환되도록 설정
class ProductItem(BaseModel):
    id: int
    name: str
    price: int
    quantity: int  # 장바구니에 담긴 수량
    
    
    class Config:
        orm_mode = True  # SQLAlchemy 모델과 호환되도록 설정
 
 class CartItem(BaseModel):
    user_id : int
    product_id : int
    quantity : int

class OrderOut(BaseModel):
    id : int
    user_id : int
    product_id : int 
    quantity : int

    class Config:
        from_attributes = True
   