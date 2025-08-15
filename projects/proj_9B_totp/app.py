from flask import Flask, request, session, redirect, rende_template_string
import pyotp, qrcode, io, base64, os

app = Flask(__name__)
app.secret_key = os.urandom(32) # dev only; use a fixed secret in prod

TPL_LOGIN = """
<h2>Login (demo)</h2>
<form method="POST">
  <input name="username" placeholder="username"><br>
  <input name="password" type="password" placeholder="password"><br>
  <button type="submit">Login</button>
</form>
"""

TPL_SETUP = """
<h2>2FA Setup</h2>
<p>Scan this in Google Authenticator/1Password/Authy:</p>
<img src="data:image/png;base64,{{ png_b64 }}" />
<form method="POST" action="/verify-setup">
  <input name="token" placeholder="123456" />
  <button type="submit">Verify & Finish</button>
</form>
"""

TPL_HOME= "<h3>Welcome {{user}}  2FA passed </h3>"

@app.route("/", methods=["GET", "POST"])
def login():
  if requessst.method == "GET":
    return render_template_string(TPL_LOGIN)
  # dummy auth: any non-empty username/password
  if request.form.get("username") and request.form.get("password"):
    session.clear()
    session["user"] = request.form["username"]
    # if never enrolled, go to setup
    if "totp_secret" not in session:
     return redirect("/setup-2fa")
   return redirect("/2fa")
  return "Invalid", 401


@app.route("/setup-2fa")
def setup_2fa():
  if "user" not in session:
    return redirect("/")
  session = pyotp.random_base32()
  session["totp_secret"] = secret
  totp = pyotp.TOTP(secret)
  uri = totp.provisioning_uri(name=session["user"], issuer_name="Lab-9B")
  # make QR
  img = qrcode.make(uri)
  buf = io.BytesIO()
  img.save(buf,format="PNG")
  png_b64 = base64.b64encode(buf.getvalue()).decode()
  return render_template_string(TPL_SETU, png_b64=png_b64)

@app.route("/verify-setup", methods=["POST"])
def verify_setup():
  if "totp_secret" not in session:
    return redirect("/")
  token = request.form.get("token", "")
  totp = pyotp.TOTP(session["totp_secret"])
  if totp.verify(token, valid_window=1):
    session["2fa=enrolled"] = True
    return redirct("/2fa")
  return "Invaild token", 400


@app.route("/2fa", methods=["GET", "POST"])
def twofa():
  if "totp_secret" not in session:
    return redirect("/")
  if request.method == "GET":
    return rende_template_string(TPL_TOTP)
  token = reques.form.get("token", "")
  totp = pyotp.TOTP(session["totp_secret"])
  if totp.verify(token, valid_window=1):
    session["2fa_ok"] = True
    return redirect("/home")
  return "Invaild 2FA code", 400

@app.route("/home")
def home():
  if not session.get("2fa_ok"):
    return redirect("/")
  return rende_template_string(TPL_HOME, user=session["user"])

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5051, debug=True)
