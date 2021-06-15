from flask import Flask,render_template,request,session
#Flask is a micro framework

app=Flask(__name__)
app.config["SECRET_KEY"]="1234"
@app.route('/')
def home():
    return "WELCOME"

@app.route('/home')
def hello():
    return render_template("h1.html")

@app.route('/number', methods=['GET', 'POST'])
def number():
    return render_template("create.html") 

@app.route('/even_or_odd', methods=['GET', 'POST'])
def even_or_odd():
    num=request.form.get("number")
    num=int(num)
    message=""
    if num%2==0: 
        message="This is an even number"
    else:
        message="This is an odd number"
    return render_template("create.html",message=message)

@app.route('/get_string')
def get_string():
    return render_template("okay.html")
   
@app.route('/reverse_string')
def reverse_string():
    str=request.args.get("string")
    rev_str=""
    for i in str:
        rev_str=i+rev_str
    return render_template("okay.html",rev_str=rev_str) 


@app.route('/login_page')
def login_page():
   return render_template("login_page.html")


@app.route('/validate_user')
def validate_user():
    users={"User_1":1234,"User_2":4321,"User_3":0000}
    user_name=request.args.get("username")
    password=request.args.get("password",type=int)
    get_user=users.get(user_name)
    message=""
    if get_user==password:
        message="You have succesfully logged in!!!😃"
    else:
        message="You have failed to login!!!😔"
    return render_template("login_page.html",message=message)


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





































if __name__=="__main__":
    app.run(debug=True)