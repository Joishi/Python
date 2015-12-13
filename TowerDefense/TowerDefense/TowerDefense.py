import threading
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
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
    mainView = view.MainView()
    uiThread = threading.Thread(target=mainView.show)
    uiThread.start()
    mainModel =  model.MainModel()
    mainModel.gameStages = gameStages
    mainView.model = mainModel
    return


if __name__ == "__main__":
    main()

