from flask import Blueprint, url_for, render_template, jsonify, request
from prediction import run_inference

views = Blueprint("views", __name__)

@views.route('/run-model', methods = ["POST"])
def main_infernce():
        try:
            data = request.get_json()
            raw_data = data.get("image")
            print("got_data")
            
            if not raw_data:
                return jsonify({"error": "No image found"}), 400
            
            res = run_inference(raw_data)
            return jsonify({"message": res})
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    