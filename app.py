
from flask import Flask, render_template, request,redirect
from datetime import date 
import os as m
app = Flask(__name__)

STUDENTS_file="students.txt"
ATTENDANCE_file="attendance.txt"
SCORES_file="scores.txt"
def get_students():
    if not   (m.path.exists(STUDENTS_file)):
        return []
    with open  (STUDENTS_file,"r") as f:
            names=[line.strip() for line in f.readlines()]
    return [n for n in names if n !=""]

def   save_student (name):
     with open   (STUDENTS_file,"a") as f:
        f.write(name + "\n")

def save_attendance(data):
    today=str(date.today())
    with open(ATTENDANCE_file, "a") as f:
        for student,status in data.items() :
            f.write  (today + ","+ student + ","+ status+ "\n" )

#TODO: ADD A ATTENDANCE SYSTEM IF NEEDS TO CHANGE THE ALREADY MARK TODAY
# A system
def get_attendance():
    if not m.path.exists(ATTENDANCE_file):
        return[]
    with open (ATTENDANCE_file,"r") as f:
            lines=f.readlines()
            records=[]
            for l in lines:
                l=l.strip()
                if l!="":
                    parts=l.split(",")
                    records.append(parts)
    return records

#marking sys
def save_scores(subject, data):
    with open(SCORES_file, "a") as f:
        for students,marks in data.items():
            m2=int(marks)
            if m2>=90: grade="Aplus"
            elif m2>=70: grade="A"
            elif m2>=50: grade="B"
            elif m2>=34: grade="C"
            elif m2>=20: grade="D"
            else: grade="F"

            f.write(subject+","+students+","+marks+","+grade+"\n")

def get_scores():
    if not m.path.exists(SCORES_file):
        return[]
    with open(SCORES_file,"r") as f:
        lines=f.readlines()
        records=[]
        for l in lines:
            l=l.strip()
            if l!="":
                parts=l.split(",")
                records.append(parts)
        return records



@app.route("/") 
def home():
    return render_template("index.html")

@app.route("/students") 
def students():
    all_students=get_students()
    return render_template("students.html", students=all_students)


@app.route("/add_student", methods=["POST"])
def add_student():
    name=request.form.get("name")
    if name and name.strip() !="":
        save_student(name.strip())
    return redirect("/students")

@app.route("/attendance")
def attendancee():
    s= get_students()
    return render_template("attendance.html", students=s)

@app.route("/save_attendance", methods=["POST"])
def submit_attendance():
    s=get_students()
    data={}
    for a in s:
        #PRESENT ABSENT
        val= request.form.get(a)
        if val:
            data[a]=val
        else:
            data[a]="ABSENT"
    save_attendance(data)
    return redirect("/view_attendance")

@app.route("/view_attendance")
def view_attendance():
    records=get_attendance()
    return render_template("view_attendance.html", records=records)

@app.route("/scores")
def scores():
    studs=get_students()
    return render_template("scores.html", students=studs)

@app.route("/save_scores", methods=["POST"])
def submit_scores():
    studs=get_students()
    subject=request.form.get("subject")
    data={}
    for s in studs:
        val=request.form.get(s)
        if val:
            data[s] =val
    save_scores(subject,data)
    return redirect("/view_scores")

@app.route("/view_scores")
def view_scores():
    records=get_scores()
    return render_template("view_scores.html", records=records)

    #TODO: add more route later

if __name__ == "__main__":
    app.run(debug=True)
