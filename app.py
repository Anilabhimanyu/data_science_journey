from flask import Flask,render_template

# app=Flask(__name__,template_folder='template')
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/plans')
def plans():
    return render_template('plan.html')

@app.route('/notes')
def notes():
    return render_template('notes.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')



if __name__=="__main__":
    app.run(debug=True)