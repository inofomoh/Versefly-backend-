from flask import Flask, request, jsonify
from generate_film import generate_full_film

app = Flask(__name__)

@app.route("/generate_film", methods=["POST"])
def generate_film():
    data = request.get_json()
    script = data.get("script", "")
    result = generate_full_film(script)
    return jsonify({"status": "success", "output_file": result})

if __name__ == "__main__":
    app.run(debug=True)