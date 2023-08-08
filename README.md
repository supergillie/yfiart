# yfiart

start with "flask run"
try locally with http://127.0.0.1:5000/artist/Lee%20Perry



todo: 
C To prevent the same cover from appearing twice when you reload, you'll need to store the previously displayed covers and ensure they're not selected again. One way to achieve this is by using browser local storage.

Hodify the Flask app and the HTML template to implement this:
ß
1. **Python Code (Flask App)**:

First, modify the Flask route to accept a list of previously displayed album IDs:

```python
@app.route('/artist/<artist_name>/<previous_ids>')
def artist(artist_name, previous_ids):
    # ... (rest of the code remains unchanged)

    # Filter out previously displayed albums
    previous_ids_list = previous_ids.split(',')
    filtered_results = [album for album in data['results'] if str(album['id']) not in previous_ids_list]

    # Randomly select 9 album covers from the filtered results
    albums = random.sample(filtered_results, min(9, len(filtered_results)))
    return render_template('index.html', albums=albums)
```

2. **JavaScript (within the HTML template)**:

Add JavaScript to store the IDs of the displayed albums in local storage and use them when reloading:

```html
<!-- ... (rest of the HTML code) ... -->

<script>
    // Store the IDs of the displayed albums in local storage
    const albumIds = [{% for album in albums %}"{{ album.id }}",{% endfor %}];
    localStorage.setItem('previousAlbums', albumIds.join(','));

    // Modify the reload button's onclick function
    document.querySelector('.reload-btn').onclick = function() {
        const previousAlbums = localStorage.getItem('previousAlbums') || '';
        location.href = `/artist/Santana/${previousAlbums}`;
    };
</script>
```

With these modifications:

- When you click the reload button, the Flask route will receive the IDs of the previously displayed albums.
- The Flask app will then filter out these albums before randomly selecting 9 new ones.
- The JavaScript will store the IDs of the displayed albums in local storage and use them when reloading the page.

This will ensure that the same cover doesn't appear twice when you reload. However, note that this approach works for consecutive reloads. If you want to reset and allow all covers to be selectable again, you'd need to clear the local storage or provide an additional mechanism to do so.