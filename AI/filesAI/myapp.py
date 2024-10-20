from flask import Flask, render_template, redirect, url_for, session,request,jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit
from authlib.integrations.flask_client import OAuth
from hiden2 import myid, mysecret
import os
import mysql.connector
import bcrypt 
from werkzeug.security import generate_password_hash
from PIL import Image
import json
from werkzeug.utils import secure_filename
from datetime import datetime
import logging
import pymysql

logging.basicConfig(level=logging.INFO)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")  # Allowing all origins for simplicity


oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id = myid,
    client_secret= mysecret,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    access_token_url='https://oauth2.googleapis.com/token',
    authorize_params=None,
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://127.0.0.1:5000/login/callback',
    client_kwargs={'scope': 'openid email profile'},
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
)

@app.route('/ty')
def index2():
    user = session.get('user')
    return render_template('query.html', user=user)

@app.route('/login')
def login():
    try:
        redirect_uri = url_for('authorize', _external=True)
        return redirect(google.authorize_redirect(redirect_uri).headers['Location'])
    except Exception as e:
        print(f"Error during login redirection: {str(e)}")
        return "An error occurred during login redirection."

    
@app.route('/login/callback')
def authorize():
    try:
        token = google.authorize_access_token()
        if not token:
            return 'Authorization failed.', 400

        resp = google.get('https://www.googleapis.com/oauth2/v1/userinfo')
        user_info = resp.json()
        session['user'] = user_info
        print(user_info)
        # Send a message to the parent window to indicate login success
        script = """
        <script>
            window.parent.postMessage('loginSuccess', '*');
        </script>
        """
        return script
    except Exception as err:
        print(f" ERROR>>: {err}")
        return render_template('query.html', msg=str(err))


@app.route('/logout')
def logout():
    session.pop('user', None)
    msg ="LOGGED OUT!!"
    
    #return render_template('accounton.html',msg=msg)



users = {}

@app.route('/')
def index():
    user = session.get('user')
    return render_template('query.html',user=user)



import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="worknest"
)
 
mycursor = mydb.cursor()


   

if __name__ == '__main__':
    socketio.run(app, debug=True)
