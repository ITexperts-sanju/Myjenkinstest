from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify("message": "Hello from Flask running in Docker! and this is our jenkin successfull test bro"})
@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
