#run command
#gcloud app deploy --project=powerful-bounty-401013 --version 1

#run command
#gcloud app deploy --project=powerful-bounty-401013 --version 1

from flask import Flask, json, request

app = Flask(__name__)
songs = [
    {
        "title": "Rockstar",
        "artist": "Dababy",
        "genre": "rap",
    },
    {
        "title": "Say So",
        "artist": "Doja Cat",
        "genre": "Hiphop",
    },
    {
        "title": "Panini",
        "artist": "Lil Nas X",
        "genre": "Hiphop"
    }
]
@app.route('/')
def index():
    songs = request.get_json()
    return json(songs)

@app.route('/songs', methods=['GET'])
def add_songs():
    songs = request.get_json()
    songs.append(songs)
    return json(songs)

@app.route('/songs', methods=['POST'])
def add_songsPOST():
    songs = request.get_json()
    songs.append(songs)
    return json(songs)

if __name__ == '__main__':
  app.run(debug=True)
