# goit_python_web_hw_07

GoIT, Python WEB, Homework number 07. SQL. ORM. SQLAlchemy. Alembic.

## Вступна

У цьому домашньому завданні ми продовжимо працювати з домашнім завданням із попереднього модуля.

В цій домашній роботі використаємо базу даних postgres. У командному рядку запустіть Docker контейнер:

`docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres`

Замість some-postgres виберіть свою назву контейнера, а замість mysecretpassword придумайте свій пароль для підключення до бази даних

## Кроки виконання домашнього завдання

### Перший крок

Реалізуйте свої моделі SQLAlchemy, для таблиць:

 - Таблиця студентів;
 - Таблиця груп;
 - Таблиця викладачів;
 - Таблиця предметів із вказівкою викладача, який читає предмет;
 - Таблиця де кожен студент має оцінки з предметів із зазначенням коли оцінку отримано;

### Другий крок

Використовуйте `alembic` для створення міграцій у базі даних.

### Третій крок

Напишіть скрипт `seed.py` та заповніть отриману базу даних випадковими даними (~30-50 студентів, 3 групи, 5-8 предметів, 3-5 викладачів, до 20 оцінок у кожного студента з усіх предметів). Використовуйте пакет Faker для наповнення. При заповненні використовуємо механізм сесій `SQLAlchemy`.

### Четвертий крок

Зробити такі вибірки з отриманої бази даних:

 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
 2. Знайти студента із найвищим середнім балом з певного предмета.
 3. Знайти середній бал у групах з певного предмета.
 4. Знайти середній бал на потоці (по всій таблиці оцінок).
 5. Знайти які курси читає певний викладач.
 6. Знайти список студентів у певній групі.
 7. Знайти оцінки студентів у окремій групі з певного предмета.
 8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
 9. Знайти список курсів, які відвідує певний студент.
10. Список курсів, які певному студенту читає певний викладач.


## Додаткове завдання
### Перша частина

Для додаткового завдання зробіть такі запити підвищеної складності:

 11. Середній бал, який певний викладач ставить певному студентові.
 12. Оцінки студентів у певній групі з певного предмета на останньому занятті.

### Друга частина

Замість скрипту seed.py подумайте та реалізуйте повноцінну CLI програму для CRUD операцій із базою даних. Використовуйте для цього модуль argparse .

Використовуйте команду `--action` або скорочений варіант -a для CRUD операцій. Та команду `--model` (-m) для вказівки над якою моделлю проводитися операція.

Приклад:

    --action create -m Teacher --name 'Boris Jonson' створення вчителя
    --action list -m Teacher показати всіх вчителів
    --action update -m Teacher --id 3 --name 'Andry Bezos' оновити дані вчителя з id=3
    --action remove -m Teacher --id 3 видалити вчителя з id=3- Знайти студента із найвищим середнім балом з певного предмета.
 


## ВИКОНАННЯ

### run
python src/main.py
```
--------------------------------------------------------------------------------
task_01
2023-10-03 00:12:40,913 INFO sqlalchemy.engine.Engine select pg_catalog.version()
2023-10-03 00:12:40,913 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-10-03 00:12:40,917 INFO sqlalchemy.engine.Engine select current_schema()
2023-10-03 00:12:40,917 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-10-03 00:12:40,919 INFO sqlalchemy.engine.Engine show standard_conforming_strings
2023-10-03 00:12:40,919 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-10-03 00:12:40,919 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-10-03 00:12:40,949 INFO sqlalchemy.engine.Engine SELECT concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", ROUND(AVG(grades.grade), %(ROUND_1)s) AS "Average grade"
FROM grades JOIN students ON students.id = grades.student_id GROUP BY students.id ORDER BY "Average grade" DESC
 LIMIT %(param_1)s
2023-10-03 00:12:40,949 INFO sqlalchemy.engine.Engine [generated in 0.00115s] {'concat_1': ' ', 'ROUND_1': 2, 'param_1': 5}
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
[ 1] Student: "Юхим Удовиченко", Average grade: "77.31"
[ 2] Student: "Еріка Дзиндра", Average grade: "76.76"
[ 3] Student: "Аліна Устенко", Average grade: "74.82"
[ 4] Student: "Олег Оробець", Average grade: "74.22"
[ 5] Student: "Кирило Височан", Average grade: "73.88"
--------------------------------------------------------------------------------
task_02
2023-10-03 00:12:40,966 INFO sqlalchemy.engine.Engine SELECT disciplines.name AS "Discipline", concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", ROUND(AVG(grades.grade), %(ROUND_1)s) AS "Average grade"
FROM grades JOIN students ON students.id = grades.student_id JOIN disciplines ON disciplines.id = grades.discipline_id
WHERE disciplines.id = %(id_1)s GROUP BY students.id, disciplines.name ORDER BY "Average grade" DESC
 LIMIT %(param_1)s
2023-10-03 00:12:40,966 INFO sqlalchemy.engine.Engine [generated in 0.00178s] {'concat_1': ' ', 'ROUND_1': 2, 'id_1': 2, 'param_1': 1}
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
[ 1] Discipline: "Python Web", Student: "Любов Ільєнко", Average grade: "95.50"
--------------------------------------------------------------------------------
task_03
2023-10-03 00:12:40,966 INFO sqlalchemy.engine.Engine SELECT disciplines.name AS "Discipline", groups.name AS "Group", ROUND(AVG(grades.grade), %(ROUND_1)s) AS "Average grade"
FROM grades JOIN students ON students.id = grades.student_id JOIN disciplines ON disciplines.id = grades.discipline_id JOIN groups ON groups.id = students.group_id
WHERE disciplines.id = %(id_1)s GROUP BY students.id, disciplines.name, groups.name ORDER BY "Average grade" DESC
 LIMIT %(param_1)s
2023-10-03 00:12:40,966 INFO sqlalchemy.engine.Engine [generated in 0.00094s] {'ROUND_1': 2, 'id_1': 2, 'param_1': 1}
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   
[ 1] Discipline: "Python Web", Group: "C89-1/8", Average grade: "95.50"
--------------------------------------------------------------------------------
task_04
2023-10-03 00:12:40,982 INFO sqlalchemy.engine.Engine SELECT ROUND(AVG(grades.grade), %(ROUND_1)s) AS "Average grade"
FROM grades ORDER BY "Average grade" DESC
2023-10-03 00:12:40,982 INFO sqlalchemy.engine.Engine [generated in 0.00063s] {'ROUND_1': 2}
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
[ 1] Average grade: "64.56"
--------------------------------------------------------------------------------
task_05
2023-10-03 00:12:40,982 INFO sqlalchemy.engine.Engine SELECT disciplines.name AS "Discipline", concat(teachers.first_name, %(concat_1)s, teachers.last_name) AS "Teacher"
FROM disciplines JOIN teachers ON teachers.id = disciplines.teacher_id
WHERE teachers.id = %(id_1)s ORDER BY disciplines.name
2023-10-03 00:12:40,982 INFO sqlalchemy.engine.Engine [generated in 0.00077s] {'concat_1': ' ', 'id_1': 10}
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   
[ 1] Discipline: "HTML CSS", Teacher: "Давид Цимбалюк"
[ 2] Discipline: "Python Core", Teacher: "Давид Цимбалюк"
[ 3] Discipline: "Вища математика", Teacher: "Давид Цимбалюк"
--------------------------------------------------------------------------------
task_06
2023-10-03 00:12:40,999 INFO sqlalchemy.engine.Engine SELECT groups.name AS "Group", concat(students.first_name, %(concat_1)s, students.last_name) AS "Student"
FROM students JOIN groups ON groups.id = students.group_id
WHERE groups.id = %(id_1)s ORDER BY students.last_name
2023-10-03 00:12:40,999 INFO sqlalchemy.engine.Engine [generated in 0.00095s] {'concat_1': ' ', 'id_1': 1}
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
[ 1] Group: "M88-1/8", Student: "Пантелеймон Бандура"
[ 2] Group: "M88-1/8", Student: "Ігор Єременко"
[ 3] Group: "M88-1/8", Student: "Панас Овсієнко"
[ 4] Group: "M88-1/8", Student: "Леон Перебийніс"
[ 5] Group: "M88-1/8", Student: "Аліна Устенко"
[ 6] Group: "M88-1/8", Student: "Андрій Цюпа"
--------------------------------------------------------------------------------
task_07
C:\Users\lexxa\Developments\GoIT\Python\Python 15\Web\goit_python_web_hw_07\src\tasks.py:23: SAWarning: SELECT statement has a cartesian product between FROM element(s) "students", "disciplines", "grades" and FROM element "groups".  Apply join condition(s) between each element to resolve.
  return {"column_names": query.statement.columns.keys(), "result": query.all()}
2023-10-03 00:12:41,007 INFO sqlalchemy.engine.Engine SELECT concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", groups.name AS "Group", disciplines.name AS "Discipline", grades.grade AS "Grade"
FROM grades JOIN students ON students.id = grades.student_id JOIN disciplines ON disciplines.id = grades.discipline_id, groups        
WHERE groups.id = %(id_1)s AND disciplines.id = %(id_2)s ORDER BY grades.grade DESC
2023-10-03 00:12:41,014 INFO sqlalchemy.engine.Engine [generated in 0.00111s] {'concat_1': ' ', 'id_1': 1, 'id_2': 1}
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
[ 1] Student: "Богданна Стельмах", Group: "M88-1/8", Discipline: "Python Core", Grade: "100"
[ 2] Student: "Варвара Верхола", Group: "M88-1/8", Discipline: "Python Core", Grade: "99"
[ 3] Student: "Панас Овсієнко", Group: "M88-1/8", Discipline: "Python Core", Grade: "99"
[ 4] Student: "Прохір Лагода", Group: "M88-1/8", Discipline: "Python Core", Grade: "99"
[ 5] Student: "Нестор Ярема", Group: "M88-1/8", Discipline: "Python Core", Grade: "98"
[ 6] Student: "Вікторія Гаврилишин", Group: "M88-1/8", Discipline: "Python Core", Grade: "98"
[ 7] Student: "Еріка Дзиндра", Group: "M88-1/8", Discipline: "Python Core", Grade: "98"
[ 8] Student: "Охрім Теліженко", Group: "M88-1/8", Discipline: "Python Core", Grade: "98"
[ 9] Student: "Ярина Ковалюк", Group: "M88-1/8", Discipline: "Python Core", Grade: "98"
[10] Student: "Яків Худобʼяк", Group: "M88-1/8", Discipline: "Python Core", Grade: "97"
[11] Student: "Ярема Гречаник", Group: "M88-1/8", Discipline: "Python Core", Grade: "97"
[12] Student: "Демʼян Андрійович", Group: "M88-1/8", Discipline: "Python Core", Grade: "97"
[13] Student: "Михайло Забара", Group: "M88-1/8", Discipline: "Python Core", Grade: "97"
[14] Student: "Тимофій Гайворонський", Group: "M88-1/8", Discipline: "Python Core", Grade: "96"
[15] Student: "Прохір Лагода", Group: "M88-1/8", Discipline: "Python Core", Grade: "96"
[16] Student: "Клавдія Артимович", Group: "M88-1/8", Discipline: "Python Core", Grade: "96"
[17] Student: "Тимофій Гайворонський", Group: "M88-1/8", Discipline: "Python Core", Grade: "95"
[18] Student: "Пантелеймон Бандура", Group: "M88-1/8", Discipline: "Python Core", Grade: "95"
[19] Student: "Нестор Ярема", Group: "M88-1/8", Discipline: "Python Core", Grade: "95"
[20] Student: "Гордій Приймак", Group: "M88-1/8", Discipline: "Python Core", Grade: "94"
[21] Student: "Едита Назаренко", Group: "M88-1/8", Discipline: "Python Core", Grade: "94"
[22] Student: "Ярина Габелко", Group: "M88-1/8", Discipline: "Python Core", Grade: "93"
[23] Student: "Павло Деревʼянко", Group: "M88-1/8", Discipline: "Python Core", Grade: "93"
[24] Student: "Ганна Опанасенко", Group: "M88-1/8", Discipline: "Python Core", Grade: "93"
[25] Student: "Едуард Батіг", Group: "M88-1/8", Discipline: "Python Core", Grade: "93"
[26] Student: "Соломія Копитко", Group: "M88-1/8", Discipline: "Python Core", Grade: "92"
[27] Student: "Едуард Батіг", Group: "M88-1/8", Discipline: "Python Core", Grade: "92"
[28] Student: "Тимофій Гайворонський", Group: "M88-1/8", Discipline: "Python Core", Grade: "92"
[29] Student: "Азар Артюх", Group: "M88-1/8", Discipline: "Python Core", Grade: "91"
[30] Student: "Трохим Бабко", Group: "M88-1/8", Discipline: "Python Core", Grade: "91"
[31] Student: "Мирон Гупало", Group: "M88-1/8", Discipline: "Python Core", Grade: "91"
[32] Student: "Світлана Василенко", Group: "M88-1/8", Discipline: "Python Core", Grade: "90"
[33] Student: "Соломія Копитко", Group: "M88-1/8", Discipline: "Python Core", Grade: "90"
[34] Student: "Варвара Верхола", Group: "M88-1/8", Discipline: "Python Core", Grade: "90"
[35] Student: "Варвара Верхола", Group: "M88-1/8", Discipline: "Python Core", Grade: "89"
[36] Student: "Вікторія Гаврилишин", Group: "M88-1/8", Discipline: "Python Core", Grade: "89"
[37] Student: "Клавдія Артимович", Group: "M88-1/8", Discipline: "Python Core", Grade: "88"
[38] Student: "Лукʼян Юрченко", Group: "M88-1/8", Discipline: "Python Core", Grade: "88"
[39] Student: "Тимофій Гайворонський", Group: "M88-1/8", Discipline: "Python Core", Grade: "87"
[40] Student: "Едита Назаренко", Group: "M88-1/8", Discipline: "Python Core", Grade: "86"
[41] Student: "Леон Наливайко", Group: "M88-1/8", Discipline: "Python Core", Grade: "86"
[42] Student: "Світлана Василенко", Group: "M88-1/8", Discipline: "Python Core", Grade: "85"
[43] Student: "Адам Алексюк", Group: "M88-1/8", Discipline: "Python Core", Grade: "85"
[44] Student: "Ігнат Гаврилишин", Group: "M88-1/8", Discipline: "Python Core", Grade: "85"
[45] Student: "Зорян Аронець", Group: "M88-1/8", Discipline: "Python Core", Grade: "83"
[46] Student: "Ярослав Арсенич", Group: "M88-1/8", Discipline: "Python Core", Grade: "82"
[47] Student: "Панас Овсієнко", Group: "M88-1/8", Discipline: "Python Core", Grade: "81"
[48] Student: "Іван Медведенко", Group: "M88-1/8", Discipline: "Python Core", Grade: "81"
[49] Student: "Андрій Цюпа", Group: "M88-1/8", Discipline: "Python Core", Grade: "80"
[50] Student: "Едуард Батіг", Group: "M88-1/8", Discipline: "Python Core", Grade: "80"
[51] Student: "Соломія Копитко", Group: "M88-1/8", Discipline: "Python Core", Grade: "80"
[52] Student: "Прохір Лагода", Group: "M88-1/8", Discipline: "Python Core", Grade: "79"
[53] Student: "Соломія Копитко", Group: "M88-1/8", Discipline: "Python Core", Grade: "79"
[54] Student: "Прохір Лагода", Group: "M88-1/8", Discipline: "Python Core", Grade: "79"
[55] Student: "Богданна Стельмах", Group: "M88-1/8", Discipline: "Python Core", Grade: "79"
[56] Student: "Василина Даниленко", Group: "M88-1/8", Discipline: "Python Core", Grade: "79"
[57] Student: "Остап Теличенко", Group: "M88-1/8", Discipline: "Python Core", Grade: "78"
[58] Student: "Ганна Опанасенко", Group: "M88-1/8", Discipline: "Python Core", Grade: "78"
[59] Student: "Алевтин Конопленко", Group: "M88-1/8", Discipline: "Python Core", Grade: "78"
[60] Student: "Оксана Арсенич", Group: "M88-1/8", Discipline: "Python Core", Grade: "77"
[61] Student: "Варвара Верхола", Group: "M88-1/8", Discipline: "Python Core", Grade: "77"
[62] Student: "Нестор Ярема", Group: "M88-1/8", Discipline: "Python Core", Grade: "76"
[63] Student: "Едита Назаренко", Group: "M88-1/8", Discipline: "Python Core", Grade: "76"
[64] Student: "Едуард Батіг", Group: "M88-1/8", Discipline: "Python Core", Grade: "76"
[65] Student: "Юстина Шамрай", Group: "M88-1/8", Discipline: "Python Core", Grade: "75"
[66] Student: "Володимира Карась", Group: "M88-1/8", Discipline: "Python Core", Grade: "75"
[67] Student: "Ярослав Арсенич", Group: "M88-1/8", Discipline: "Python Core", Grade: "75"
[68] Student: "Нестор Ярема", Group: "M88-1/8", Discipline: "Python Core", Grade: "75"
[69] Student: "Іван Медведенко", Group: "M88-1/8", Discipline: "Python Core", Grade: "74"
[70] Student: "Вікторія Гаврилишин", Group: "M88-1/8", Discipline: "Python Core", Grade: "74"
[71] Student: "Захар Затула", Group: "M88-1/8", Discipline: "Python Core", Grade: "74"
[72] Student: "Кирило Височан", Group: "M88-1/8", Discipline: "Python Core", Grade: "74"
[73] Student: "Тимофій Гайворонський", Group: "M88-1/8", Discipline: "Python Core", Grade: "72"
[74] Student: "Едуард Батіг", Group: "M88-1/8", Discipline: "Python Core", Grade: "72"
[75] Student: "Прохір Лагода", Group: "M88-1/8", Discipline: "Python Core", Grade: "72"
[76] Student: "Кирило Величко", Group: "M88-1/8", Discipline: "Python Core", Grade: "72"
[77] Student: "Оксана Арсенич", Group: "M88-1/8", Discipline: "Python Core", Grade: "72"
[78] Student: "Едуард Батіг", Group: "M88-1/8", Discipline: "Python Core", Grade: "71"
[79] Student: "Соломія Копитко", Group: "M88-1/8", Discipline: "Python Core", Grade: "71"
[80] Student: "Адам Алексюк", Group: "M88-1/8", Discipline: "Python Core", Grade: "71"
[81] Student: "Пилип Данчук", Group: "M88-1/8", Discipline: "Python Core", Grade: "71"
[82] Student: "Ярина Габелко", Group: "M88-1/8", Discipline: "Python Core", Grade: "70"
[83] Student: "Азар Артюх", Group: "M88-1/8", Discipline: "Python Core", Grade: "69"
[84] Student: "Варвара Верхола", Group: "M88-1/8", Discipline: "Python Core", Grade: "69"
[85] Student: "Прохір Чубай", Group: "M88-1/8", Discipline: "Python Core", Grade: "69"
[86] Student: "Аліна Устенко", Group: "M88-1/8", Discipline: "Python Core", Grade: "68"
[87] Student: "Мирон Адамчук", Group: "M88-1/8", Discipline: "Python Core", Grade: "68"
[88] Student: "Пармен Гаєвський", Group: "M88-1/8", Discipline: "Python Core", Grade: "68"
[89] Student: "Мирон Адамчук", Group: "M88-1/8", Discipline: "Python Core", Grade: "67"
[90] Student: "Зорян Аронець", Group: "M88-1/8", Discipline: "Python Core", Grade: "67"
[91] Student: "Андрій Цюпа", Group: "M88-1/8", Discipline: "Python Core", Grade: "65"
[92] Student: "Максим Дзиндра", Group: "M88-1/8", Discipline: "Python Core", Grade: "64"
[93] Student: "Алевтин Конопленко", Group: "M88-1/8", Discipline: "Python Core", Grade: "63"
[94] Student: "Михайло Забара", Group: "M88-1/8", Discipline: "Python Core", Grade: "63"
[95] Student: "Юхим Сірко", Group: "M88-1/8", Discipline: "Python Core", Grade: "62"
[96] Student: "Федір Павленко", Group: "M88-1/8", Discipline: "Python Core", Grade: "62"
[97] Student: "Маруся Баранець", Group: "M88-1/8", Discipline: "Python Core", Grade: "61"
[98] Student: "Кирило Височан", Group: "M88-1/8", Discipline: "Python Core", Grade: "61"
[99] Student: "Ігор Єременко", Group: "M88-1/8", Discipline: "Python Core", Grade: "61"
[100] Student: "Юхим Сірко", Group: "M88-1/8", Discipline: "Python Core", Grade: "61"
[101] Student: "Прохір Лагода", Group: "M88-1/8", Discipline: "Python Core", Grade: "60"
[102] Student: "Азар Артюх", Group: "M88-1/8", Discipline: "Python Core", Grade: "60"
[103] Student: "Георгій Мазур", Group: "M88-1/8", Discipline: "Python Core", Grade: "60"
[104] Student: "Варвара Верхола", Group: "M88-1/8", Discipline: "Python Core", Grade: "59"
[105] Student: "Тимофій Гайворонський", Group: "M88-1/8", Discipline: "Python Core", Grade: "58"
[106] Student: "Панас Овсієнко", Group: "M88-1/8", Discipline: "Python Core", Grade: "58"
[107] Student: "Ярема Гречаник", Group: "M88-1/8", Discipline: "Python Core", Grade: "58"
[108] Student: "Емілія Бебешко", Group: "M88-1/8", Discipline: "Python Core", Grade: "57"
[109] Student: "Соломія Копитко", Group: "M88-1/8", Discipline: "Python Core", Grade: "56"
[110] Student: "Пармен Гаєвський", Group: "M88-1/8", Discipline: "Python Core", Grade: "56"
[111] Student: "Світлана Василенко", Group: "M88-1/8", Discipline: "Python Core", Grade: "56"
[112] Student: "Василина Даниленко", Group: "M88-1/8", Discipline: "Python Core", Grade: "55"
[113] Student: "Марта Баранник", Group: "M88-1/8", Discipline: "Python Core", Grade: "55"
[114] Student: "Пармен Гаєвський", Group: "M88-1/8", Discipline: "Python Core", Grade: "55"
[115] Student: "Захар Затула", Group: "M88-1/8", Discipline: "Python Core", Grade: "54"
[116] Student: "Юстина Шамрай", Group: "M88-1/8", Discipline: "Python Core", Grade: "53"
[117] Student: "Вікторія Гаврилишин", Group: "M88-1/8", Discipline: "Python Core", Grade: "53"
[118] Student: "Вікторія Гаврилишин", Group: "M88-1/8", Discipline: "Python Core", Grade: "52"
[119] Student: "Тимофій Гайворонський", Group: "M88-1/8", Discipline: "Python Core", Grade: "52"
[120] Student: "Максим Дзиндра", Group: "M88-1/8", Discipline: "Python Core", Grade: "51"
[121] Student: "Юхим Сірко", Group: "M88-1/8", Discipline: "Python Core", Grade: "49"
[122] Student: "Нестор Ярема", Group: "M88-1/8", Discipline: "Python Core", Grade: "49"
[123] Student: "Хома Яценюк", Group: "M88-1/8", Discipline: "Python Core", Grade: "49"
[124] Student: "Любов Ільєнко", Group: "M88-1/8", Discipline: "Python Core", Grade: "48"
[125] Student: "Михайло Забара", Group: "M88-1/8", Discipline: "Python Core", Grade: "48"
[126] Student: "Пармен Гаєвський", Group: "M88-1/8", Discipline: "Python Core", Grade: "48"
[127] Student: "Захар Затула", Group: "M88-1/8", Discipline: "Python Core", Grade: "47"
[128] Student: "Варвара Верхола", Group: "M88-1/8", Discipline: "Python Core", Grade: "47"
[129] Student: "Ігор Єременко", Group: "M88-1/8", Discipline: "Python Core", Grade: "47"
[130] Student: "Панас Овсієнко", Group: "M88-1/8", Discipline: "Python Core", Grade: "46"
[131] Student: "Ігнат Гаврилишин", Group: "M88-1/8", Discipline: "Python Core", Grade: "46"
[132] Student: "Богдан Кириленко", Group: "M88-1/8", Discipline: "Python Core", Grade: "46"
[133] Student: "Едуард Батіг", Group: "M88-1/8", Discipline: "Python Core", Grade: "45"
[134] Student: "Ганна Опанасенко", Group: "M88-1/8", Discipline: "Python Core", Grade: "45"
[135] Student: "Варфоломій Макаренко", Group: "M88-1/8", Discipline: "Python Core", Grade: "45"
[136] Student: "Варфоломій Макаренко", Group: "M88-1/8", Discipline: "Python Core", Grade: "45"
[137] Student: "Азар Артюх", Group: "M88-1/8", Discipline: "Python Core", Grade: "45"
[138] Student: "Остап Теличенко", Group: "M88-1/8", Discipline: "Python Core", Grade: "44"
[139] Student: "Артем Ляшко", Group: "M88-1/8", Discipline: "Python Core", Grade: "43"
[140] Student: "Юхим Сірко", Group: "M88-1/8", Discipline: "Python Core", Grade: "43"
[141] Student: "Юхим Сірко", Group: "M88-1/8", Discipline: "Python Core", Grade: "43"
[142] Student: "Галина Копитко", Group: "M88-1/8", Discipline: "Python Core", Grade: "43"
[143] Student: "Юхим Сірко", Group: "M88-1/8", Discipline: "Python Core", Grade: "42"
[144] Student: "Трохим Бабко", Group: "M88-1/8", Discipline: "Python Core", Grade: "42"
[145] Student: "Ростислав Рубець", Group: "M88-1/8", Discipline: "Python Core", Grade: "42"
[146] Student: "Панас Овсієнко", Group: "M88-1/8", Discipline: "Python Core", Grade: "41"
[147] Student: "Юхим Сірко", Group: "M88-1/8", Discipline: "Python Core", Grade: "41"
[148] Student: "Ярема Гречаник", Group: "M88-1/8", Discipline: "Python Core", Grade: "40"
[149] Student: "Омелян Чекалюк", Group: "M88-1/8", Discipline: "Python Core", Grade: "40"
[150] Student: "Любов Ільєнко", Group: "M88-1/8", Discipline: "Python Core", Grade: "39"
[151] Student: "Соломія Копитко", Group: "M88-1/8", Discipline: "Python Core", Grade: "39"
[152] Student: "Алевтин Конопленко", Group: "M88-1/8", Discipline: "Python Core", Grade: "38"
[153] Student: "Лукʼян Юрченко", Group: "M88-1/8", Discipline: "Python Core", Grade: "36"
[154] Student: "Юстина Шамрай", Group: "M88-1/8", Discipline: "Python Core", Grade: "35"
[155] Student: "Юстина Ляшко", Group: "M88-1/8", Discipline: "Python Core", Grade: "35"
[156] Student: "Михайло Забара", Group: "M88-1/8", Discipline: "Python Core", Grade: "35"
[157] Student: "Лукʼян Юрченко", Group: "M88-1/8", Discipline: "Python Core", Grade: "34"
[158] Student: "Панас Овсієнко", Group: "M88-1/8", Discipline: "Python Core", Grade: "34"
[159] Student: "Ігор Єременко", Group: "M88-1/8", Discipline: "Python Core", Grade: "34"
[160] Student: "Лариса Колісниченко", Group: "M88-1/8", Discipline: "Python Core", Grade: "33"
[161] Student: "Нестор Ярема", Group: "M88-1/8", Discipline: "Python Core", Grade: "33"
[162] Student: "Франц Ткач", Group: "M88-1/8", Discipline: "Python Core", Grade: "33"
[163] Student: "Прохір Лагода", Group: "M88-1/8", Discipline: "Python Core", Grade: "32"
[164] Student: "Станіслав Негода", Group: "M88-1/8", Discipline: "Python Core", Grade: "32"
[165] Student: "Максим Дзиндра", Group: "M88-1/8", Discipline: "Python Core", Grade: "31"
[166] Student: "Азар Артюх", Group: "M88-1/8", Discipline: "Python Core", Grade: "31"
[167] Student: "Нестор Ярема", Group: "M88-1/8", Discipline: "Python Core", Grade: "31"
[168] Student: "Нестор Ярема", Group: "M88-1/8", Discipline: "Python Core", Grade: "31"
[169] Student: "Юстина Шамрай", Group: "M88-1/8", Discipline: "Python Core", Grade: "30"
[170] Student: "Леон Перебийніс", Group: "M88-1/8", Discipline: "Python Core", Grade: "30"
[171] Student: "Юхим Сірко", Group: "M88-1/8", Discipline: "Python Core", Grade: "30"
[172] Student: "Маруся Баранець", Group: "M88-1/8", Discipline: "Python Core", Grade: "30"
[173] Student: "Лариса Колісниченко", Group: "M88-1/8", Discipline: "Python Core", Grade: "30"
--------------------------------------------------------------------------------
task_08
2023-10-03 00:12:41,049 INFO sqlalchemy.engine.Engine SELECT concat(teachers.first_name, %(concat_1)s, teachers.last_name) AS "Teacher", disciplines.name AS "Discipline", ROUND(AVG(grades.grade), %(ROUND_1)s) AS "Average grade"
FROM grades JOIN disciplines ON disciplines.id = grades.discipline_id JOIN teachers ON teachers.id = disciplines.teacher_id
WHERE teachers.id = %(id_1)s GROUP BY disciplines.id, teachers.first_name, teachers.last_name ORDER BY "Average grade" DESC
2023-10-03 00:12:41,049 INFO sqlalchemy.engine.Engine [generated in 0.00113s] {'concat_1': ' ', 'ROUND_1': 2, 'id_1': 8}
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   
[ 1] Teacher: "Людмила Зінченко", Discipline: "Ділова українська мова", Average grade: "67.66"
[ 2] Teacher: "Людмила Зінченко", Discipline: "Історія України", Average grade: "64.87"
[ 3] Teacher: "Людмила Зінченко", Discipline: "Філософія", Average grade: "63.98"
--------------------------------------------------------------------------------
task_09
2023-10-03 00:12:41,067 INFO sqlalchemy.engine.Engine SELECT concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", disciplines.name AS "Discipline"
FROM grades JOIN disciplines ON disciplines.id = grades.discipline_id JOIN students ON students.id = grades.student_id
WHERE students.id = %(id_1)s GROUP BY disciplines.id, students.first_name, students.last_name ORDER BY disciplines.name
2023-10-03 00:12:41,067 INFO sqlalchemy.engine.Engine [generated in 0.00086s] {'concat_1': ' ', 'id_1': 1}
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
[ 1] Student: "Охрім Теліженко", Discipline: "English"
[ 2] Student: "Охрім Теліженко", Discipline: "Git"
[ 3] Student: "Охрім Теліженко", Discipline: "Python Core"
[ 4] Student: "Охрім Теліженко", Discipline: "Python Data Science"
[ 5] Student: "Охрім Теліженко", Discipline: "Python Web"
[ 6] Student: "Охрім Теліженко", Discipline: "Ділова українська мова"
[ 7] Student: "Охрім Теліженко", Discipline: "Історія України"
[ 8] Student: "Охрім Теліженко", Discipline: "Філософія"
--------------------------------------------------------------------------------
task_10
2023-10-03 00:12:41,084 INFO sqlalchemy.engine.Engine SELECT disciplines.name AS "Discipline", concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", concat(teachers.first_name, %(concat_2)s, teachers.last_name) AS "Teacher"
FROM grades JOIN disciplines ON disciplines.id = grades.discipline_id JOIN students ON students.id = grades.student_id JOIN teachers ON teachers.id = disciplines.teacher_id
WHERE students.id = %(id_1)s AND teachers.id = %(id_2)s GROUP BY disciplines.id, "Student", "Teacher" ORDER BY disciplines.name       
2023-10-03 00:12:41,087 INFO sqlalchemy.engine.Engine [generated in 0.00301s] {'concat_1': ' ', 'concat_2': ' ', 'id_1': 5, 'id_2': 8}
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   
[ 1] Discipline: "Ділова українська мова", Student: "Федір Павленко", Teacher: "Людмила Зінченко"
[ 2] Discipline: "Історія України", Student: "Федір Павленко", Teacher: "Людмила Зінченко"
[ 3] Discipline: "Філософія", Student: "Федір Павленко", Teacher: "Людмила Зінченко"
--------------------------------------------------------------------------------
task_11
2023-10-03 00:12:41,098 INFO sqlalchemy.engine.Engine SELECT disciplines.name AS "Discipline", concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", concat(teachers.first_name, %(concat_2)s, teachers.last_name) AS "Teacher", ROUND(AVG(grades.grade), %(ROUND_1)s) AS "Average grade"
FROM grades JOIN disciplines ON disciplines.id = grades.discipline_id JOIN students ON students.id = grades.student_id JOIN teachers ON teachers.id = disciplines.teacher_id
WHERE students.id = %(id_1)s AND teachers.id = %(id_2)s GROUP BY disciplines.id, "Student", "Teacher" ORDER BY "Average grade" DESC   
2023-10-03 00:12:41,099 INFO sqlalchemy.engine.Engine [generated in 0.00125s] {'concat_1': ' ', 'concat_2': ' ', 'ROUND_1': 2, 'id_1': 5, 'id_2': 8}
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
[ 1] Discipline: "Історія України", Student: "Федір Павленко", Teacher: "Людмила Зінченко", Average grade: "61.00"
[ 2] Discipline: "Ділова українська мова", Student: "Федір Павленко", Teacher: "Людмила Зінченко", Average grade: "56.00"
[ 3] Discipline: "Філософія", Student: "Федір Павленко", Teacher: "Людмила Зінченко", Average grade: "43.00"
--------------------------------------------------------------------------------
task_12
c:\Users\lexxa\Developments\GoIT\Python\Python 15\Web\goit_python_web_hw_07\src\tasks.py:23: SAWarning: SELECT statement has a cartesian product between FROM element(s) "groups" and FROM element "students".  Apply join condition(s) between each element to resolve.
  return {"column_names": query.statement.columns.keys(), "result": query.all()}
2023-10-03 00:32:46,284 INFO sqlalchemy.engine.Engine SELECT groups.name AS "Group", disciplines.name AS "Discipline", concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", concat(teachers.first_name, %(concat_2)s, teachers.last_name) AS "Teacher", grades.date_of AS "DATE OF", grades.grade AS "Grade"     
FROM grades JOIN disciplines ON disciplines.id = grades.discipline_id JOIN students ON students.id = grades.student_id JOIN teachers ON teachers.id = disciplines.teacher_id, groups
WHERE groups.id = %(id_1)s AND grades.discipline_id = %(discipline_id_1)s AND grades.date_of = (SELECT max(grades.date_of) AS max_1
FROM grades JOIN students ON students.id = grades.student_id
WHERE students.group_id = %(group_id_1)s AND grades.discipline_id = %(discipline_id_2)s) ORDER BY "Grade" DESC
2023-10-03 00:32:46,284 INFO sqlalchemy.engine.Engine [generated in 0.00110s] {'concat_1': ' ', 'concat_2': ' ', 'id_1': 1, 'discipline_id_1': 1, 'group_id_1': 1, 'discipline_id_2': 1}
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
[ 1] Group: "M88-1/8", Discipline: "Python Core", Student: "Панас Овсієнко", Teacher: "Давид Цимбалюк", DATE OF: "2024-01-02", Grade: "99"
[ 2] Group: "M88-1/8", Discipline: "Python Core", Student: "Панас Овсієнко", Teacher: "Давид Цимбалюк", DATE OF: "2024-01-02", Grade: "81"
[ 3] Group: "M88-1/8", Discipline: "Python Core", Student: "Аліна Устенко", Teacher: "Давид Цимбалюк", DATE OF: "2024-01-02", Grade: "68"
[ 4] Group: "M88-1/8", Discipline: "Python Core", Student: "Панас Овсієнко", Teacher: "Давид Цимбалюк", DATE OF: "2024-01-02", Grade: "41"

```


### CONSOLE CLI

```
usage: main.py [-h] [-a ACTION] [-m {Teacher,Student,Discipline,Grade}] [-n,  NAME] [-e EMAIL] [-p PHONE] [-addr ADDRESS]
               [--id ID] [--sid SID] [--tid TID] [--did DID] [--grade GRADE] [--date DATE] [--limit LIMIT]

options:
  -h, --help            show this help message and exit
  -a ACTION, --action ACTION
                        Action
  -m {Teacher,Student,Discipline,Grade}, --model {Teacher,Student,Discipline,Grade}
                        What model modify
  -n,  NAME, --name NAME
                        Name or Full name
  -e EMAIL, --email EMAIL
                        Email
  -p PHONE, --phone PHONE
                        Phone
  -addr ADDRESS, --address ADDRESS
                        Address
  --id ID               ID of record
  --sid SID             Student ID record
  --tid TID             Teacher ID record
  --did DID             Discipline ID record
  --grade GRADE         grade
  --date DATE           date of grade
  --limit LIMIT         limit of results
```

### create
--action create -m Teacher --name "Jon Valis" --email dsds@wwe.com --address "addres one"
```
2023-10-03 03:55:56,592 INFO sqlalchemy.engine.Engine INSERT INTO teachers (first_name, last_name, email, phone, address) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(phone)s, %(address)s) RETURNING teachers.id
2023-10-03 03:55:56,592 INFO sqlalchemy.engine.Engine [generated in 0.00075s] {'first_name': 'Jon', 'last_name': 'Valis', 'email': 'dsds@wwe.com', 'phone': None, 'address': 'addres one'}
2023-10-03 03:55:56,592 INFO sqlalchemy.engine.Engine COMMIT
2023-10-03 03:55:56,607 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-10-03 03:55:56,607 INFO sqlalchemy.engine.Engine SELECT teachers.id AS teachers_id, teachers.first_name AS teachers_first_name, teachers.last_name AS teachers_last_name, teachers.email AS teachers_email, teachers.phone AS teachers_phone, teachers.address AS teachers_address
FROM teachers
WHERE teachers.id = %(pk_1)s
2023-10-03 03:55:56,607 INFO sqlalchemy.engine.Engine [generated in 0.00112s] {'pk_1': 24}
Done. Created record with ID: 24
```


### list
```
 -a list -m Discipline --limit 5
2023-10-03 04:11:14,179 INFO sqlalchemy.engine.Engine SELECT disciplines.id AS disciplines_id, disciplines.name AS disciplines_name, disciplines.teacher_id AS disciplines_teacher_id
FROM disciplines
 LIMIT %(param_1)s
2023-10-03 04:11:14,179 INFO sqlalchemy.engine.Engine [generated in 0.00085s] {'param_1': 5}
[ 1] id: "1", name: "Python Core", teacher_id: "10"
[ 2] id: "2", name: "Python Web", teacher_id: "9"
[ 3] id: "3", name: "Python Data Science", teacher_id: "1"
[ 4] id: "4", name: "Вища математика", teacher_id: "10"
[ 5] id: "5", name: "HTML CSS", teacher_id: "10"
```

-a list -m Teacher --limit 5  
```
2023-10-03 04:10:25,040 INFO sqlalchemy.engine.Engine SELECT teachers.id AS teachers_id, teachers.first_name AS teachers_first_name, teachers.last_name AS teachers_last_name, teachers.email AS teachers_email, teachers.phone AS teachers_phone, teachers.address AS teachers_address
FROM teachers
 LIMIT %(param_1)s
2023-10-03 04:10:25,040 INFO sqlalchemy.engine.Engine [generated in 0.00089s] {'param_1': 5}
[ 1] id: "1", first_name: "Орест", last_name: "Товстуха", email: "myron44@email.ua", phone: "+380 69 737-27-27", address: "вулиця Докова, буд. 942 кв. 97, Нововолинськ, 53126"
[ 2] id: "2", first_name: "Максим", last_name: "Яценюк", email: "nestorbandurka@meta.ua", phone: "093 447 68 62", address: "провулок Лиманчик 2-й Лінія 4-та, буд. 52, Тернопіль, 52059"
[ 3] id: "3", first_name: "Болеслав", last_name: "Лаба", email: "mykolaiatroshchenko@gov.ua", phone: "517 47 83", address: "сквер 8-ма Лінія Дачі Ковалевського, буд. 526, Миргород, 74434"
[ 4] id: "4", first_name: "Франц", last_name: "Доценко", email: "abramenkoirena@i.ua", phone: "+380 23 281 41 71", address: "шосе Виноградна, буд. 2 кв. 465, Брянка, 64891"
[ 5] id: "5", first_name: "Едита", last_name: "Артимович", email: "aleksandrenkoviacheslav@gov.ua", phone: "+380 24 229-50-50", address: "шосе Естонський, буд. 6, Вільногірськ, 48925"
```

-a list -m Grade --limit 5      
```
2023-10-03 04:12:26,963 INFO sqlalchemy.engine.Engine SELECT grades.id AS grades_id, grades.grade AS grades_grade, grades.date_of AS grades_date_of, grades.student_id AS grades_student_id, grades.discipline_id AS grades_discipline_id
FROM grades
 LIMIT %(param_1)s
2023-10-03 04:12:26,963 INFO sqlalchemy.engine.Engine [generated in 0.00081s] {'param_1': 5}
[ 1] id: "1", grade: "88", date_of: "2023-11-27", student_id: "27", discipline_id: "2"
[ 2] id: "2", grade: "76", date_of: "2023-11-27", student_id: "11", discipline_id: "2"
[ 3] id: "3", grade: "93", date_of: "2023-11-27", student_id: "98", discipline_id: "2"
[ 4] id: "4", grade: "60", date_of: "2023-11-27", student_id: "27", discipline_id: "2"
[ 5] id: "5", grade: "68", date_of: "2023-11-27", student_id: "11", discipline_id: "2"
```


### DOCKER COMPOSER
```
scripts>docker_run_docker-compose.cmd
[+] Running 2/0
 ✔ Container goit_python_web_hw_07-db-1    Created                                                                          0.0s 
 ✔ Container goit_python_web_hw_07-code-1  Created                                                                          0.0s 
Attaching to goit_python_web_hw_07-code-1
goit_python_web_hw_07-code-1  | Sleep 1...
goit_python_web_hw_07-code-1  | INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
goit_python_web_hw_07-code-1  | INFO  [alembic.runtime.migration] Will assume transactional DDL.
goit_python_web_hw_07-code-1  | --------------------------------------------------------------------------------
goit_python_web_hw_07-code-1  | task_01
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:43,984 INFO sqlalchemy.engine.Engine select pg_catalog.version()
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:43,984 INFO sqlalchemy.engine.Engine [raw sql] {}
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:43,985 INFO sqlalchemy.engine.Engine select current_schema()
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:43,986 INFO sqlalchemy.engine.Engine [raw sql] {}
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:43,987 INFO sqlalchemy.engine.Engine show standard_conforming_strings
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:43,988 INFO sqlalchemy.engine.Engine [raw sql] {}
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:43,989 INFO sqlalchemy.engine.Engine BEGIN (implicit)
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,015 INFO sqlalchemy.engine.Engine SELECT concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", ROUND(AVG(grades.grade), %(ROUND_1)s) AS "Average grade"
goit_python_web_hw_07-code-1  | FROM grades JOIN students ON students.id = grades.student_id GROUP BY students.id ORDER BY "Average grade" DESC
goit_python_web_hw_07-code-1  |  LIMIT %(param_1)s
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,016 INFO sqlalchemy.engine.Engine [generated in 0.00028s] {'concat_1': ' ', 'ROUND_1': 2, 'param_1': 5}
goit_python_web_hw_07-code-1  | .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   
goit_python_web_hw_07-code-1  | --------------------------------------------------------------------------------
goit_python_web_hw_07-code-1  | task_02
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,022 INFO sqlalchemy.engine.Engine SELECT disciplines.name AS "Discipline", concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", ROUND(AVG(grades.grade), %(ROUND_1)s) AS "Average grade"
goit_python_web_hw_07-code-1  | FROM grades JOIN students ON students.id = grades.student_id JOIN disciplines ON disciplines.id = grades.discipline_id
goit_python_web_hw_07-code-1  | WHERE disciplines.id = %(id_1)s GROUP BY students.id, disciplines.name ORDER BY "Average grade" DESC
goit_python_web_hw_07-code-1  |  LIMIT %(param_1)s
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,023 INFO sqlalchemy.engine.Engine [generated in 0.00024s] {'concat_1': ' ', 'ROUND_1': 2, 'id_1': 2, 'param_1': 1}
goit_python_web_hw_07-code-1  | .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
goit_python_web_hw_07-code-1  | --------------------------------------------------------------------------------
goit_python_web_hw_07-code-1  | task_03
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,032 INFO sqlalchemy.engine.Engine SELECT disciplines.name AS "Discipline", groups.name AS "Group", ROUND(AVG(grades.grade), %(ROUND_1)s) AS "Average grade"
goit_python_web_hw_07-code-1  | FROM grades JOIN students ON students.id = grades.student_id JOIN disciplines ON disciplines.id = grades.discipline_id JOIN groups ON groups.id = students.group_id
goit_python_web_hw_07-code-1  | WHERE disciplines.id = %(id_1)s GROUP BY students.id, disciplines.name, groups.name ORDER BY "Average grade" DESC
goit_python_web_hw_07-code-1  |  LIMIT %(param_1)s
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,032 INFO sqlalchemy.engine.Engine [generated in 0.00055s] {'ROUND_1': 2, 'id_1': 2, 'param_1': 1}
goit_python_web_hw_07-code-1  | .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
goit_python_web_hw_07-code-1  | --------------------------------------------------------------------------------
goit_python_web_hw_07-code-1  | task_04
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,038 INFO sqlalchemy.engine.Engine SELECT ROUND(AVG(grades.grade), %(ROUND_1)s) AS "Average grade"
goit_python_web_hw_07-code-1  | FROM grades ORDER BY "Average grade" DESC
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,038 INFO sqlalchemy.engine.Engine [generated in 0.00039s] {'ROUND_1': 2}     
goit_python_web_hw_07-code-1  | .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   
goit_python_web_hw_07-code-1  | [ 1] Average grade: "None"
goit_python_web_hw_07-code-1  | --------------------------------------------------------------------------------
goit_python_web_hw_07-code-1  | task_05
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,055 INFO sqlalchemy.engine.Engine SELECT disciplines.name AS "Discipline", concat(teachers.first_name, %(concat_1)s, teachers.last_name) AS "Teacher"
goit_python_web_hw_07-code-1  | FROM disciplines JOIN teachers ON teachers.id = disciplines.teacher_id
goit_python_web_hw_07-code-1  | WHERE teachers.id = %(id_1)s ORDER BY disciplines.name
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,056 INFO sqlalchemy.engine.Engine [generated in 0.00071s] {'concat_1': ' ', 'id_1': 10}
goit_python_web_hw_07-code-1  | .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
goit_python_web_hw_07-code-1  | --------------------------------------------------------------------------------
goit_python_web_hw_07-code-1  | task_06
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,060 INFO sqlalchemy.engine.Engine SELECT groups.name AS "Group", concat(students.first_name, %(concat_1)s, students.last_name) AS "Student"
goit_python_web_hw_07-code-1  | FROM students JOIN groups ON groups.id = students.group_id
goit_python_web_hw_07-code-1  | WHERE groups.id = %(id_1)s ORDER BY students.last_name
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,060 INFO sqlalchemy.engine.Engine [generated in 0.00031s] {'concat_1': ' ', 'id_1': 1}
goit_python_web_hw_07-code-1  | .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   
goit_python_web_hw_07-code-1  | --------------------------------------------------------------------------------
goit_python_web_hw_07-code-1  | task_07
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,071 INFO sqlalchemy.engine.Engine SELECT concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", groups.name AS "Group", disciplines.name AS "Discipline", grades.grade AS "Grade"        
goit_python_web_hw_07-code-1  | FROM grades JOIN students ON students.id = grades.student_id JOIN disciplines ON disciplines.id = grades.discipline_id, groups
goit_python_web_hw_07-code-1  | WHERE groups.id = %(id_1)s AND disciplines.id = %(id_2)s ORDER BY grades.grade DESC
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,072 INFO sqlalchemy.engine.Engine [generated in 0.00035s] {'concat_1': ' ', 'id_1': 1, 'id_2': 1}
goit_python_web_hw_07-code-1  | /app/src/tasks.py:23: SAWarning: SELECT statement has a cartesian product between FROM element(s) "groups" and FROM element "disciplines".  Apply join condition(s) between each element to resolve.
goit_python_web_hw_07-code-1  |   return {"column_names": query.statement.columns.keys(), "result": query.all()}
goit_python_web_hw_07-code-1  | .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
goit_python_web_hw_07-code-1  | --------------------------------------------------------------------------------
goit_python_web_hw_07-code-1  | task_08
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,080 INFO sqlalchemy.engine.Engine SELECT concat(teachers.first_name, %(concat_1)s, teachers.last_name) AS "Teacher", disciplines.name AS "Discipline", ROUND(AVG(grades.grade), %(ROUND_1)s) AS "Average grade"
goit_python_web_hw_07-code-1  | FROM grades JOIN disciplines ON disciplines.id = grades.discipline_id JOIN teachers ON teachers.id = disciplines.teacher_id
goit_python_web_hw_07-code-1  | WHERE teachers.id = %(id_1)s GROUP BY disciplines.id, teachers.first_name, teachers.last_name ORDER BY "Average grade" DESC
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,080 INFO sqlalchemy.engine.Engine [generated in 0.00042s] {'concat_1': ' ', 'ROUND_1': 2, 'id_1': 8}
goit_python_web_hw_07-code-1  | .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   
goit_python_web_hw_07-code-1  | --------------------------------------------------------------------------------
goit_python_web_hw_07-code-1  | task_09
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,092 INFO sqlalchemy.engine.Engine SELECT concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", disciplines.name AS "Discipline"
goit_python_web_hw_07-code-1  | FROM grades JOIN disciplines ON disciplines.id = grades.discipline_id JOIN students ON students.id = grades.student_id
goit_python_web_hw_07-code-1  | WHERE students.id = %(id_1)s GROUP BY disciplines.id, students.first_name, students.last_name ORDER BY disciplines.name
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,092 INFO sqlalchemy.engine.Engine [generated in 0.00031s] {'concat_1': ' ', 'id_1': 1}
goit_python_web_hw_07-code-1  | .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
goit_python_web_hw_07-code-1  | --------------------------------------------------------------------------------
goit_python_web_hw_07-code-1  | task_10
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,098 INFO sqlalchemy.engine.Engine SELECT disciplines.name AS "Discipline", concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", concat(teachers.first_name, %(concat_2)s, teachers.last_name) AS "Teacher"
goit_python_web_hw_07-code-1  | FROM grades JOIN disciplines ON disciplines.id = grades.discipline_id JOIN students ON students.id = grades.student_id JOIN teachers ON teachers.id = disciplines.teacher_id
goit_python_web_hw_07-code-1  | WHERE students.id = %(id_1)s AND teachers.id = %(id_2)s GROUP BY disciplines.id, "Student", "Teacher" ORDER BY disciplines.name
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,098 INFO sqlalchemy.engine.Engine [generated in 0.00028s] {'concat_1': ' ', 'concat_2': ' ', 'id_1': 5, 'id_2': 8}
goit_python_web_hw_07-code-1  | .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
goit_python_web_hw_07-code-1  | --------------------------------------------------------------------------------
goit_python_web_hw_07-code-1  | task_11
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,112 INFO sqlalchemy.engine.Engine SELECT disciplines.name AS "Discipline", concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", concat(teachers.first_name, %(concat_2)s, teachers.last_name) AS "Teacher", ROUND(AVG(grades.grade), %(ROUND_1)s) AS "Average grade"
goit_python_web_hw_07-code-1  | FROM grades JOIN disciplines ON disciplines.id = grades.discipline_id JOIN students ON students.id = grades.student_id JOIN teachers ON teachers.id = disciplines.teacher_id
goit_python_web_hw_07-code-1  | WHERE students.id = %(id_1)s AND teachers.id = %(id_2)s GROUP BY disciplines.id, "Student", "Teacher" ORDER BY "Average grade" DESC
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,112 INFO sqlalchemy.engine.Engine [generated in 0.00028s] {'concat_1': ' ', 'concat_2': ' ', 'ROUND_1': 2, 'id_1': 5, 'id_2': 8}
goit_python_web_hw_07-code-1  | .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
goit_python_web_hw_07-code-1  | --------------------------------------------------------------------------------
goit_python_web_hw_07-code-1  | task_12
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,123 INFO sqlalchemy.engine.Engine SELECT groups.name AS "Group", disciplines.name AS "Discipline", concat(students.first_name, %(concat_1)s, students.last_name) AS "Student", concat(teachers.first_name, %(concat_2)s, teachers.last_name) AS "Teacher", grades.date_of AS "DATE OF", grades.grade AS "Grade"
goit_python_web_hw_07-code-1  | FROM grades JOIN disciplines ON disciplines.id = grades.discipline_id JOIN students ON students.id = grades.student_id JOIN teachers ON teachers.id = disciplines.teacher_id, groups
goit_python_web_hw_07-code-1  | WHERE groups.id = %(id_1)s AND grades.discipline_id = %(discipline_id_1)s AND grades.date_of = (SELECT max(grades.date_of) AS max_1
goit_python_web_hw_07-code-1  | FROM grades JOIN students ON students.id = grades.student_id
goit_python_web_hw_07-code-1  | WHERE students.group_id = %(group_id_1)s AND grades.discipline_id = %(discipline_id_2)s) ORDER BY "Grade" DESC
goit_python_web_hw_07-code-1  | 2023-10-03 03:36:44,123 INFO sqlalchemy.engine.Engine [generated in 0.00061s] {'concat_1': ' ', 'concat_2': ' ', 'id_1': 1, 'discipline_id_1': 1, 'group_id_1': 1, 'discipline_id_2': 1}
goit_python_web_hw_07-code-1  | .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
goit_python_web_hw_07-code-1 exited with code 0

```