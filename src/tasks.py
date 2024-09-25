import logging

from sqlalchemy import func, select, label, desc, and_

from database.db import session
from database.models import Student, Teacher, Group, Grade, Discipline

package_name = "hw"
logger = logging.getLogger(package_name)


def get_tasks(obj=None):
    if obj is None:
        obj = globals()
    tasks = [
        globals().get(task_str)
        for task_str in filter(lambda x: x.startswith("task_"), obj)
    ]
    return tasks


def get_query_dict(query):
    return {"column_names": query.statement.columns.keys(), "result": query.all()}


def task_01(*args, **kwargs):
    """
    SELECT s.fullname as student, ROUND(AVG(grade),2) as average_grade
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5
    """
    query = (
        session.query(
            func.CONCAT(Student.first_name, " ", Student.last_name).label("Student"),
            func.ROUND(func.AVG(Grade.grade), 2).label("Average grade"),
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc("Average grade"))
        .limit(5)
    )
    return get_query_dict(query)


def task_02(*args, **kwargs):
    """
    SELECT d.name AS discipline, s.fullname as student, ROUND(AVG(grade),2) as average_garde
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id
    LEFT JOIN disciplines d ON g.disciplines_id = d.id
    WHERE g.disciplines_id = 2
    GROUP BY s.id
    ORDER BY average_garde DESC
    LIMIT 1
    """
    discipline_id = kwargs.get("discipline_id", 2)
    query = (
        session.query(
            label("Discipline", Discipline.name),
            func.CONCAT(Student.first_name, " ", Student.last_name).label("Student"),
            func.ROUND(func.AVG(Grade.grade), 2).label("Average grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .filter(Discipline.id == discipline_id)
        .group_by(Student.id, Discipline.name)
        .order_by(desc("Average grade"))
        .limit(1)
    )
    return get_query_dict(query)


def task_03(*args, **kwargs):
    """
    SELECT  d.name AS discipline, gr.name AS [group], ROUND(AVG(grade),2) as average_garde
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id
    LEFT JOIN disciplines d ON g.disciplines_id = d.id
    LEFT JOIN groups gr ON s.group_id = gr.id
    WHERE g.disciplines_id = 2
    GROUP BY gr.id
    ORDER BY average_garde DESC
    """
    discipline_id = kwargs.get("discipline_id", 2)
    query = (
        session.query(
            label("Discipline", Discipline.name),
            label("Group", Group.name),
            func.ROUND(func.AVG(Grade.grade), 2).label("Average grade"),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .join(Group)
        .filter(Discipline.id == discipline_id)
        .group_by(Student.id, Discipline.name, Group.name)
        .order_by(desc("Average grade"))
        .limit(1)
    )
    return get_query_dict(query)


def task_04(*args, **kwargs):
    """
    SELECT ROUND(AVG(grade),2) as average_garde
    FROM grade
    ORDER BY average_garde DESC
    """
    discipline_id = kwargs.get("discipline_id", 2)
    query = session.query(
        func.ROUND(func.AVG(Grade.grade), 2).label("Average grade"),
    ).order_by(desc("Average grade"))
    return get_query_dict(query)


def task_05(*args, **kwargs):
    """
    SELECT t.fullname AS teacher, d.name AS discipline
    FROM grade g
    LEFT JOIN disciplines d ON g.disciplines_id  = d.id
    LEFT JOIN teachers t ON d.teachers_id = t.id
    WHERE t.id = 1
    GROUP BY d.id
    """
    teacher_id = kwargs.get("teacher_id", 10)
    query = (
        session.query(
            label("Discipline", Discipline.name),
            func.CONCAT(Teacher.first_name, " ", Teacher.last_name).label("Teacher"),
        )
        .select_from(Discipline)
        .join(Teacher)
        .filter(Teacher.id == teacher_id)
        .order_by(Discipline.name)
    )
    return get_query_dict(query)


def task_06(*args, **kwargs):
    """
    SELECT gr.name as [group] , s.fullname as student, REVERSE(SUBSTR(REVERSE(s.fullname), 0, CHARINDEX(' ', REVERSE(s.fullname)))) AS last_name
    FROM students s
    LEFT JOIN groups gr ON s.group_id = gr.id
    WHERE group_id = 1
    ORDER BY last_name
    """
    group_id = kwargs.get("group_id", 1)
    query = (
        session.query(
            label("Group", Group.name),
            func.CONCAT(Student.first_name, " ", Student.last_name).label("Student"),
        )
        .select_from(Student)
        .join(Group)
        .filter(Group.id == group_id)
        .order_by(Student.last_name)
    )
    return get_query_dict(query)


def task_07(*args, **kwargs):
    """
    SELECT s.fullname as student, d.name AS discipline, gr.name AS [group], grade
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id
    LEFT JOIN disciplines d ON g.disciplines_id = d.id
    LEFT JOIN groups gr ON s.group_id = gr.id
    WHERE d.id = 1 AND gr.id = 1
    ORDER BY grade DESC
    """
    discipline_id = kwargs.get("discipline_id", 1)
    group_id = kwargs.get("group_id", 1)
    query = (
        session.query(
            func.CONCAT(Student.first_name, " ", Student.last_name).label("Student"),
            label("Group", Group.name),
            label("Discipline", Discipline.name),
            label("Grade", Grade.grade),
        )
        .select_from(Grade)
        .join(Student)
        .join(Discipline)
        .filter(and_(Group.id == group_id, Discipline.id == discipline_id))
        .order_by(desc(Grade.grade))
    )
    return get_query_dict(query)


def task_08(*args, **kwargs):
    """
    SELECT t.fullname AS teacher, d.name AS discipline, ROUND(AVG(grade),2) as average_garde
    FROM grade g
    LEFT JOIN disciplines d ON g.disciplines_id  = d.id
    LEFT JOIN teachers t ON d.teachers_id = t.id
    WHERE t.id = 1
    GROUP BY d.id
    """
    teacher_id = kwargs.get("teacher_id", 8)
    query = (
        session.query(
            func.CONCAT(Teacher.first_name, " ", Teacher.last_name).label("Teacher"),
            label("Discipline", Discipline.name),
            func.ROUND(func.AVG(Grade.grade), 2).label("Average grade"),
        )
        .select_from(Grade)
        .join(Discipline)
        .join(Teacher)
        .filter(Teacher.id == teacher_id)
        .group_by(Discipline.id, Teacher.first_name, Teacher.last_name)
        .order_by(desc("Average grade"))
    )
    return get_query_dict(query)


def task_09(*args, **kwargs):
    """
    SELECT  s.fullname as student, d.name AS discipline
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id
    LEFT JOIN disciplines d ON g.disciplines_id = d.id
    WHERE s.id = 3
    GROUP BY discipline
    ORDER BY discipline
    """
    student_id = kwargs.get("student_id", 1)
    query = (
        session.query(
            func.CONCAT(Student.first_name, " ", Student.last_name).label("Student"),
            label("Discipline", Discipline.name),
        )
        .select_from(Grade)
        .join(Discipline)
        .join(Student)
        .filter(Student.id == student_id)
        .group_by(Discipline.id, Student.first_name, Student.last_name)
        .order_by(Discipline.name)
    )
    return get_query_dict(query)


def task_10(*args, **kwargs):
    """
    SELECT d.name AS discipline, s.fullname as student, t.fullname AS teacher
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id
    LEFT JOIN disciplines d ON g.disciplines_id = d.id
    LEFT JOIN teachers t ON d.teachers_id = t.id
    WHERE s.id = 3 AND t.id = 1
    GROUP BY discipline
    ORDER BY discipline
    """
    student_id = kwargs.get("student_id", 5)
    teacher_id = kwargs.get("teacher_id", 8)

    query = (
        session.query(
            label("Discipline", Discipline.name),
            func.CONCAT(Student.first_name, " ", Student.last_name).label("Student"),
            func.CONCAT(Teacher.first_name, " ", Teacher.last_name).label("Teacher"),
        )
        .select_from(Grade)
        .join(Discipline)
        .join(Student)
        .join(Teacher)
        .filter(and_(Student.id == student_id, Teacher.id == teacher_id))
        .group_by(Discipline.id, "Student", "Teacher")
        .order_by(Discipline.name)
    )
    return get_query_dict(query)


def task_11(*args, **kwargs):
    """
    SELECT d.name AS discipline, s.fullname as student, t.fullname AS teacher, ROUND(AVG(grade),2) as average_garde
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id
    LEFT JOIN disciplines d ON g.disciplines_id = d.id
    LEFT JOIN teachers t ON d.teachers_id = t.id
    WHERE s.id = 3 AND t.id = 1
    GROUP BY discipline
    ORDER BY average_garde DESC
    """
    student_id = kwargs.get("student_id", 5)
    teacher_id = kwargs.get("teacher_id", 8)

    query = (
        session.query(
            label("Discipline", Discipline.name),
            func.CONCAT(Student.first_name, " ", Student.last_name).label("Student"),
            func.CONCAT(Teacher.first_name, " ", Teacher.last_name).label("Teacher"),
            func.ROUND(func.AVG(Grade.grade), 2).label("Average grade"),
        )
        .select_from(Grade)
        .join(Discipline)
        .join(Student)
        .join(Teacher)
        .filter(and_(Student.id == student_id, Teacher.id == teacher_id))
        .group_by(Discipline.id, "Student", "Teacher")
        .order_by(desc("Average grade"))
    )
    return get_query_dict(query)


def task_12(*args, **kwargs):
    """
    SELECT gr.name AS [group], d.name AS discipline, s.fullname as student, t.fullname AS teacher, grade, date_of
    FROM grade g
    LEFT JOIN students s ON s.id = g.students_id
    LEFT JOIN disciplines d ON g.disciplines_id = d.id
    LEFT JOIN teachers t ON d.teachers_id = t.id
    LEFT JOIN groups gr ON s.group_id = gr.id
    WHERE gr.id = 3 AND d.id = 1
    AND date_of = (
        SELECT MAX(date_of)
        FROM grade g
        LEFT JOIN students s ON s.id = g.students_id
        WHERE s.group_id = 3 AND g.disciplines_id = 1
    )
    ORDER BY grade DESC;
    """
    discipline_id = kwargs.get("discipline_id", 1)
    group_id = kwargs.get("group_id", 1)

    subquery = (
        session.query(func.MAX(Grade.date_of))
        .select_from(Grade)
        .join(Student)
        .filter(
            and_(Student.group_id == group_id, Grade.discipline_id == discipline_id)
        )
    ).scalar_subquery()

    query = (
        session.query(
            label("Group", Group.name),
            label("Discipline", Discipline.name),
            func.CONCAT(Student.first_name, " ", Student.last_name).label("Student"),
            func.CONCAT(Teacher.first_name, " ", Teacher.last_name).label("Teacher"),
            label("DATE OF", Grade.date_of),
            label("Grade", Grade.grade),
        )
        .select_from(Grade)
        .join(Discipline)
        .join(Student)
        .join(Teacher)
        .filter(
            and_(
                Group.id == group_id,
                Grade.discipline_id == discipline_id,
                Grade.date_of == subquery,
            )
        )
        .order_by(desc("Grade"))
    )
    return get_query_dict(query)


if __name__ == "__main__":
    # print(globals())
    # print(dir())
    # tasks = get_tasks(dir())
    # [task() for task in tasks]
    # func = getattr(globals, tasks[0])
    # func = globals().get(tasks[0])
    # func()
    for task in get_tasks():
        print("-" * 80)
        print(task.__name__)
        task_result = task()
        if task_result:
            column_names = task_result.get("column_names")
            print(".   " * 20)
            for id, row in enumerate(task_result.get("result")):
                row_str = []
                for i, col in enumerate(row):
                    row_str.append(f'{column_names[i]}: "{col}"')
                result = ", ".join(row_str)
                print(f"[{id+1:2}] {result}")
