from flask import Flask,render_template,request,jsonify
from flask_restful import Api,Resource,reqparse
import pandas as pd
import sqlite3
# import jsonify,requests


## creating projects database
conn=sqlite3.connect('data_science_app.db',check_same_thread=False)

# command= "ALTER TABLE projects ADD description VARCHAR tools_used VARCHAR link VARCHAR reference VARCHAR dataset VARCHAR;"
# conn.execute(command)
# print('table altered sucesfully')
# columns=[
#         "id INTEGER PRIMARY KEY",
#         "name VARCHAR UNIQUE",
#         "category VARCHAR",
#         "timestamp DATETIME",
# ]
# projects_table_cmd=f"CREATE TABLE projects({','.join(columns)})"
# conn.execute(projects_table_cmd)
# print('table created')


## Creating notes database
# notes_table_create_cmd="CREATE TABLE notes(id INTEGER PRIMARY KEY,title VARCHAR, category VARCHAR,timestamp DATETIME)"
# conn.execute(notes_table_create_cmd)
# print('notes table created')


## creating plans table in data_science_app db
# plans_create_cmd="CREATE TABLE plans(id INTEGER PRIMARY KEY,data DATETIME,name VARCHAR,description VARCHAR, priority INTEGER, finished VARCHAR)"
# conn.execute(plans_create_cmd)


# conn.execute("INSERT INTO plans VALUES (10,'2023-02-10','anil','YET TO BE FINISHED',5,1),(4,'2023-02-10','kumar','YET TO BE FINISHED',5,0),(6,'2023-02-10','anil','YET TO issued',5,0)")
# print('plans table  UPDATED created')





# app=Flask(__name__,template_folder='template')
app=Flask(__name__)
api=Api(app)
@app.route('/')
def index():
    return render_template('index.html')

db=[{
            'name':'anil',
            'second':'21',
            'city':'bang'
        },
        {
            'name':'kumar',
            'second':'22',
            'city':'hyd'
        }]
class Users(Resource):
    def get(self,data):
        # data=pd.read_csv('/home/divum/Data_Science_Flask/venv/users.csv')
        # data=data.to_dict('records')
       
        return {'data':data},200
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('name',required=True)
        parser.add_argument('age',required=True)
        parser.add_argument('city',required=True)
        args=parser.parse_args()

        # data=pd.read_csv('/home/divum/Data_Science_Flask/venv/users.csv')

        new_data=pd.DataFrame({
            'name':[args['name']],
            'age':[args['age']],
            'city':[args['city']]
        })

        # data=data.append(new_data,ignore_index=True)
        # data.to_csv('users.csv',index=False)
        return jsonify(pd.to_dict(new_data)),201
    def delete(self):
        parser=reqparse.RequestParser()
        parser.add_argument('name',required=True)
        args=parser.parse_args()

        data=pd.read_csv('/home/divum/Data_Science_Flask/venv/users.csv')
        data=data[data['name']!=args['name']]
        data.to_csv('users.csv',index=False)
        return {'message':'record deleted successfully'},200




api.add_resource(Users,'/users')

@app.get('/show')
def learn():
    # print('jsonify of db is',jsonify(db))
    return jsonify(db)

@app.post('/show')
def add_user():
    if request.is_json:
        user=request.get_json()
        db.append(user)
        return db,201
    return 'bad input',405


@app.route('/projects')
def projects():
    return render_template('projects.html')



### plans
@app.route('/plans')
def plans():
    return render_template('plan.html')

@app.post('/select_date')
def date_chosen():
    if request.method=="POST":
        date_value=request.form['date']
        print("date value read from html is ",date_value)
        cur=conn.cursor()
        cur.execute("SELECT * FROM plans")
        rows=cur.fetchall()

        print('rows is=========================',rows)
        left,right=[],[]
        for i in rows:
            print('=========----------..........',i)
            print('after string conversion',str(date_value))
            if i[1]==str(date_value):
                print('-------------------->>>',i[1])
                print('=========================>>>>',date_value)
                if i[-1]==1:
                    print('right side entered+++++++++++++++++++++++++++++++')
                    right.append(i)
                else:
                    print('left side entered--------------------------------')

                    left.append(i)

        return render_template('plan.html',data=[left,right])

    #  if request.method == "POST":
    #    date = request.form['date']
    #    return date

# return render_template(login.html)




@app.route('/notes')
def notes():
    return render_template('notes.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', port=4459,debug=True)

# import sqlite3
# >>> conn = sqlite3.connect("people.db")
# >>> columns = [
# ...     "id INTEGER PRIMARY KEY",
# ...     "lname VARCHAR UNIQUE",
# ...     "fname VARCHAR",
# ...     "timestamp DATETIME",
# ... ]
# >>> create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
# >>> conn.execute(create_table_cmd)