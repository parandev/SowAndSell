from db.base import Base
from db.session import engine

Base.metadata.create_all(bind=engine)
