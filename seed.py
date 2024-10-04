from sqlalchemy import text
from model import db, Artist, Music
from app import app

with app.app_context():
    # Step 1: Clear the data from the tables
    db.session.query(Music).delete()
    db.session.query(Artist).delete()
    db.session.commit()

    # Step 2: Reset the ID sequence for the artists and music tables
    db.session.execute(text("ALTER SEQUENCE artists_id_seq RESTART WITH 1;"))
    db.session.execute(text("ALTER SEQUENCE music_id_seq RESTART WITH 1;"))

    db.session.commit()

    # Step 3: Add new data
    artist = Artist(name='Test Artist')
    artist1 = Artist(name='Test Artist1')

    # Create songs associated with the artist
    music1 = Music(title='Test Song 1', album_image='image1.jpg', album_link='link1.com', artist=artist)
    music2 = Music(title='Test Song 2', album_image='image2.jpg', album_link='link2.com', artist=artist1)

    # Add artist and songs to the session
    db.session.add(artist)
    db.session.add(artist1)
    db.session.add(music1)
    db.session.add(music2)

    db.session.commit()

    print("Data reset and new entries added successfully.")
