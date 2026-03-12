import sqlite3
from sqlite3 import Error
import difflib
from flask import Flask, render_template, request, flash, redirect

def compare_simmilarity(string1, string2):
    """ return simmiliarity score for string1 to string2
    :param string1:
    :param string2:
    :return: float simmiliarity score in range from 0 to 1
    """
    return difflib.SequenceMatcher(None,string1.lower(), string2.lower()).ratio()


def search_simmilar_themes(conn, search_string, search_table_name="themes"):
    table_content = get_table(conn, search_table_name)[1]
    print("штуки")
    print(*table_content)
    field_content = [row[3] for row in table_content]

    return difflib.get_close_matches(search_string, field_content)

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row
        return conn
    except Error as e:
        print(e)

    return conn


def close_connection(conn):
    """ close connection do the SQLite database
    :param conn: Connection object
    :return: True or None
    """
    try:
        conn.close()
    except Error as e:
        print(e)
    else:
        return True


def get_themes(conn):
    """ get all themes from the "themes" table with student and
        discipline names joined in
    :param conn: Connection object
    :return: list of tuples (rows) with themes in format:
        ("discipline","student","theme")
    """
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT
                        discipline.name as discipline,
                        student.name as student,
                        theme.type as type,
                        theme.content as content
                    FROM
                        theme
                    INNER JOIN discipline
                        ON theme.discipline_id = discipline.id
                    INNER JOIN student
                        ON theme.student_id = student.id;
                   """)
    column_names = list(map(lambda x: x[0], cursor.description))
    header = [description[0] for description in cursor.description]
    return (header ,cursor.fetchall())


def get_disciplines(conn):
    """ get all disciplines from the "disciplines" table
    :param conn: Connection object
    :return: list of discipline names
    """
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT
                        discipline.name as discipline
                    FROM
                        discipline
                   """)
    column_names = list(map(lambda x: x[0], cursor.description))
    header = [description[0] for description in cursor.description]
    return (header ,cursor.fetchall())


def get_students(conn):
    """
    """
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT
                        name,
                        group_code
                    FROM
                        student
                   """)
    column_names = list(map(lambda x: x[0], cursor.description))
    print(f"Имена аааа: {column_names}")
    header = [description[0] for description in cursor.description]
    return (header ,cursor.fetchall())


def get_groups(conn):
    """
    """
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT
                        "group".code,
                        qualification.name
                    FROM
                        "group"
                    INNER JOIN
                        qualification
                    ON "group".qualification_id = qualification.id
                   """)
    column_names = list(map(lambda x: x[0], cursor.description))
    header = [description[0] for description in cursor.description]
    return (header ,cursor.fetchall())


def get_qualifications(conn):
    """
    """
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT
                        name
                    FROM
                        qualification
                   """)
    column_names = list(map(lambda x: x[0], cursor.description))
    header = [description[0] for description in cursor.description]
    return (header ,cursor.fetchall())

def get_table(conn, table_name):
    """
    """
    if table_name == "themes":
        return get_themes(conn)
    elif table_name == "disciplines":
        return get_disciplines(conn)
    elif table_name == "students":
        return get_students(conn)
    elif table_name == "groups":
        return get_groups(conn)
    elif table_name == "qualifications":
        return get_qualifications(conn)
    else:
        return None


def add_qualification(conn, qualification):
    """add qualification into qualification table
    :param conn:
    :param qualification:
    :return: True or None
    """
    #TODO return ID instead of True
    #TODO try-except
    cursor = conn.cursor()
    cursor.execute("INSERT INTO qualification (name) VALUES (?)", (qualification,))

    connection.commit()
    return True


def add_group(conn, group_code, qualification_id):
    """
    """
    #TODO try-except
    cursor = conn.cursor()
    cursor.execute("INSERT INTO group (code, qualification_id) VALUES (?, ?)", (group_code, qualification_id))

    connection.commit()
    return True


def add_student(conn, name, group_code):
    #TODO return ID instead of True
    #TODO try-except
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student (name, group_code) VALUES (?, ?)", (name, group_code))

    connection.commit()
    return True

def add_discipline(conn, name):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO discipline (name) VALUES (?)", (name))

    connection.commit()
    return True

def add_theme(conn, discipline_id, student_id, type_, content):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO discipline (discipline_id, student_id, type, content) VALUES (?, ?, ?, ?, ?)", (conn, discipline_id, student_id, type_, content))

    connection.commit()
    return True

def add_table(conn, table_name):
    """
    """
    if table_name == "themes":
        return add_theme(conn)
    elif table_name == "disciplines":
        return add_discipline(conn)
    elif table_name == "students":
        return add_student(conn)
    elif table_name == "groups":
        return add_groups(conn)
    elif table_name == "qualifications":
        return add_qualifications(conn)
    else:
        return None



database = "db-themes.db"
app = Flask(__name__)
app.config['SECRET_KEY'] = '5708552aed9b6ad9e280c2651ac330f4795284b63655b485'

@app.route('/', methods=('GET', 'POST'))
def index():
    conn = create_connection(database)
    table_type = request.args.get('table')
    if not table_type:
        table_type = "themes"

    header, table_content = get_table(conn, table_type)
    if not header:
        flash(f"не существует таблицы %table_type")
    print(f"заголовки: {header}")
    print(f"содержимое: {table_content}")

    search_results = None
    if request.method == "POST":
        search = list(request.form.items())
        print(f"список из формы поиска:")
        print(*search)
        if "search_request" in search[0][0]:
            search_request = request.form['search_request']
            search_results = search_simmilar_themes(conn, search_request)
            print(f"поисковый запрос: {search_request}")
            print(f"результат: {search_results}")


    close_connection(conn)
    return render_template('index.html', header = header, table_content =  table_content, search_results = search_results)

@app.route('/add/', methods=('GET', 'POST'))
def add():
    conn = create_connection(database)
    table_type = request.args.get('table')
    if not table_type:
        table_type = "themes"
    if request.method == 'POST':
        input_table = request.form.items()

        print(*input_table)
        for line in input_table:
            print(line)
            print(f"key = {line[0]}, value = {line[1]}")

    header, _ = get_table(conn, table_type)
    return render_template('add.html', table_type = table_type, header = header, size = 10)

