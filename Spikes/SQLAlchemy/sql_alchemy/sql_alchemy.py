from sqlite import sqlite_in_memory
from orm_base import Base, CarMake, CarModel, CarOwner, Car
from sqlalchemy.orm import Session

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

resultSet = session.query(CarMake)
for row in resultSet.all():
    print(row, row.car_models)

resultSet = session.query(CarModel)
for row in resultSet.all():
    print(row, row.cars)

resultSet = session.query(CarOwner)
for row in resultSet.all():
    print(row, row.cars)

resultSet = session.query(Car)
for row in resultSet.all():
    print(row)

#resultSet = sqlite_in_memory.dbEngine.execute("select * from car_make")
#for row in resultSet.fetchall():
#    print(row)
