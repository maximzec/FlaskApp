from flask import Flask , render_template , request , url_for , redirect , session ,jsonify ,json
from forms import RegistrationForm , LoginForm
from flask_pymongo import PyMongo
from models import  User


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "local"
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
app.config['SECRET_KEY'] = 'd69781f775f8a871d09f523f091df7e3'

mongo = PyMongo(app)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/auth", methods=['GET', 'POST'])
def auth():
    registration_form = RegistrationForm()
    login_form = LoginForm()

    users = mongo.db.users
    if not session.get("logged_in"):
        if request.method == 'POST':
            if registration_form.validate():
                if registration_form.is_submitted():
                    user = User(request.registration_form)
                    users.insert({'first-name': user.first_name , 'last-name': user.last_name , 'email': user.email,
                                  'password': user.password})
                    return "USER ADDED:" + jsonify(user)
        if request.method == 'GET':
            if login_form.is_submitted():
                if login_form.validate():
                    return "OK"
    return render_template("auth.html", reg_form=registration_form, log_form=login_form)




if __name__ == "__main__":
    app.run(debug=True)
