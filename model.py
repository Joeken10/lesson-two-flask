from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Music(db.Model):
  __tablename__ = "music"

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String)
  artist = db.Column(db.String)
  album_image = db.Column(db.Text)
  album_link = db.Column(db.Text)

  def music_serializer(self):
    return{
      'id':self.id,
      'title':self.title,
      'artist':self.artist,
      'album_image':self.album_image,
      'album_link':self.album_link
    }