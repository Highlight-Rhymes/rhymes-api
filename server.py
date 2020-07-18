from flask import Flask
from flask import request
from mongo import getSongs, insertSong
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/songs")
def get_songs():
    return {
        'songs': getSongs()
    }

@app.route("/songs/<song_id>")
def get_song(song_id):
    print("return the information for <song_id>")

@app.route("/songs", methods = ['POST'])
def post_songs():
    data = request.form
    if data['song']:
        song_id = insertSong(data['song'])
    return {
        "status": "200",
        "song_id": str(song_id)
    }

if __name__ == "__main__":
    app.run()