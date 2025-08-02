# 🔗 URL Shortener with Expiry Feature ⏳

A simple Flask-based URL shortener that allows users to generate short URLs with custom expiration time. If no time is provided, the short URL expires in **30 minutes** by default.

---

## Features

-  Shortens long URLs to random 6-character keys.
-  Expiry support: user can specify expiry time in **minutes**.
-  Default expiry: 30 minutes if not given.
-  Stores data in a Python dictionary (in-memory).
-  Easy to deploy and run locally.

---

##  Architecture

User Request (POST /shorten)
⬇
Flask Backend (Python)
⬇
Generate Unique Key (6 chars)
⬇
Store Original URL, Expiry Time
⬇
Return Short URL + Expiry Info
⬇
Redirect via /<short_key> (GET)




---

##  Setup Instructions

###  Requirements

- Python 3.x
- Flask

###  Install Flask

```bash
pip install flask
🔗 POST Request: /shorten
Example with expiry: 10 min
curl -X POST -H "Content-Type: application/json" \
-d "{\"url\":\"https://example.com\",\"expires_in_minutes\":10}" \
http://127.0.0.1:5000/shorten

Example without expiry (default 30 min)
curl -X POST -H "Content-Type: application/json" \
-d "{\"url\":\"https://example.com\"}" \
http://127.0.0.1:5000/shorten
Response:
{
  "original_url": "https://example.com",
  "short_url": "http://127.0.0.1:5000/Ab12Xy",
  "expires_in_minutes": 10,
  "expiry_time": "2025-08-02 15:00:00 UTC"
}





