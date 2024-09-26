import sys
import os

from sqlalchemy import select, delete

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from database.db import session
from database.models import Grade, Student, Discipline, Group

from faker import Faker
from datetime import date, datetime
from random import randint, choice
import logging

package_name = "hw"
logger = logging.getLogger(f"{package_name}.{__name__}")
fake = Faker()

TOTAL_GRADES_DAYS = 400


def erase_grades():
    deleted_gardes = session.execute(delete(Grade))
    logger.info(f"{deleted_gardes=}")


def select_groups():
    return session.execute(select(Group.id)).all()

def select_students():
    return session.execute(select(Student.id)).all()


def select_students_in_group(group_id: int):
    return session.execute(select(Student.id).filter_by(group_id=group_id)).all()


def select_disciplines():
    return session.execute(select(Discipline.id)).all()


def get_random_day() -> date:
    satrt_date = datetime.strptime("2023-04-21", "%Y-%m-%d")
    end_date = datetime.strptime("2024-02-20", "%Y-%m-%d")

    fake_day: date
    while True:
        fake_day = fake.date_between(satrt_date, end_date)
        if fake_day.isoweekday() < 6:
            break
    return fake_day


def create_gardes(total: int = TOTAL_GRADES_DAYS):
    groups = select_groups()
    if not groups:
        logger.error("GROUPS NOT FOUND")
        return
    students = select_students()
    if not students:
        logger.error("students NOT FOUND")
        return
    disciplines = select_disciplines()
    if not disciplines:
        logger.error("disciplines NOT FOUND")
        return

    erase_grades()
    grade_day = 0
    while True:
        random_discipline = choice(disciplines).id
        group_id = choice(groups).id
        group_students = select_students_in_group(group_id)
        group_students_id = [st.id for st in group_students]
        max_random_students_in_group = min(12, len(group_students))
        min_random_students_in_group = min(3, len(group_students))
        random_date_of = get_random_day()
        how_many_grades_today_in_group = randint(
            min_random_students_in_group, max_random_students_in_group
        )
        for _ in range(how_many_grades_today_in_group):
            random_grade = randint(30, 100)
            random_student = choice(group_students_id)
            grade = Grade(
                grade=random_grade,
                student_id=random_student,
                discipline_id=random_discipline,
                date_of=random_date_of,
            )
            session.add(grade)
        grade_day += 1
        if grade_day >= total:
            break
    session.commit()
    logger.info(f"{grade_day=}")

if __name__ == "__main__":
    create_gardes()
