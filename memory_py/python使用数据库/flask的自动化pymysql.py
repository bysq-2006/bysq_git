from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

def pow(base:int, n:int = 2) -> int:
    sum:int = 1
    for i in range(0,n,1):
        sum *= base
    return sum
#----------------------------------------------------------必要信息-----------------------------------------------------------------
app = Flask(__name__)

homename = "127.0.0.1"

port = 3306

username = "root"

password = "root"

database = "bysq"

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@{homename}:{port}/{database}?charset=utf8"

#---------------------------------------------------------------------------------------------------------------------------

db = SQLAlchemy(app)

database_list = []
#---------------------------------------------------------链接并使用sql语句------------------------------------------------------------------

with app.app_context():
    with db.engine.connect() as conn:
        home417 = conn.execute(text("select * from home417;"))
        home417_wai = conn.execute(text("select * from home417_外;"))
        database_list.append(home417.fetchall())
        database_list.append(home417_wai.fetchall())
#---------------------------------------------------------------------------------------------------------------------------

@app.route('/')
def index():
    return str(database_list)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)