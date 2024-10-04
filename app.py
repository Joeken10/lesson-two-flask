from flask import Flask, jsonify, abort
from model import Music, db
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
    
    # If song is not found, return 404
    if music_item is None:
        abort(404, description=f"Song with ID {song_id} not found")
    
    return jsonify(music_item.music_serializer())

if __name__ == "__main__":
    app.run(port=5000, debug=True)
