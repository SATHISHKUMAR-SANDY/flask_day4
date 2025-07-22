from flask import Flask, render_template, request, flash, redirect, url_for,Blueprint

from form import messageForm
views = Blueprint('views', __name__)
@views.route('/home',methods =['GET','POST'])
def home():
    name = request.args.get("name")
    email = request.args.get("email")
    message = request.args.get("message")
    gender = request.args.get("gender")
    terms = request.args.get('terms') 
    date = request.args.get('date')
    age = request.args.get('age')
    return render_template("index.html",name= name,email=email,message=message,gender = gender,terms=terms,date = date,age=age)


@views.route("/",methods = ['POST','GET'])
def message_form():
    message_form =  messageForm()
    if request.method == 'GET':
        message_form.name.data = "Sathish Kumar"
        message_form.email.data = "sathish@example.com"
        message_form.gender.data = 'A'
    if message_form.validate_on_submit():
        name = message_form.name.data
        email = message_form.email.data
        message = message_form.message.data
        gender = message_form.gender.data
        terms = message_form.accept_term.data
        date = message_form.date.data
        age = message_form.age.data
        print(name)
        print(email)
        print(message)
        print(gender)
        return redirect(url_for('home',name= name,email=email,message=message ,gender=gender,terms=terms,date =date,age=age))
    return render_template("form.html",message = message_form)


@views.route("/success")
def success():
    return "Form submitted successfully!"


