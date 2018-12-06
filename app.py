from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
import fetch_data
engine = create_engine('sqlite:///tutorial.db', echo=True)
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        posts = []
        temp_list = fetch_data.fetch_recent_transaction()    
        for item in temp_list:
            temp_dict = {'transactionHash':str(item[0]),'age':str(item[2]),'btc':str(item[1]),'usd': '6191.24'}
            posts.append(temp_dict)
        return render_template('home.html', posts=posts)
 
@app.route('/login', methods=['POST'])
def do_admin_login():
 
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route('/home', methods=['GET'])
def home1():
        posts = []
        temp_list = fetch_data.fetch_recent_transaction()    
        for item in temp_list:
            temp_dict = {'transactionHash':str(item[0]),'age':str(item[2]),'btc':str(item[1]),'usd': '6191.24'}
            posts.append(temp_dict)
        return render_template('home.html',posts=posts)
 
@app.route("/logout", methods=['GET','POST'])
def logout():
    session['logged_in'] = False
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
