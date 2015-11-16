from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

SQLAlchemyBase = declarative_base()

class Path(SQLAlchemyBase):
    __tablename__ = "path"

    path_id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String(60), nullable=False)

    def __repr__(self):
        return "<Path(%r, %r)>" %(self.path_id, self.name)
