from flask import Flask, request, render_template_string
import psycopg2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
       peoplename = request.form["peoplename"]
       password = request.form["password"]
    try:
	conn = psycopg2.connect(
		dbname= "testdb",
		user="postgres",
		password-"Love1Home2!.",
		host="localhost"
	)
	cur = conn,cursor()

query = f"SELECT * FROM people WHERE peoplename = '{peoplename}' AND password = '{password}'"
cur.execute(query)
rows = cur.fetchall()

	if rows:
		message = f"logged in as {peoplename}"
	else:
		message  =" Invaild login"

	cur.close()
	conn.close()

	except Exception as e:
		message =f"Database error:{e}"

    return render_template_string("""
	<h2>Vulnerable Login (SQL Injection Lab)</h2>
	<form method="post">
		People Name: <input name="peoplename"><br>
		Password: <input name="password"><br>
		<button type="submit">Login</button>
	</form>
	<p>{{ message }}</p>
    """, message=message)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
