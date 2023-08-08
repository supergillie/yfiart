from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

BASE_URL = "https://api.discogs.com/database/search?type=master&artist="
DISCOGS_URL = "https://api.discogs.com/database/search?type=master&artist=Santana"
TOKEN = "qwzwnSYzsXKaYhvBPBgIMThxSCnGmRlgbAelZPsJ"

@app.route('/artist/<artist_name>')
def artist(artist_name):
    url = BASE_URL + artist_name
    headers = {
        "User-Agent": "FlaskApp/1.0 +http://localhost:5000",
        "Authorization": f"Discogs token={TOKEN}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    # Randomly select 9 album covers if there are at least 9 results
    albums = random.sample(data['results'], min(9, len(data['results'])))
    return render_template('index.html', albums=albums)

@app.route('/')
def index():
    headers = {
        "User-Agent": "FlaskApp/1.0 +http://localhost:5000",
        "Authorization": f"Discogs token={TOKEN}"
    }
    response = requests.get(DISCOGS_URL, headers=headers)
    data = response.json()

    # Randomly select 9 album covers
    albums = random.sample(data['results'], 9)
    return render_template('index.html', albums=albums)

if __name__ == '__main__':
    app.run(debug=True)
