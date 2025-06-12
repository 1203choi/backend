from sqlalchemy import create_engine # DB 연결 엔진
from sqlalchemy.orm import sessionmaker, declarative_base # DB 세션, 모델 베이스 생성

DATABASE_URL = "sqlite:///./database.db"  # SQLite 데이터베이스 URL

# 현재경로에 database.db 파일을 생성
engine = create_engine(DATABASE_URL, connect_args = {"check_same_thread": False})

# 세션을 생성하는 함수 - 요청시 함수를 통해서 세션을 만들어 사용
SessionLocal = sessionmaker(bind = engine)

# 클래스를 정의할때마다 사용하는 base 클래스
Base = declarative_base()