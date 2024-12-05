from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

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

app.config['SQLALCHEMY_DATEBASE_URI'] = f"mysql+pymysql://{username}:{password}@{homename}:{port}/{database}?charset=utf-8"

db = SQLAlchemy(app)

with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute("select 1")
        print(rs.fetchone())

@app.route('/')
def index():
    return 666

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)