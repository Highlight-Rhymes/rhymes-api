from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/songs")
def get_songs():
    return ["1", "2", "3"]

@app.route("/songs/<song_id>")
def get_song(song_id):
    print("return the information for <song_id>")

@app.route("/songs", methods = ['POST'])
def post_songs():
    data = request.form
    if data['song']:
        song = data['song']
    if data['lyrics']:
        lyrics = data['lyrics']
    print("processing new song")
    return {
        status: "200"
    }

if __name__ == "__main__":
    app.run()