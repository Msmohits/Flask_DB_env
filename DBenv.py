# TO interact with Operating System.
import os
# To load environment variable from a file.
from dotenv import load_dotenv
# TO develop web application using flask library.
from flask import Flask
# To handle database connection across the app.
from flask_sqlalchemy import SQLAlchemy
# Flask constructor.
app = Flask(__name__)
# Making connection for both database from .env file
load_dotenv()
PG_CONN = os.getenv('PG_CONN')
SQ_CONN = os.getenv('SQ_CONN')
# The database URI used for the connection and dictionary that maps bind keys to SQLAlchemy connection URIs.
app.config['SQLALCHEMY_DATABASE_URI'] = PG_CONN
app.config['SQLALCHEMY_BINDS'] = {
    'db1': SQ_CONN,
}
# Map database schema to the app.
db = SQLAlchemy(app)


# Decorating route URL for postgresql.Making empty list and append all table column data to it.
@app.route('/postgresql')
def postgresql():
    pgsql_data = PGuser.query.all()
    pgalllist = []
    for item in pgsql_data:
        pgalllist.append(item.id)
        pgalllist.append(item.name)
        pgalllist.append(item.section)
    return str(pgalllist)

# Decorating route URL for mysql.Making empty list and append all table column data to it.
@app.route('/mysql')
def mysql():
    sql_data = SQLuser.query.all()
    pgalllist = []
    for item in sql_data:
        pgalllist.append(item.id)
        pgalllist.append(item.name)
        pgalllist.append(item.desig)
    return str(pgalllist)


# Making function and determines the logical structure of a database for postgresql.
class PGuser(db.Model):
    __tablename__ = 'students'
    id = db.Column('std_id', db.Integer, primary_key=True)
    name = db.Column('std_name', db.String(50))
    section = db.Column('std_section', db.String(70))


# Making function and determines the logical structure of a database for mysql.
# Using bind key so that model connects to the specified database connection itself.
class SQLuser(db.Model):
    __bind_key__ = 'db1'
    __tablename__ = 'employees'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(50))
    desig = db.Column('desig', db.String(70))


# Attribute value set to run the main program.
if __name__ == '__main__':

    app.run()
