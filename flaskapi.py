import os
import self
import flask
#import MySQLdb
import pymysql
from flask import Flask
application = Flask(__name__)


@application.route('/')
def hello_world():
    storage = Storage()
    storage.populate()
    score = storage.score()
    return "Hello Devops 123, %d!" % score
class Storage():
    def init(self):
        self.db = pymysql.connect(
        user = os.getenv('MYSQL_USERNAME', 'root'),
        passwd = os.getenv('MYSQL_PASSWORD', 'admin'),
        db = os.getenv('MYSQL_ROOT_DB', 'mydb'),
        host = os.getenv('MYSQL_ROOT_HOST', 'localhost'),
        port = os.getenv('MYSQL_ROOT_PORT', '3306'))
        cur = self.db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS scores(score INT)")

        def populate(self):
            cur = self.db.cursor()
            cur.execute("INSERT INTO scores(score) VALUES(1234)")

        def score(self):
            cur = self.db.cursor()
            cur.execute("SELECT * FROM scores")
        row = cur.fetchone()
        return row[0]

if __name__ == "main":
    application.run(host='0.0.0.0', port=3000)
    # application.debug = True
