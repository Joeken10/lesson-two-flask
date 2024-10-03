from model import Music,db
from app import app

with app.app_context():
  music1= Music(title='test', artist='testing', album_image='testing_on', album_link='tested')
  music2= Music(title='test', artist='testing', album_image='testing_on', album_link='tested')

  db.session.add(music1)
  db.session.add(music2)
  db.session.commit()