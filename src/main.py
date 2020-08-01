from flask import Flask
from flask import request
from mongo import getSongs, insertSong
from lib.song import getSongFromYoutube
app = Flask(__name__)

@app.route("/")
def hello():
    print(getSongFromYoutube("get"))
    return "Hello World!"

@app.route("/songs")
def get_songs():
    return {
        'songs': getSongs()
    }

@app.route("/songs/<song_id>")
def get_song(song_id):
    print("return the information for <song_id>")

@app.route("/song", methods = ['POST'])
def post_song():
    data = request.form
    if data['song']:
        song_id = insertSong(data['song'])
    return {
        "status": "200",
        "song_id": str(song_id)
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)