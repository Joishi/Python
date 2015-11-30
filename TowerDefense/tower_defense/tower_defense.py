from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import tkinter
from database import seed_data, orm
from mvc import model, view

def main():
    dbEngine = create_engine("sqlite://")
#    dbEngine = create_engine("postgres://devtbsp:devtbsp@localhost/devtbsp")
    orm.SQLAlchemyBase.metadata.create_all(dbEngine)
    session = Session(bind=dbEngine)
    seedData = seed_data.SeedData()
    seedData.createSeedData(session)
    gameStages = session.query(orm.GameStage).all()
    mainModel =  model.MainModel()
    mainView = view.MainView(tkinter.Tk())
    mainView.model = mainModel
    mainView.gameStages = gameStages
    mainView.run()

if __name__ == "__main__":
    main()
