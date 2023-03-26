from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'#name or path to our database
#app.config['SQLALCHEMY_TRAK_MODIFIATIONS']=False
db=SQLAlchemy(app) #gets the app
class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    #show all todo
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html',todo_list = todo_list)
@app.route('/add',methods=["POST"])
def add():
    title = request.form.get('title')
    new_todo = Todo(title=title,complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index')) #fun name inside urlfor

@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo=Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('index')) #fun name inside urlfor

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo=Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index')) #fun name inside urlfor

@app.route('/')
def about():
    return 'about'

if(__name__)=='__main__':
    with app.app_context():
        db.create_all() 
        # new_todo = Todo(title='todo 1',complete=False)
        # db.ses sion.add(new_todo)
        # db.session.commit()
    app.run(debug=True) #development mode