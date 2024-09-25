import argparse
from pathlib import Path


def app_arg():
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--action", help="Action")
    ap.add_argument("-m","--model", help="What model modify", choices=[
       "Teacher", "Student", "Discipline", "Grade", 
    ])

    ap.add_argument("-n, ","--name", help="Name or Full name")    
    ap.add_argument("-e","--email", help="Email")
    ap.add_argument("-p","--phone", help="Phone")
    ap.add_argument("-addr", "--address", help="Address")
    ap.add_argument("--id", help="ID of record",  type=int)
    ap.add_argument("--sid", help="Student ID record",  type=int)
    ap.add_argument("--tid", help="Teacher ID record", type=int)
    ap.add_argument("--did", help="Discipline ID record", type=int)
    ap.add_argument("--grade", help="grade", type=int)
    ap.add_argument("--date", help="date of grade")
    ap.add_argument("--limit", help="limit of results", type=int)

    args = vars(ap.parse_args())
    # print(f"{args=}")
    return args
