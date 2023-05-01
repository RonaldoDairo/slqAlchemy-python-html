# from app import app
# from utils.db import db

# with app.app_context():
#     db.create_all()

# if __name__ == "__main__":
#     app.run(debug=True)



## Tuve que use este codigo de abajo para poder que funcionara
from flask import Flask
from routes.contacts import contacts
from utils.db import db
from config import DATABASE_CONNECTION_URI
app = Flask(__name__)
app.secret_key = "secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(contacts)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)