
from flask import Flask, render_template, request,redirect
from datetime import date 
import os as m
app = Flask(__name__)

STUDENTS_file="students.txt"
ATTENDANCE_file="attendance.txt"
def get_students():
    def   save student (name):
         with open   (STUDENTS_file,"a") as f:
            f.write(name + "\n")
        with open
    if not   (m.path.exists(STUDENTS_file):
        return []
        def save_attendance(data):
            today=(str(date.today()
            with open(ATTENDANCE_file, "a") as f:
for student,status in data.items() :
f.write  (today + ","+  student + ","+ status+ "/n" )

#TODO: ADD A ATTENDANCE SYSTEM IF NEEDS TO CHANGE THE ALREADY MARK TODAY
# A system
 def (get_attendance):
    if not os.path.exists(ATTENDANCE_file):
        return[]
        with open (ATTENDANCE_file,"r") as f:
            line=f,readlines()
            records=[]
            for l in lines:
                l=l.strip()
                if l!="":
                    parts=l.split(",")
records.append(parts)
return records

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
                    data(a)=val
                    else:
                        data[a]="ABSENT "
                        save_attendance(data)
                        return redirect("/view_attendance")
                        @app.route("/view_attendance")
                        def view_attendance():
                            records=get_attendance()
                            return render_template("view_attendance.html", records=records)
                            



    #TODO: add more route later

if __name__ == "__main__":
    app.run(debug=True)      
