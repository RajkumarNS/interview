from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/<username>', methods=['GET'])
def get_gists(username):
    url = f"https://api.github.com/users/{username}/gists"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "User not found"}), 404

    gists = response.json()

    result = []
    for gist in gists:
        result.append({
            "id": gist["id"],
            "url": gist["html_url"]
        })

    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
