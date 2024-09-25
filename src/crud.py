from parse_args import app_arg
import logging

from sqlalchemy import func, select, label, desc, and_

from database.db import session
from database.models import Student, Teacher, Group, Grade, Discipline

package_name = "hw"
logger = logging.getLogger(package_name)


def get_query_dict(query, id = None):
    column_names = query.statement.columns.keys()
    if id is None:
        result = query.all()
        result_list = []
        for r in result:
            result_list.append({ col: r.__dict__[col] for col in column_names })
    else:
        result = query.get(id)
        result_list = [{ col: result.__dict__[col] for col in column_names }]
    return {"column_names": column_names, "result": result_list}


def action_create(kwargs):
    # print(kwargs)
    id = kwargs.get("id")
    group_id = kwargs.get("group_id")
    teacher_id = kwargs.get("tid")
    student_id = kwargs.get("sid")
    discipline_id = kwargs.get("did")
    grade = kwargs.get("grade")
    date_of = kwargs.get("date")
    model = kwargs.get("model")
    name: str = kwargs.get("name")
    if name:
        first_name, last_name = name.split(maxsplit=2)
    email = kwargs.get("email")
    address = kwargs.get("address")
    if not model:
         return "model name undefined"
    match model.lower():
        case "teacher":
            if not name:
                return "Missed name"
            teacher = Teacher(first_name=first_name, last_name=last_name, email=email, address=address, id=id)
            session.add(teacher)
            try:
                session.commit()
            except Exception as e:
                return f"ERROR: {e}"

            if teacher.id:
                result = f"Done. Created record with ID: {teacher.id}"
            else:
                result = "ERROR of CREATE"
            return result
  
        case "student":
            if not name:
                return "Missed name"
            student = Student(first_name=first_name, last_name=last_name, email=email, address=address, id=id, group_id = group_id)
            session.add(student)
            try:
                session.commit()
            except Exception as e:
                return f"ERROR: {e}"
            if student.id:
                result = f"Done. Created record with ID: {student.id}"
            else:
                result = "ERROR of CREATE"
            return result
        
        case "group":
            if not name:
                return "Missed name"
            group = Group(
                name=name, id=id
            )
            session.add(group)
            try:
                session.commit()
            except Exception as e:
                return f"ERROR: {e}"
            if group.id:
                result = f"Done. Created record with ID: {group.id}"
            else:
                result = "ERROR of CREATE"
            return result
        
        case "discipline":
            if not name:
                return "Missed name"
            discipline = Discipline(
                id=id,
                name=name,
                teacher_id=teacher_id
            )
            session.add(discipline)
            try:
                session.commit()
            except Exception as e:
                return f"ERROR: {e}"
            if discipline.id:
                result = f"Done. Created record with ID: {discipline.id}"
            else:
                result = "ERROR of CREATE"
            return result
    
        case "gardes":
            if not name:
                return "Missed name"
            grade = Grade(
                id=id,
                grade=grade,
                student_id=student_id,
                discipline_id=discipline_id,
                date_of=date_of,
            )
            session.add(discipline)
            try:
                session.commit()
            except Exception as e:
                return f"ERROR: {e}"
            if grade.id:
                result = f"Done. Created record with ID: {grade.id}"
            else:
                result = "ERROR of CREATE"
            return result     
        
            
        case "*":
            return "model name undefined"

def action_list(kwargs):
    id = kwargs.get("id")
    limit = kwargs.get("limit")    
    model = kwargs.get("model")
    if not model:
         return "model name undefined"
    match model.lower():
        case "teacher":
            try:
                query  = session.query(Teacher).limit(limit)
                result = get_query_dict(query, id)
            except Exception as e:
                return f"ERROR: {e}"
            return result
  
        case "student":
            try:
                query  = session.query(Student).limit(limit)
                result = get_query_dict(query, id)
            except Exception as e:
                return f"ERROR: {e}"
            return result
        
        case "group":
            try:
                query  = session.query(Group).limit(limit)
                result = get_query_dict(query, id)
            except Exception as e:
                return f"ERROR: {e}"
            return result
        
        case "discipline":
            try:
                query  = session.query(Discipline).limit(limit)
                result = get_query_dict(query, id)
            except Exception as e:
                return f"ERROR: {e}"
            return result
    
        case "grade":
            try:
                query  = session.query(Grade).limit(limit)
                result = get_query_dict(query, id)
            except Exception as e:
                return f"ERROR: {e}"
            return result
        
            
        case "*":
            return "model name implemented"




def action_update():
    return "not implemented"


def action_remove():
    return "not implemented"


ACTIONS_LIST = {
    "create": action_create,
    "list" : action_list,
    "update" : action_update,
    "remove": action_remove
}

def check_action(command: str) -> bool:
    return command in ACTIONS_LIST


def do_commnds(args):
    action = args.get("action")
    if not check_action(action):
        return f"Commnads unknown. List of commands: {tuple(ACTIONS_LIST)}"
    action_fun = ACTIONS_LIST.get(action)
    if action_fun:
        return action_fun(args)
        
        



"""
    --action create -m Teacher --name 'Boris Jonson' створення вчителя
    --action list -m Teacher показати всіх вчителів
    --action update -m Teacher --id 3 --name 'Andry Bezos' оновити дані вчителя з id=3
    --action remove -m Teacher --id 3 видалити вчителя з id=3
"""

if __name__ == "__main__":

    args = app_arg()
    result = do_commnds(args)
    print(result)