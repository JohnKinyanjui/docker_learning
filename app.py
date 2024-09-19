from flask import Flask

app = Flask(__name__)
timesVisited = 0

@app.route("/")
def hello_world():
    global timesVisited  # Declare the variable as global to modify it
    timesVisited += 1  # Increment the global variable
    return f"<p>Hello, World! Times Visited: {timesVisited}</p>"  # Use f-string for formatting
