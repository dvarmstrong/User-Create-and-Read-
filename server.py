from flask import Flask, render_template,request,redirect

from user import User



app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users/new')

@app.route('/users/')
def user():
    return render_template('/read(All).html', users=User.get_all())

@app.route('/users/new')
def new():
    return render_template('create.html')

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users/')



if __name__ == "__main__":
    app.run(debug=True)





            
