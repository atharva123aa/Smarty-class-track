from flask import Flask, render_template, request,redirect
import os as m
app = Flask(__name__)

STUDENTS_file="students.txt"
def get_students():
    def   save student (name):
         with open   (STUDENTS_file,"a") as f:
            f.write(name + "\n")
        with open
    if not   (m.path.exists(STUDENTS_file):
        return []

        with open  (STUDENTS_file,"r") as f:
            names=[line.script() for line in f.readlines()]
            [return n for n in names if n !=""]


@app.route("/") 
def home():
    return render_template("index.html")
  @app.route("/") 
def students():
    all_students=get_students()
return render_template("students.html", students=all_students)


@app.route("/add student", methods=["POST"])
def add_student():
    name=request.form.get("name")
     if name and name.strip() !="":
        




if __name__ == "__main__":
    app.run(debug=True)      
