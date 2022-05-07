import os
import self
import flask
import MySQLdb
from flask import Flask
application = Flask(_name_)


@application.route('/')
def hello_world():
    storage = Storage()
    storage.populate()
    score = storage.score()
    return "Hello Devops 123, %d!" % score
class Storage():
    def init(self):
        self.db = MySQLdb.connect(
        user = os.getenv('MYSQL_USERNAME'),
        passwd = os.getenv('MYSQL_PASSWORD'),
        db = os.getenv('MYSQL_INSTANCE_NAME'),
        host = os.getenv('MYSQL_PORT_3306_TCP_ADDR'),
        port = os.getenv('MYSQL_PORT_3306_TCP_PORT'))
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

if _name_ == "main":
    application.run(host='0.0.0.0', port=3000)
    # application.debug = True
