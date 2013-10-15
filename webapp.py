from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

# @app.route("/")
# def get_github():
#     return render_template("get_github.html")

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    grades_str = hackbright_app.get_all_grades(row[2])


    html = render_template("student_info.html", first_name=row[0],
                                                last_name=row[1],
                                                github=row[2], 
                                                grades = grades_str)
    return html

@app.route("/newstudent")
def make_student():
    hackbright_app.connect_to_db()
    student_first_name = request.args.get("first_name")
    student_last_name = request.args.get("last_name")
    student_github = request.args.get("github")
    
    hackbright_app.make_new_student(student_first_name, student_last_name, student_github)
    row = hackbright_app.get_student_by_github(student_github)

    html = render_template("student_info.html", first_name=row[0],
                                                last_name=row[1],
                                                github=row[2])
    return html

@app.route("/project")
def get_project(): 
    hackbright_app.connect_to_db()
    project_title = request.args.get("project_title")
    row = hackbright_app.get_project_title(project_title)

    html = render_template("project_info.html", project=row)

    return html

@app.route("/newproject")
def make_project():
    hackbright_app.connect_to_db()
    title = request.args.get("title")
    description = request.args.get("description")
    max_grade = request.args.get("max_grade")
    hackbright_app.make_new_project(title, max_grade, description)

    row = hackbright_app.get_project_info(title)
    html = render_template("project_info.html", project=row)

    return html



@app.route("/")
def new_project():
    return render_template("new_project.html")

# @app.route("/")
# def new_student():
#     return render_template("new_student.html")

if __name__ == "__main__":
    app.run(debug=True)