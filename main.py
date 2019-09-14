from flask import Flask,render_template
from users import users

app = Flask(__name__)

app.register_blueprint(users)

@app.route("/")
def hello():
    return render_template('index.html', title = 'Bienvenidos')

if __name__ == "__main__":
    app.run(debug=True)