import threading, logging
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database import seed_data, orm
from mvc import model, view

def main():
    initializeLogger()
    dbEngine = create_engine("sqlite://")
#    dbEngine = create_engine("postgres://devtbsp:devtbsp@localhost/devtbsp")
    orm.SQLAlchemyBase.metadata.create_all(dbEngine)
    session = Session(bind=dbEngine)
    seedData = seed_data.SeedData()
    seedData.createSeedData(session)
    gameStages = session.query(orm.GameStage).all()
    mainView = view.MainView("openGL view")
    uiThread = threading.Thread(target=mainView.show)
    uiThread.start()
    mainModel =  model.MainModel("model for openGL view")
    mainModel.gameStages = gameStages
    mainView.model = mainModel
    return


# from https://aykutakin.wordpress.com/2013/08/06/logging-to-console-and-file-in-python/
def initializeLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
     
    # create console handler and set level to info
    handler = logging.StreamHandler()
#    handler.setLevel(logging.INFO)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
 
    # create error file handler and set level to error
#    handler = logging.FileHandler(os.path.join(output_dir, "error.log"),"w", encoding=None, delay="true")
#    handler.setLevel(logging.ERROR)
#    formatter = logging.Formatter("%(levelname)s - %(message)s")
#    handler.setFormatter(formatter)
#    logger.addHandler(handler)
 
    # create debug file handler and set level to debug
#    handler = logging.FileHandler(os.path.join(output_dir, "all.log"),"w")
#    handler.setLevel(logging.DEBUG)
#    formatter = logging.Formatter("%(levelname)s - %(message)s")
#    handler.setFormatter(formatter)
#    logger.addHandler(handler)


if __name__ == "__main__":
    main()

