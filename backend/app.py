from flask import Flask
from flask_cors import CORS
from views import views

app = Flask(__name__)
CORS(app)

app.register_blueprint(views, url_prefix = '/api')

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")