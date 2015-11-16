from sqlite import sqlite_in_memory
from orm_base import Base, CarMake, CarModel, CarOwner, Car
from sqlalchemy.orm import Session

Base.metadata.create_all(sqlite_in_memory.dbEngine)
session = Session(bind=sqlite_in_memory.dbEngine)

chevrolet = CarMake(car_make_id=1, make_name="CHEVROLET")
toyota = CarMake(car_make_id=2, make_name="TOYOTA")

aveo = CarModel(car_model_id=1, car_make_id=1, model_name="AVEO")

joshua = CarOwner(car_owner_id=1, first_name="Joshua", last_name="Boyd")

joshuaCar = Car(car_id=1, car_model_id=1, car_owner_id=1, vin="01234567890ABCDEF0123")

session.add_all([chevrolet, toyota, aveo, joshua, joshuaCar])

resultSet = session.query(CarMake)
for row in resultSet.all():
    print(row)

resultSet = session.query(CarModel)
for row in resultSet.all():
    print(row)

resultSet = session.query(CarOwner)
for row in resultSet.all():
    print(row)

resultSet = session.query(Car)
for row in resultSet.all():
    print(row)

#resultSet = sqlite_in_memory.dbEngine.execute("select * from car_make")
#for row in resultSet.fetchall():
#    print(row)
