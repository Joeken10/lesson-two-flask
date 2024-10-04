from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Music(db.Model):
    __tablename__ = "music"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    album_image = db.Column(db.Text)
    album_link = db.Column(db.Text)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))  # Foreign key to link to the Artist table

    # Define the relationship with the Artist
    artist = relationship('Artist', back_populates="songs")

    def music_serializer(self):
        return {
            'id': self.id,
            'title': self.title,
            'album_image': self.album_image,
            'album_link': self.album_link,
            'artist': self.artist.name  # Include artist name in the serialized output
        }

class Artist(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Define the relationship with Music (one-to-many relationship)
    songs = relationship("Music", back_populates="artist")

    def artist_serializer(self):
        return {
            'id': self.id,
            'name': self.name,
            'songs': [song.music_serializer() for song in self.songs]  # Serialize all related songs
        }
