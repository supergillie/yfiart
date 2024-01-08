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
@app.route('/artist/<artist_name>/<int:page>')
def artist(artist_name, page=1):
    per_page = 9  # Number of albums per page
    start = (page - 1) * per_page
    end = start + per_page
    
    url = BASE_URL + artist_name
    headers = {
        "User-Agent": "FlaskApp/1.0 +http://localhost:5000",
        "Authorization": f"Discogs token={TOKEN}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    results_length = len(data['results'])  # Get the length of data['results']

    print("Number of rows in data['results']:", len(data['results']))
    
    # Get a subset of albums for the current page
    albums = data['results'][start:end]

    # Calculate the total number of pages
    total_pages = (len(data['results']) + per_page - 1) // per_page

    return render_template('index.html', albums=albums, results_length=results_length, artist_name=artist_name, page=page, total_pages=total_pages)

if __name__ == '__main__':
    app.run(debug=True)
