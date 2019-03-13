from flask import Flask , render_template , request , url_for , redirect , session
from forms import RegistrationForm , LoginForm
from scripts import inout_db
from models import  User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd69781f775f8a871d09f523f091df7e3'


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/auth", methods=['GET', 'POST'])
def auth():
    registration_form = RegistrationForm()
    login_form = LoginForm()
    if not session.get("logged_in"):
        if request.method == 'POST':
            if registration_form.validate():
                if registration_form.is_submitted():
                    user = User(request.registration_form)
                    inout_db.add_user(user)
        if request.method == 'GET':
            if login_form.is_submitted():
                if login_form.validate():
                    inout_db.get_user(login_form.email,login_form.password)

    return render_template("auth.html", reg_form=registration_form, log_form=login_form)




if __name__ == "__main__":
    app.run(debug=True)
