from flask import render_template, request, Flask
from db import Base, Document
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from flask_restful import Api, Resource
from services import Count
import json

app = Flask(__name__, template_folder="templates")
api = Api(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}

engine = create_engine("postgresql://postgres:1234@localhost:5432/test", echo=True)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
    return render_template('home.html')

class UploadFile(Resource):
    def post(self):
        data = json.loads(request.get_json())
        file_text = data.get('fileText', None)
        new_document = Document(file_text= file_text)
        session.add(new_document)
        session.commit()
        c = Count(file_text, session)
        result = c.make_json()
        return result


api.add_resource(UploadFile, '/upload-file')

if __name__ == '__main__':
    app.run(host='127.1.1.1', port=8100, debug=True)