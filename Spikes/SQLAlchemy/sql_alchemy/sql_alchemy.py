from sqlite import sqlite_in_memory


resultSet = sqlite_in_memory.dbEngine.execute("select * from car_model")
for row in resultSet.fetchall():
    print(row)
