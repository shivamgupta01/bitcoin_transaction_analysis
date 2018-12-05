from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
 
app = Flask(__name__)
 
posts = [
	{
		'transactionHash':'288da69e778b2afd3882d3dcfc70bbfb7aaf5fb95a2afbea14f35814ee2f21ac',
		'age': '3 seconds',
		'btc': '0.03229882 BTC',
		'usd': '1624.56'
	},
	{
		'transactionHash':'765f0a17a75626ec4892301733cd0578ca36408a680af8fe029a4bdae0ea45ad',
		'age': '2 seconds',
		'btc': '0.95238070 BTC',
		'usd': '3887.56'
	},
	{
		'transactionHash':'138497bdafcabb44f727a0ff23ac676b7f0ad25a52abc16fd6190536105b115c',
		'age': '4 seconds',
		'btc': '5.088 BTC',
		'usd': '4047.38'
	},
	{
		'transactionHash':'1d44ffb397c96688571f1ea1eee2803ffcef6e95b1d4b8a22bd964069a48c226',
		'age': '5 seconds',
		'btc': '0.1729882 BTC',
		'usd': '6191.24'
	},
	{
		'transactionHash':'20aef5e25859038f40dd6f3713b02ed250ff80c7bf248276483c35db74173f16',
		'age': '6 seconds',
		'btc': '0.03229882 BTC',
		'usd': '3408.12'
	},
	{
		'transactionHash':'288da69e778b2afd3882d3dcfc70bbfb7aaf5fb95a2afbea14f35814ee2f21ac',
		'age': '3 seconds',
		'btc': '0.03229882 BTC',
		'usd': '1624.56'
	},
	{
		'transactionHash':'765f0a17a75626ec4892301733cd0578ca36408a680af8fe029a4bdae0ea45ad',
		'age': '2 seconds',
		'btc': '0.95238070 BTC',
		'usd': '3887.56'
	},
	{
		'transactionHash':'138497bdafcabb44f727a0ff23ac676b7f0ad25a52abc16fd6190536105b115c',
		'age': '4 seconds',
		'btc': '5.088 BTC',
		'usd': '4047.38'
	},
	{
		'transactionHash':'1d44ffb397c96688571f1ea1eee2803ffcef6e95b1d4b8a22bd964069a48c226',
		'age': '5 seconds',
		'btc': '0.1729882 BTC',
		'usd': '6191.24'
	},
	{
		'transactionHash':'20aef5e25859038f40dd6f3713b02ed250ff80c7bf248276483c35db74173f16',
		'age': '6 seconds',
		'btc': '0.03229882 BTC',
		'usd': '3408.12'
	},
	{
		'transactionHash':'288da69e778b2afd3882d3dcfc70bbfb7aaf5fb95a2afbea14f35814ee2f21ac',
		'age': '3 seconds',
		'btc': '0.03229882 BTC',
		'usd': '1624.56'
	},
	{
		'transactionHash':'765f0a17a75626ec4892301733cd0578ca36408a680af8fe029a4bdae0ea45ad',
		'age': '2 seconds',
		'btc': '0.95238070 BTC',
		'usd': '3887.56'
	},
	{
		'transactionHash':'138497bdafcabb44f727a0ff23ac676b7f0ad25a52abc16fd6190536105b115c',
		'age': '4 seconds',
		'btc': '5.088 BTC',
		'usd': '4047.38'
	},
	{
		'transactionHash':'1d44ffb397c96688571f1ea1eee2803ffcef6e95b1d4b8a22bd964069a48c226',
		'age': '5 seconds',
		'btc': '0.1729882 BTC',
		'usd': '6191.24'
	},
	{
		'transactionHash':'20aef5e25859038f40dd6f3713b02ed250ff80c7bf248276483c35db74173f16',
		'age': '6 seconds',
		'btc': '0.03229882 BTC',
		'usd': '3408.12'
	}
]

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
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

@app.route('/home', methods=['GET','POST'])
def home1():
    return render_template('home.html',posts=posts)
 
@app.route("/logout", methods=['GET','POST'])
def logout():
    session['logged_in'] = False
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
