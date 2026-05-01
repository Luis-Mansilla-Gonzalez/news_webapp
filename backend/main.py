import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/news")
def get_news():
    try:
        url = "https://api.gdeltproject.org/api/v2/doc/doc"

        params = {
            "query": "sourceCountry:US politics",
            "mode": "ArtList",
            "format": "json",
            "maxrecords": 50
        }

        response = requests.get(url, params=params)
        data = response.json()

        articles = data.get("articles") or data.get("result") or data.get("documents") or []

        formatted = []

        for a in articles:
            formatted.append({
                "title": a.get("title") or "No title",
                "url": a.get("url") or a.get("sourceUrl") or ""
            })

        return jsonify(formatted)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return {"message": "Backend is running"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)