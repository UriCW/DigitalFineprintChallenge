from flask import Flask, render_template,jsonify
from perfect_numbers import classify
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("main.html")

@app.route('/<int:number>')
def classify_number(number):
    return jsonify(number=number,classification=classify(number))


if __name__=='__main__':
    app.config.update(TEMPLATES_AUTO_RELOAD=True)
    app.run(host='localhost', port=5001)
