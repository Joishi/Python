from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, BigInteger, String, ForeignKey

class CarMake(Base):
    __tablename__ = "car_make"

    car_make_id = Column(BigInteger, primary_key=True)
    make_name = Column(String(60), nullable=False)

    def __repr__(self):
        return "<CarMake(%r, %r)>" % (
            self.car_make_id, self.make_name
        )

class CarModel(Base):
    __tablename__ = "car_model"

    car_model_id = Column(BigInteger, primary_key=True)
    car_make_id = Column(BigInteger, ForeignKey(CarMake.car_make_id), nullable=False)
    model_name = Column(String(60), nullable=False)

    def __repr__(self):
        return "<CarModel(%r, %r, %r)>" % (
            self.car_model_id, self.car_make_id, self.model_name
        )

class CarOwner(Base):
    __tablename__ = "car_owner"

    car_owner_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)

    def __repr__(self):
        return "<CarOwner(%r, %r, %r)>" % (
            self.car_owner_id, self.first_name, self.last_name
        )

class Car(Base):
    __tablename__ = "car"

    car_id = Column(BigInteger, primary_key=True)
    car_model_id = Column(BigInteger, ForeignKey(CarModel.car_model_id), nullable=False)
    car_owner_id = Column(BigInteger, ForeignKey(CarOwner.car_owner_id))
    vin = Column(String(60), nullable=False)

    def __repr__(self):
        return "<Car(%r, %r, %r, %r)>" % (
            self.car_id, self.car_model_id, self.car_owner_id, self.vin
        )
