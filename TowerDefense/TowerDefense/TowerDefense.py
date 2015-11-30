from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import tkinter
from database import seed_data, orm
from mvc import model, view

def main():
    print("Creating DB Engine")
    dbEngine = create_engine("sqlite://")
#    dbEngine = create_engine("postgres://devtbsp:devtbsp@localhost/devtbsp")
    print("Creating Schema")
    orm.SQLAlchemyBase.metadata.create_all(dbEngine)
    session = Session(bind=dbEngine)
    seedData = seed_data.SeedData()
    print("Creating seed data")
    seedData.createSeedData(session)
    print("Getting a list of game stages")
    gameStages = session.query(orm.GameStage).all()
    print("Creating main model")
    mainModel =  model.MainModel()
#    mainView = view.MainView(tkinter.Tk())
    print("Creating main view")
    mainView = view.MainView()
#    mainView.model = mainModel
#    mainView.gameStages = gameStages
#    mainView.run()
    return

print("Running TowerDefense")

if __name__ == "__main__":
    print("Running main")
    main()
    print("Main completed")

print("Exiting TowerDefense")
