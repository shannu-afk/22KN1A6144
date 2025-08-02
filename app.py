import secrets
from datetime import datetime, timedelta

from flask import Flask, jsonify, redirect, request

app = Flask(__name__)

# Store URL mappings in memory
url_store = {}


# Helper to generate unique short ID
def generate_short_id(num_chars=6):
    return secrets.token_urlsafe(num_chars)[:num_chars]


# Route to shorten the URL
@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")
    expires_in_minutes = data.get("expires_in_minutes", 30) 

    if not original_url:
        return jsonify({"error": "Missing 'url'"}), 400

    short_id = generate_short_id()
    expiry_time = datetime.utcnow() + timedelta(minutes=expires_in_minutes)
    url_store[short_id] = {"original_url": original_url, "expiry_time": expiry_time}

    # Adjust to IST (UTC+5:30)
    ist_expiry_time = expiry_time + timedelta(hours=5, minutes=30)
    ist_time_str = ist_expiry_time.strftime("%Y-%m-%d %H:%M:%S IST")

    return jsonify(
        {
            "original_url": original_url,
            "short_url": f"http://127.0.0.1:5000/{short_id}",
            "expires_in_minutes": expires_in_minutes,
            "expiry_time": ist_time_str,
        }
    )


# Route to redirect short URL to original
@app.route("/<short_id>")
def redirect_url(short_id):
    entry = url_store.get(short_id)
    if not entry:
        return jsonify({"error": "Invalid short URL"}), 404

    if datetime.utcnow() > entry["expiry_time"]:
        return jsonify({"error": "This short URL has expired"}), 410

    return redirect(entry["original_url"])


if __name__ == "__main__":
    app.run(debug=True)
