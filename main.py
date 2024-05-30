
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
app.secret_key = 'Secret Key 123'
CORS(app)

@app.route("/", methods = ["GET"])
def return_index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host = '0.0.0.0')