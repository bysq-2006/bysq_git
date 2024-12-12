from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

def pow(base:int, n:int = 2) -> int:
    sum:int = 1
    for i in range(0,n,1):
        sum *= base
    return sum

app = Flask(__name__)

homename = "127.0.0.1"

port = 3306

username = "root"

password = "root"

database = "bysq"

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@{homename}:{port}/{database}?charset=utf8"

db = SQLAlchemy(app)

class home417(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    database_list = []
    return str(database_list)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)