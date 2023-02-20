from flask import Flask,render_template

app=Flask(__name__)



@app.route('/')
def index():
    render_template('base.html')

@app.route('/learn')
def learn():
    render_template('learn.html')

@app.route('/projects')
def projects():
    render_template('projects.html')

@app.route('/plans')
def plans():
    render_template('plans.html')

@app.route('/notes')
def notes():
    render_template('notes.html')




if __name__=="__main__":
    app.run(debug=True)