from flask import Flask, render_template, redirect
import requests
import random

app = Flask(__name__)

BASE_URL = "https://api.discogs.com/database/search?type=master&artist="
DISCOGS_URL = "https://api.discogs.com/database/search?type=master&artist=Santana"
TOKEN = "JLyawlHOYLPCOPyRQqVoASPqzwJAgRjldmGUNJwA"



@app.route('/')
def home():
    return redirect('/artist/Abba', code=302)

@app.route('/artist/<artist_name>')
def artist(artist_name):
    url = BASE_URL + artist_name
    headers = {
        "User-Agent": "FlaskApp/1.0 +http://localhost:5000",
        "Authorization": f"Discogs token={TOKEN}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    results_length = len(data['results'])  # Get the length of data['results']

    print("Number of rows in data['results']:", len(data['results']))
    
    # Randomly select 9 album covers if there are at least 9 results
    albums = random.sample(data['results'], min(9, len(data['results'])))
    return render_template('index.html', albums=albums, results_length=results_length, artist_name=artist_name)

if __name__ == '__main__':
    app.run(debug=True)
