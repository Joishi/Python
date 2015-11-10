from sqlite import sqlite_in_memory
from orm_base import Base, CarMake, CarModel
from sqlalchemy.orm import Session

Base.metadata.create_all(sqlite_in_memory.dbEngine)
session = Session(bind=sqlite_in_memory.dbEngine)

chevrolet = CarMake(car_make_id=1, car_make_name="CHEVROLET")
toyota = CarMake(car_make_id=2, car_make_name="TOYOTA")
session.add(chevrolet)
session.add(toyota)

resultSet = session.query(CarMake)
for row in resultSet.all():
    print(row)

#resultSet = sqlite_in_memory.dbEngine.execute("select * from car_make")
#for row in resultSet.fetchall():
#    print(row)
