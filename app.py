from main import create_app
from flask import render_template, request, redirect
# from forms import FoodForm
# from db import Food


app = create_app()

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password1@localhost:5432/test"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/upload-file', methods=['POST'])
def upload():
    file = request.files['file']
    return file.filename


if __name__ == '__main__':
    app.run(host='127.1.1.1', port=8100, debug=True)