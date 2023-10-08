from flask import Flask, render_template, request
# Data from backend to frontend
app = Flask(__name__)
@app.route("/")
def home():
    first_name = input("Enter your name!")
    
    return render_template("home.html",data = {"first_name":first_name})

@app.route("/about", methods=["GET","POST"])
def about():

    if request.method=="POST":
        num1=int(request.form['Num1'])
        num2=int(request.form['Num2'])
       
        result=num1 + num2

    last_name=input("Enter your last name")
   
    return render_template("about.html", result={"result":result})

@app.route("/Contact")
def ContactUs():
    contact=input("Enter Your Contact please!")
    return render_template("Contact.html",data2={"contact":contact})


if __name__ == "__main__":
    app.run(debug=True)