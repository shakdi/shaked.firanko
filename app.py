from flask import Flask, redirect, url_for, render_template

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

if __name__ == '__main__':
    app.run()

