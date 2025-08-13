from flask import Flask, render_template
from flask_cors import CORS
from views import views
import os

app = Flask(__name__, static_folder="static", template_folder="static/templates")
CORS(app)

app.register_blueprint(views, url_prefix="/api")

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")

def serve_react(path):
    
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return app.send_static_file(path)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
