import configparser
from pathlib import Path
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

package_name="hw"
logger = logging.getLogger(package_name)


def read_config() -> str:
    file_config = (
        Path(__file__).parent.parent.parent.joinpath(".config").joinpath("config.ini")
    )
    if not file_config.exists():
        logger.error(f"CONFIG NOT FOUND {file_config}")
        return None

    config = configparser.ConfigParser()
    config.read(file_config)
    if "DB" not in config.sections():
        logger.error("CONFIG READ ERROR SECTION [DB]")
        return False
    section_db = config["DB"]
    host = section_db.get("host")
    port = section_db.get("port")
    database_name = section_db.get("db_name")
    username = section_db.get("username")
    password = section_db.get("password")
    uri = f"postgresql://{username}:{password}@{host}:{port}/{database_name}"
    return uri


def get_engine():
    uri = read_config()
    if  uri:
        engine = create_engine(uri, echo=True)
        DBsession = sessionmaker(bind=engine)
        session = DBsession()
        return engine, session, uri
    return None,None, None


engine, session, uri = get_engine()
logger.debug("session created")

if not engine:
    logger.error("engine not created")
