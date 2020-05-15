from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# konfigurcja sciezki bazy danych
app.config["SECRET_KEY"] = "ca228fe05da3f26ff064bf69b5960a12"
# konfigurcja ścieżki bazy danych
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wyposazenie.db"
db = SQLAlchemy(app)
from wyposazenie import routes
