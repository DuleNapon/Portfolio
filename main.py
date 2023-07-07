from flask import Flask, render_template

app = Flask(__name__)

certificates = [
    {
      "name": "Crash course on Python by Google",
      "image": "Crash course on Python by Google.pdf"
    },
    {
      "name": "Crash course on Python by Google",
      "image": "Python.jpg"
    },
    {
      "name": "Using Python to interact with the Operating System by Google",
      "image": "Interacting with OS.jpg"
    },
    {
      "name": "Introduction to Git and GitHub by Google",
      "image": "Git and GitHub.jpg"
    }
]

@app.route("/")
def Home():
    return render_template("home.html", certificates=certificates)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)