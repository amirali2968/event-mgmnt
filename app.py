import mysql.connector,sys
import datetime
from mysql.connector import Error
from flask import Flask, request, jsonify, render_template,redirect, url_for
from random import randint
from routes.admin import admin_bp
from routes.participants import participants_bp
from routes.login import login_bp
from routes.event_type import event_type_bp
from routes.event_info import event_info_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(participants_bp)
app.register_blueprint(login_bp)
app.register_blueprint(event_type_bp)
app.register_blueprint(event_info_bp)

def runQuery(query):

    try:
        db = mysql.connector.connect( host='localhost',database='event_mgmt',user='root',password='password')

        if db.is_connected():
            print("Connected to MySQL, running query: ", query)
            cursor = db.cursor(buffered = True)
            cursor.execute(query)
            db.commit()
            res = None
            try:
                res = cursor.fetchall()
            except Exception as e:
                print("Query returned nothing, ", e)
                return []
            return res

    except Exception as e:
        print(e)
        return []

    db.close()

    print("Couldn't connect to MySQL")
    return None


if __name__ == "__main__":
    app.run()
