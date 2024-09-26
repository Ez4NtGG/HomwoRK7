try:
    from seed.teachers import create_teachers
    from seed.disciplines import create_disciplines
    from seed.groups import create_groups
    from seed.students import create_students
    from seed.grades import create_gardes
except ImportError:
    from teachers import create_teachers
    from disciplines import create_disciplines
    from groups import create_groups
    from students import create_students
    from grades import create_gardes

import logging

package_name="hw"
logger = logging.getLogger(f"{package_name}.{__name__}")


def create_data():
    create_teachers()
    create_disciplines()
    create_groups()
    create_students()
    create_gardes()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    create_data()