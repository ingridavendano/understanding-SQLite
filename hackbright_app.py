import sqlite3

DB = None
CONN = None

def make_new_student(first_name, last_name, github):
    query = """INSERT INTO Students VALUES (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))

    CONN.commit()
    print "Successfully added student: %s %s" % (first_name, last_name)

def make_new_project(title, max_grade, description):
    query = """INSERT INTO Projects VALUES (?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))

    CONN.commit()
    print "Successfully added project: %s" % (title)

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])
    
def get_project_title(title):
    query = """SELECT * FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
Title: %s
Description: %s
Max Grade: %s""" % (row[0], row[1], row[2])

def give_student_grade(github, title, grade):
    query = """INSERT INTO Projects VALUES (?, ?, ?)"""
    DB.execute(query, (github, title, grade))

    CONN.commit()
    print "Successfully added grade: %s" % (github)


def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project_title":
            get_project_title(*args)
        elif command == "new_project":
            description = " ".join(args[2:])
            make_new_project(args[0], args[1], description)
        elif command == "student_grade":
            give_student_grades(*args)

    CONN.close()

if __name__ == "__main__":
    main()
