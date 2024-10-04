from flask import Flask, jsonify, abort 
from model import Music, Artist, db
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://june:june2004@localhost/mimusic'
db.init_app(app)
migrate = Migrate(app, db)

# Endpoint to return all songs
@app.route('/music_list', methods=['GET'])
def index():
    music_items = Music.query.all()
    return jsonify([music_item.music_serializer() for music_item in music_items])

# Endpoint to return a specific song by its ID
@app.route('/music/<int:song_id>', methods=['GET'])
def get_song(song_id):
    music_item = Music.query.get(song_id)
    
    if music_item is None:
        abort(404, description=f"Song with ID {song_id} not found")
    
    return jsonify(music_item.music_serializer())


# Endpoint to return all artists
@app.route('/artists', methods=['GET'])
def get_artists():
    artist_items = Artist.query.all()
    print("Fetched artists:", [artist.name for artist in artist_items])  # Debug output
    return jsonify([{"id": artist.id, "name": artist.name} for artist in artist_items])

# Endpoint to return a specific artist by their ID
@app.route('/artists/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    artist_item = Artist.query.get(artist_id)
    
    print(f"Fetching artist with ID {artist_id}")  # Debug output
    if artist_item is None:
        abort(404, description=f"Artist with ID {artist_id} not found")
    
    return jsonify({"id": artist_item.id, "name": artist_item.name})

