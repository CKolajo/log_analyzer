from flask import Flask, request, session, redirect, render_template_string
import pyotp, qrcode, io, base64, os

app = Flask(__name__)
app.secret_key = os.urandom(32) # dev only

TEMPLATE_SETUP= """
<h2>2FA Setup</h2>
<p>Scan this QR in Google Authenticator, Authy, or 1Password:</p>
<img src="data:image/png;base64,{{ png_b64 }}">
<form method="POST" action="/verify-setup">
 <input name="token" placeholder="123456" />
 <button type="submit">Verify & Finish</button>
</form
"""
TEMPLATE_TOTP = """
<h2>Enter 2FA Code</h2>
<form method="POST">
 <input name="token" placeholder="123456" />
 <button type="submit">Verify</button>
</form>
"""
TEMPLATE_HOME = "<h3>Welcome {{user}}  2FA passed </h3>"

@app.route("/", methods=["GET", "POST"])
def login():
  if request.method =="GET":
   return render_template_string(TEMPLATE_LOGIN)
  # dummy auth (replace with DB)
  if request.form.get("username") and request.form.get("password"):
   session["user"] = request.form["username"]
   # if no TOTP secret yet, go to setup
   if "totp_secret" not in session:
    return redirect("/setup-2fa")
  return redirect("/2fa")
  return"Invaild",401

@app.route("/setup-2fa")
def setup_2fa():
  secret = pyotp.random_base32()
  session["totp_secret"] = secret
  totp = pyotp.TOTP(secret)
  uri = totp.provisioning_url(name=session["user"], issuer_name="Lab-9A")
  img = qrcode.make(uri)
  buf = io.BytesIO(); img.save(buf, format="PNG")
  png_b64 = base64.b64encode(buf.getvalue()).decode()
  return rende_template_string(TEMPLATE_SETUP, png_b64=png_b64)

@app.route("/verify-seetup", methods=["POST"])
def veify_setup():
  token = request.form.get("token","")
  totp = pyotp.TOTP(session["totp_secret"])
  if totp.verify(token, valid_window=1):
   session["2fa_enrolled"] = True
   return redirect("/2fa")
  return "Invalid token", 400


@app.route("/2fa", methods=["GET", "POST"])
def twofa():
  if "totp_secret" not in session:
   return redirect("/")
  if request.method == "GET":
   return render_template_string(TEMPLATE_TOTP)
  token = request.form.get("token", "")
  totp = pyotp.TOTP(session["totp_secret"])
  if totp.verify(token, valid_window=1):
   session["2fa_ok"] = True
   return redirect("/home")
  return "Invalid 2FA code", 400

@app.route("/home")
def home():
  if not session.get("2fa_ok"):
   return redirect("/")
  return rende_template_string(TEMPLATE_HOME, user=session["user"])

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5050, debug=True)
