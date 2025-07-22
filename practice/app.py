from flask import Flask, render_template, request, flash, redirect, url_for 
from forms import LoginForm,Login2form
app = Flask(__name__) 


app.config['SECRET_KEY'] = 'your_secret_key_here' # Required for CSRF protection 

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/",methods=['GET','POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
     email = form.email.data
     password = form.password.data
     return redirect(url_for('home'))
    return render_template("login.html",form = form )



@app.route('/log2',methods = ['GET','POST'])
def Login2():
   form2 = Login2form()
   if form2.validate_on_submit():
      name = form2.name.data
      return redirect(url_for("home"))
   return render_template("login2.html",form2= form2)     




if __name__ == '__main__': app.run(debug=True)