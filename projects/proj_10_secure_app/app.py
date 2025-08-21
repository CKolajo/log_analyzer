import os, sqlite3
from flask import Flask, request, redirect, sessio, render_template_string, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, Passwordfield, SubmitField
from wtforms.validators import DataRequired, Length
from passlib.hash import bcrypt

#---Config---
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("APP_SECRET_KEY", os.urandom(32))
DB_PATH = " data/app.db"


#---Forms---
class RegisterForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired(), Length(min=3, max=32)])
  password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
  submit = SubmitField("Register")


class LoginForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired()])
  submit = SubmitField("Login")

# --- Templates (simple inline for now) ---
TPL_BASE = """
  <!doctype html><title>Secure App</title>
  <h2>{{ title }}</h2>
  {% with msgs = get_flashed_messages() %}
   {% if msgs %}<ul>{% for m in msgs %}<li>{{ m }}</li>{% endfor %}</ul>{% endif %}
  {% endwith %}
  {{ body|safe }}
"""

def render(title, body):
  return render_template_string(TLP_BASE, title=title, body=body)

def get_db():
  con = sqlite3.connect(DB_PATH)
  con.row_factory = sqlite3.Row
  return con

@app.route("/")
def index():
  user = session.get("user")
  body = f"<p>Welcome {user or 'guest'}.</p><p><a href='{url_for('register')}'>Register</a> | <a href='{url_for('login')}'>Login</a> | <a href='{url_for('logout')}'>Logout</a></p>"
  return render("Home", body)

#--- Register ---
@app.route("/register", methods=["GET", "POST"])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
   username = form.usename.data.strip()
  password_hash = bcrypt.hash(form.password.data)
  try:
   con = get_db(); cur = con.cursor()
   con.execute("INSERT INTO users(username, password_hash) VALUES(form.username.data, password_hash")
   con.commit()
   flash("Registration successful. Please log in.")
   return redirect(url_for("login"))
  except sqlite3.IntegrityError:
   flash("Username already taken.")
  finally:
   con.close()
  body = render_template_string("""
<form method="POST">
  {{ form.hidden_tag() }}
  {{ form.username.label }} {{ form.username(size=32) }}<br>
  {{ form.password.label }} {{ form.password(size=32) }}<br>
  {{ form.submit() }}
</form>
""", form=form)
     return render("Register", body)


#--- Login ---
@app.route("/login",methods=["GET", "POST"])
def login():
  form = LoginForm()
  if form.validate_on_sumbit():
   username = form.username.date.strip()
   password = form.password.data
   con = get_db(); cur = con.cursor()
   cur.execute("SELECT id, username, password_hash, FROM users WHERE username = ?",(username,))
   row = cur.fetchone()
   con.close()
   if row and bycrpt.verify(password, row["password_hash"]):
    session.clear()
    session["user"]= row["username"]
    session["uid"] = row["id"]
    flash("Logged in.")
    return redirect(url_for("dashboard"))
   flash("Invalid credentails.")
  body = render_template_string("""
<form method="POST">
  {{ form.hidden_tag() }}
  {{ form.username.label }} {{ form.username(size=32) }}<br>
  {{ form.password.label }} {{ form.password(size=32) }}<br>
  {{ form.submit() }}
</form>
""", form=form)
  return render("Login", body)

@app.route("/dashboard")
def dashboard():
  if "user" not in session:
   return redirect(url_for("login"))
  body = f"<p>Hi, {session['user']}! </p><p>Protected content here.</p>"
  return render("Dashboard", body)

@app.route("/logout")
def logout():
  session.clear()
  flash("Logged out.")
  return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5070, debug=True)
