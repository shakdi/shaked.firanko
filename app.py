from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

@app.route('/')
def MyPage():
    return render_template('exercise2.html')

@app.route('/HomePage')
def HomePage():
    return redirect(url_for('MyPage'))

@app.route('/Home')
def Home():
    return redirect('/')

@app.route('/cv')
def CV():
    return render_template('cv.html')

@app.route('/cssExemple')
def ce():
    return render_template('cssExemple.html')

@app.route('/CVgrid')
def CVG():
    return render_template('CVgrid.html')

@app.route('/form')
def f():
    return render_template('form.html')


@app.route('/RWDexemple')
def RWD():
    return render_template('RWDexemple.html')

@app.route('/assignment8')
def assignment8():
    return render_template('assignment8.html')

@app.route('/logout',methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    session['username'] = ' '
    return render_template('assignment9.html')


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    userslist=[{"id": 123, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson", "Country": "Israel"},
            {"id": 456, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson", "Country": "USA"},
            {"id": 789, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke", "Country": "France"},
            {"id": 101, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields", "Country": "Germany"},
            {"id": 122, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards", "Country": "Turkey"},
            {"id": 111, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell", "Country": "USA"}]

    username=''
    searchname=''
    if request.method == 'GET':
        if 'name' in request.args:
            searchname = request.args['name']
        if searchname == '':
            return render_template('assignment9.html', userslist=userslist)
        else:
            return render_template('assignment9.html', username=searchname, userslist=userslist,
                                   request_method=request.method)

    if request.method == 'POST':
        user = request.form['username']
        session['logged_in'] = True
        session['username'] = user
        return render_template('assignment9.html')
    return render_template('assignment9.html')


if __name__ == '__main__':
    app.run()

