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
    for gameStage in session.query(orm.GameStage).all():
        print(gameStage)
        for waveLevel in gameStage.waves:
            print("  " + str(waveLevel))
            for creep in waveLevel.wave.creeps:
                print("    " + str(creep))

if __name__ == "__main__":
    main()
