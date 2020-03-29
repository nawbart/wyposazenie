from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# konfigurcja ścieżki bazy danych
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wyposazenie.db"
db = SQLAlchemy(app)
from wyposazenie import routes
