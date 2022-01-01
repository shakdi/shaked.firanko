from flask import Blueprint, render_template, request, redirect, session
from utilities.db_manager import dbManager

assignment10 = Blueprint(
    'assignment10',
    __name__,
    static_folder='assignment10',
    static_url_path='/assignment10',
    template_folder='templates')

@assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        id = request.form['id']
        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        country = request.form['country']
        query = "INSERT INTO users(id, email, firstname, lastname, country) Values ('%s','%s','%s','%s','%s')" % (id, email, firstname, lastname, country)
        dbManager.commit(query=query)
    return redirect('/assignment10')

@assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        id = request.form['id']
        query = "DELETE from users where id=('%s')" % id
        dbManager.commit(query=query)
    return redirect('/assignment10')

@assignment10.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        id = request.form['id']
        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        country = request.form['country']
        query_email = "update users set email=('%s') where id=('%s')" % (email, id)
        query_fname = "update users set firstname=('%s') where id=('%s')" % (firstname, id)
        query_lname = "update users set lastname=('%s') where id=('%s')" % (lastname, id)
        query_country = "update users set country=('%s') where id=('%s')" % (country, id)
        dbManager.commit(query=query_email)
        dbManager.commit(query=query_fname)
        dbManager.commit(query=query_lname)
        dbManager.commit(query=query_country)
    return redirect('/assignment10')


@assignment10.route('/assignment10')
def show():
    query = "select * from users"
    query_result = dbManager.fetch(query)
    return render_template('assignment10.html', users=query_result)