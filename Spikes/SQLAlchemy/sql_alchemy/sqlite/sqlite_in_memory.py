from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, BigInteger, String, ForeignKey


# in memory sqlite db
dbEngine = create_engine("sqlite://")

# define database structure
'''
dbMetaData = MetaData()
makeTable = Table("car_make", dbMetaData,
                    Column("car_make_id", BigInteger, primary_key=True),
                    Column("car_make_name", String(60), nullable=False)
                  )

modelTable = Table("car_model", dbMetaData,
                    Column("car_model_id", BigInteger, primary_key=True),
                    Column("car_make_id", BigInteger, ForeignKey("car_make.car_make_id"), nullable=False),
                    Column("car_model_name", String(60), nullable=False)
                   )

dbMetaData.create_all(dbEngine)

dbEngine.execute("insert into car_make (car_make_id, car_make_name) values (1, 'CHEVROLET'), (2, 'FORD'), (3, 'TOYOTA'), (4, 'HYUNDAI')")
dbEngine.execute("insert into car_model (car_model_id, car_make_id, car_model_name) values (1, 1, 'AVEO'), (2, 1, 'CAVALIER'), (3, 3,'PRIUS')")
'''
