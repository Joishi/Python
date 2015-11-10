from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, BigInteger, String, ForeignKey

class CarMake(Base):
    __tablename__ = "car_make"

    car_make_id = Column(BigInteger, primary_key=True)
    car_make_name = Column(String(60), nullable=False)

    def __repr__(self):
        return "<CarMake(%r, %r)>" % (
            self.car_make_id, self.car_make_name
        )

class CarModel(Base):
    __tablename__ = "car_model"

    car_model_id = Column(BigInteger, primary_key=True)
    car_make_id = Column(BigInteger, ForeignKey(CarMake.car_make_id), nullable=False)
    car_model_name = Column(String(60), nullable=False)
