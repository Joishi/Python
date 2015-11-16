from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

SQLAlchemyBase = declarative_base()

class Path(SQLAlchemyBase):
    __tablename__ = "path"

    path_id = Column(Integer, autoincrement=True, primary_key=True)

    def __repr__(self):
        return "<Path(%r)>" %(self.path_id)
