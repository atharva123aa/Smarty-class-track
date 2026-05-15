
    from flask import Flask, render_template, request,redirect
from datetime import date 
import os as m
app = Flask(__name__)

STUDENTS_file="students.txt"
ATTENDANCE_file="attendance.txt"
SCORES_file="scores.txt"
Quiz_file="quiz.txt"
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
            try:
                m2=int(marks)
            except ValueError:
                m2=0
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

def save_question(q,opts,ans):
    with open(QUIZ_file,"r") as f:
        lines=f.readlines()
        qs=[]
        for l in lines:
            l=l.strip()
            if l!="":
                qs.append(l.split("|"))
                return qs



@app.route("/quiz")
def quiz():
    qs=get_questions()
    return render_template("quiz.html", questions=qs)
@app.routd("/add_question")

def add_question():
    return render_template("add_question.html")
@app.route("/save_question", methods=["POST"])
def submit_question():
    
    q=request.form.get("question")
    opts=[request.form.get("optA")
          request.form.get("optB")
          request.form.get("optC")
          request.form.get("optD")
    ]
    ans=request.form.get("answer")
    save_question(q,opts,ans)
    return redirect("/add_question")

@app.route("/submit_quiz", methods=["POST"])
def submit_quiz():
    qs=get_questions()
    score=0
    total=len(qs)
    results=[]
    for i,q in enumerate(qs):

        chosen=request.form.get("q"+str(i))
        correct=q[5]
        #check correct
        if chosen==correct:
            score+=1
            results.append((q[0],chosen,correct,"right"))
        else:
             results.append((q[0],chosen,correct,"wrongt"))
    return render_template("quiz_result.html",score=score,total=total, results=results)
    




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
def attendance():
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
    if not subject or subject.strip()=="":
        return redirect("/scores")
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

@app.route("/report/<name>")
def report(name):
    #attendance counting
    all_att=get_attendance()
    present=0
    absent=0

    for r in all_att:
        if r[1]==name:
            if r[2].strip().lower()=="present":
                present+=1
            else:
                absent+=1


    all_scores=get_scores()
    my_scores=[] 
    for r in all_scores:
        if r[1]==name:
            my_scores.append(r)

    return render_template("report.html", name=name, present=present,absent=absent, scores=my_scores)
        #listing page
        #TODO: CONNECT MY OTHER TODO PDF EXPORT HERE TO GET REPORT CARD COPY WITH SOME RPORTS

@app.route("/report_card")
def report_card():

    studs=get_students()
    return render_template("report_card.html",  students=studs)

                




    #TODO: add more route later

if __name__ == "__main__":
    app.run(debug=True)
