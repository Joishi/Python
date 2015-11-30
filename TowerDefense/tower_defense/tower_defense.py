from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import tkinter
from database import seed_data, orm
from gui import gui

def main():
    dbEngine = create_engine("sqlite://")
#    dbEngine = create_engine("postgres://devtbsp:devtbsp@localhost/devtbsp")
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
    mainGui = gui.MainGUI(tkinter.Tk())
    mainGui.run()

if __name__ == "__main__":
    main()
