from flask import Blueprint, render_template, request, redirect, session, Response
import json
import requests
import mysql.connector


# ------------------------------------------------- #
# ------------- DATABASE CONNECTION --------------- #
# ------------------------------------------------- #
def interact_db(query, query_type: str, named_tuple=True, dictionary=None):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='root',
                                         database='shaked')
    if dictionary and named_tuple:
        raise Exception('Only one of named tuple or dictionary can be chosen')
    cursor = connection.cursor(named_tuple=named_tuple, dictionary=dictionary)
    cursor.execute(query)
    #

    if query_type == 'commit':
        # Use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

assignment10 = Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
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
        interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

@assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        id = request.form['id']
        query = "DELETE from users where id=('%s')" % id
        interact_db(query=query, query_type='commit')
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
        interact_db(query=query_email, query_type='commit')
        interact_db(query=query_fname, query_type='commit')
        interact_db(query=query_lname, query_type='commit')
        interact_db(query=query_country, query_type='commit')
    return redirect('/assignment10')


@assignment10.route('/assignment10')
def show():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)

@assignment10.route('/assignment11/users')
def list_users():
    query = "select * from users"
    query_result = interact_db(query, query_type='fetch')
    return Response(json.dumps(query_result), mimetype='application/json')


@assignment10.route('/req_frontend')
def req_frontend_func():
    return render_template('req_frontend.html')


@assignment10.route('/req_backend')
def req_backend_func():
    user = request.args.get('userID')
    data = None
    if user:
        res = requests.get("https://reqres.in/api/users/%s" % user, verify=False)
        data = res.json()['data']
    return render_template('req_backend.html', requestUser=data)