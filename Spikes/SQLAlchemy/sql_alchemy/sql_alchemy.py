from sqlite import sqlite_in_memory
from orm_base import Base, CarMake, CarModel, CarOwner, Car
from sqlalchemy.orm import Session, contains_eager

Base.metadata.create_all(sqlite_in_memory.dbEngine)
session = Session(bind=sqlite_in_memory.dbEngine)

chevrolet = CarMake(make_name="CHEVROLET")
toyota = CarMake(make_name="TOYOTA")
aveo = CarModel(model_name="AVEO")
joshua = CarOwner(first_name="Joshua", last_name="Boyd")
joshuaCar = Car(vin="01234567890ABCDEF0123")
chevrolet.car_models = [aveo]
aveo.cars = [joshuaCar]
joshua.cars = [joshuaCar]


session.add_all([chevrolet, toyota, aveo, joshua, joshuaCar])
session.commit()

resultSet = session.query(CarMake, CarModel, CarOwner, Car).\
    join(CarModel, CarMake.car_make_id == CarModel.car_make_id).\
    join(Car, CarModel.car_model_id == Car.car_model_id).\
    join(CarOwner, Car.car_owner_id == CarOwner.car_owner_id).\
    options(contains_eager(CarMake.car_models), contains_eager(CarModel.cars), contains_eager(CarOwner.cars))

for row in resultSet.all():
    print(row)

