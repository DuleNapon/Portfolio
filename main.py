from flask import Flask, render_template
from database import certificates

app = Flask(__name__)



@app.route("/")
def Home():
    return render_template("home.html", certificates=certificates)

@app.route("/cert")
def cert():
    return render_template("cert-galery.html", certificates=certificates)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)