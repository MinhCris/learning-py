from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace this with a strong secret key in production

# Sample user dictionary to store user credentials (username: password)
users = {
    "john_doe": "password123",
    "alice": "p@ssw0rd",
    # Add more users as needed
}

def is_authenticated(username, password):
    return username in users and users[username] == password

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if is_authenticated(username, password):
            session["username"] = username
            return redirect(url_for("dashboard"))

        return render_template("login.html", message="Invalid username or password.")

    return render_template("login.html", message="")

@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return f"Welcome to the dashboard, {session['username']}!"
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
