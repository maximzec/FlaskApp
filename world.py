from flask import Flask , render_template , request , url_for , redirect
from forms import RegistrationForm , LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'd69781f775f8a871d09f523f091df7e3'


@app.route("/", methods = ['GET', 'POST'] )
def home():
    return render_template("index.html")


@app.route("/auth" , methods =['GET' , 'POST'])
def auth():
    form = RegistrationForm()
    if form.is_submitted():
        result = request.form
        print(result)
    return render_template("auth.html" , form = form)




if __name__ == "__main__":
    app.run(debug=True)
