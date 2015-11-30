from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database import seed_data
from database import orm

def main():
    dbEngine = create_engine("sqlite://")
    orm.SQLAlchemyBase.metadata.create_all(dbEngine)
    session = Session(bind=dbEngine)
    seedData = seed_data.SeedData()
    seedData.createSeedData(session)
    for row in session.query(orm.Path).all():
        print(row)
    for row in session.query(orm.Point).all():
        print(row)
    for row in session.query(orm.PathPoint).all():
        print(row)

if __name__ == "__main__":
    main()
