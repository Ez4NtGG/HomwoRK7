import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import random
import logging


from database.db import session
from database.models import Discipline
from database.models import Teacher


package_name="hw"
logger = logging.getLogger(f"{package_name}.{__name__}")

DISCIPLINES = [
    "Python Core",
    "Python Web",
    "Python Data Science",
    "Вища математика",
    "HTML CSS",
    "Soft Skils",
    "Databases SQL, noSQL",
    "English",
    "Git",
    "Історія України",
    "Ділова українська мова",
    "Філософія",
]


def erase_disciplines():
    deleted_disciplines = session.query(Discipline).delete()
    logger.info(f"{deleted_disciplines=}")


def select_teachers():
    return session.query(Teacher).all()


def create_disciplines():
    teachers = select_teachers()
    if not teachers:
        logger.error("Teachers NOT FOUND")
        return
    erase_disciplines()
    for discipline_name in DISCIPLINES:
        discipline = Discipline(
            name=discipline_name,
            teacher_id=random.choice(teachers).id
        )
        session.add(discipline)
    session.commit()


if __name__ == "__main__":
    create_disciplines()
