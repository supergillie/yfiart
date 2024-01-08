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
    records_per_fetch = 50  # Number of records fetched each time
    start = (page - 1) * per_page
    end = start + per_page

    # Calculate the API page to fetch based on the current page
    api_page = (start // records_per_fetch) + 1
    start_record = start % records_per_fetch
    end_record = start_record + per_page

    url = BASE_URL + artist_name + f"&page={api_page}&per_page={records_per_fetch}"
    headers = {
        "User-Agent": "FlaskApp/1.0 +http://localhost:5000",
        "Authorization": f"Discogs token={TOKEN}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    # Check if we have enough records to cover the current page
    if start_record < len(data['results']):
        albums = data['results'][start_record:end_record]
    else:
        albums = []

    return render_template('index.html', albums=albums, artist_name=artist_name, page=page)


if __name__ == '__main__':
    app.run(debug=True)
