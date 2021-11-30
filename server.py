from flask import Flask, render_template,request,redirect

from user import User



app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users/new')

@app.route('/users', methods=["GET","POST"])
def user():
    return render_template('read(All).html', users=User.get_all())

@app.route('/users/new')
def new():
    return render_template('create.html')

@app.route('/users/create', methods=["POST"])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')


@app.route('/edit/<int:id>')
def edit(id):
    data ={
        'id':id
    }
    return render_template('edit_user.html', user=User.get_one(data))

@app.route('/show/<int:id>')
def show(id):
    data ={
        'id': id
    }
    return render_template('show_user.html', user=User.get_one(data))


@app.route('/users/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/delete/<int:users_id>')
def delete(users_id):
    data ={
        'id': users_id,
    }
    User.destroy( data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)





            

