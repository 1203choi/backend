# 요청 / 응답 모델 정의
from pydantic import BaseModel

class IserCreate(BaseModel):
    username: str
    password: str
    
class UserResponse(BaseModel):
    id: int
    username: str
    
    # ORM 객체를 직렬화 할수 있도록 ==> DB에서 가져온 객체를 API응답으로 사용하기 위해서
    class Config:
        orm_mode = True  # SQLAlchemy 모델과 호환되도록 설정