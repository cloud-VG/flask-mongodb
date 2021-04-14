from flask import Flask, render_template, request, redirect
import database as db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registry')
def registry():
    students = db.get_students()
    return render_template('registry.html', students=students)


@app.route('/registry/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        db.add_student(request.form)
        return redirect('/registry')
    else:
        return render_template('add.html')


@app.route('/registry/delete/<prn>')
def delete(prn):
    db.delete_student(prn)
    return redirect('/registry')


@app.route('/registry/edit/<prn>', methods=['GET', 'POST'])
def edit(prn):
    if request.method == 'POST':
        db.update_student(prn, request.form)
        return redirect('/registry')
    else:
        student = db.find_student(prn)
        return render_template('edit.html', student=student)


if __name__ == '__main__':
    app.run()
