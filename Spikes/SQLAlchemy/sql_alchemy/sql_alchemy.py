from sqlalchemy import create_engine

dbEngine = create_engine("postgres://devtbsp:devtbsp@localhost:5432")
resultSet = dbEngine.execute("select * from sql_al.car_model")
for row in resultSet.fetchall():
    print(row)
