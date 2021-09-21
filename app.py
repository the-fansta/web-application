from flask import Flask,render_template,request,session,flash
#Flask is a micro framework

app=Flask(__name__)
app.config["SECRET_KEY"]="1234"

@app.route('/')
@app.route('/home')
def hello():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/validate_register',methods=['POST',"GET"])
def validate_register():
    username=request.form.get('username')
    email=request.form.get('password')
    password=request.form.get('password')
    confirm_password=request.form.get('confirm_password')
    message=''
    if password==confirm_password:
        print('Registration Successful')
        message='Registration Successful'
        session['username']=username
        session['email'] =email
        return render_template('login_page.html',message=message)
    else:
        print('Password mismatch')
        
        message='password mismatch'
        return render_template('register.html',message=message)

@app.route('/login_page')
def login_page():
   return render_template("login_page.html")

@app.route('/validate_user',methods=['POST',"GET"])
def validate_user():
    user_name=request.form.get("username")
    password=request.form.get("password")
    print(password)
    session['password']=password
    message=""
    
    session_un=session.get('username')
    print(session_un)
    session_pwd=session.get('password')
    print(session_pwd)
    session_email=session.get('email')
    print(session_email)
    if session_un==user_name or session_email==user_name :
        if (session_pwd)==password :
            message="You have succesfully logged in!!!😃"
            flash('You were successfully logged in',)
            session['username']=user_name
            session['authenticated'] =True
            return render_template('question-1.html',message=message,score=0)
        else:
            message='Incorrect Password'
            session['authenticated'] =False
            return render_template('login_page.html',message=message)
    else:
        message='incorrect Username'
        flash("You have failed to login!!!😔")
        return render_template('login_page.html',message=message)

@app.route('/riddle_1')
def riddle_1():
   return render_template("riddle_1.html",riddles=riddles)


@app.route('/r1')
def r1():
   pass

riddles=[{
    "Author":"Divvya",
    "Title":"Riddle_1",
    "Content":"What can fill a room but takes up no space?",
    "Date_Posted":"8th June 2021"
},
{
    "Author":"Divvya",
    "Title":"Riddle_2",
    "Content":"What can fill a room but takes up no space?",
    "Date_Posted":"8th June 2021"
}]



# -------Validating Quiz---Important Function---------------------
def validatequiz(correct_answer):
    option=request.form.get("select")
    message=""
    score=session.get("user_score",0)   
    if option==correct_answer:
        message="Excellent, You are Right!!"
        score=score+20
    else:
        message="Nice try,The right answer is "+ correct_answer
    flash(message)
    session["user_score"]=score
    return message


#--------------------Quiz-------------------------------------------


#--------------------Q1-------------------------------------------

    
@app.route('/q1',methods=['POST',"GET"])
def q1():
   if request.method=="GET":
        return render_template("question-1.html")
   message = validatequiz('3')
   score=session.get("user_score",0)
   return render_template("question-2.html",message=message,score=score)

#--------------------Q2-------------------------------------------

@app.route('/q2',methods=['POST',"GET"])
def q2():
    if request.method=="GET":
        return render_template("question-2.html")
    message = validatequiz('3')
    score=session.get("user_score",0)
    return render_template("question-3.html",message=message,score=score)

#--------------------Q3-------------------------------------------

@app.route('/q3',methods=['POST',"GET"])
def q3():
    if request.method=="GET":
        return render_template("question-3.html")
    message = validatequiz('3')
    score=session.get("user_score",0)
    return render_template("question-4.html",message=message,score=score)

#--------------------Q4-------------------------------------------

@app.route('/q4',methods=['POST',"GET"])
def q4():
    if request.method=="GET":
        return render_template("question-4.html")
    message = validatequiz('2')
    score=session.get("user_score",0)
    return render_template("question-5.html",message=message,score=score)

#--------------------Q5-------------------------------------------

@app.route('/q5',methods=['POST',"GET"])
def q5():
    if request.method=="GET":
        return render_template("question-5.html")
    message = validatequiz('3')
    score=session.get("user_score",0)
    return render_template("question-6.html",message=message,score=score)

#--------------------Q6-------------------------------------------

@app.route('/q6',methods=['POST',"GET"])
def q6():
    if request.method=="GET":
        return render_template("question-6.html")
    message = validatequiz('2')
    score=session.get("user_score",0)
    return render_template("question-7.html",message=message,score=score)

#--------------------Q7-------------------------------------------

@app.route('/q7',methods=['POST',"GET"])
def q7():
    if request.method=="GET":
        return render_template("question-7.html")
    message = validatequiz('2')
    score=session.get("user_score",0)
    return render_template("question-8.html",message=message,score=score)

#--------------------Q8-------------------------------------------

@app.route('/q8',methods=['POST',"GET"])
def q8():
    if request.method=="GET":
        return render_template("question-8.html")
    message = validatequiz('3')
    score=session.get("user_score",0)
    return render_template("question-9.html",message=message,score=score)

#--------------------Q9-------------------------------------------

@app.route('/q9',methods=['POST',"GET"])
def q9():
    if request.method=="GET":
        return render_template("question-9.html")
    message = validatequiz('1')
    score=session.get("user_score",0)
    return render_template("question-10.html",message=message,score=score)

#--------------------Q10-------------------------------------------

@app.route('/q10',methods=['POST',"GET"])
def q10():
    if request.method=="GET":
        return render_template("question-10.html")  
    message = validatequiz('3')
    score=session.get("user_score",0)
    message="Your score is "+ str(score) 
    return render_template("thank_you.html",new_message=message,score=score)

#--------------------THANKU-------------------------------------------

@app.route('/thanku')
def thanku():
    return render_template("thank_you.html")








if __name__=="__main__":
    app.run(debug=True)