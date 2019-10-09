import requests, json
from random import shuffle


def get_tracks(tag: str, num=3):
    url = "http://ws.audioscrobbler.com/2.0/"
    key = "aa0ea82681d54b0e0fa96a56695cd659"
    params = {
        "method": "tag.gettoptracks",
        "tag": tag,
        "api_key": key,
        "limit": 50,
        "format": "json",
    }
    response = requests.get(url, params=params)
    content = json.loads(response.content)
    tracks = [track for track in content["tracks"]["track"]]
    shuffle(tracks)
    tracks = tracks[:num]
    return [
        {"artist": track["artist"]["name"].strip(), "title": track["name"].strip()}
        for track in tracks
    ]


def get_lyrics(artist: str, track: str):
    url = f"https://api.lyrics.ovh/v1/{artist}/{track}"
    response = requests.get(url)
    content = json.loads(response.content)
    lyrics = content["lyrics"]
    return lyrics


def get_random_songs(tag: str):
    tracks = get_tracks(tag)
    songs = []
    for track in tracks:
        lyrics = get_lyrics(track["artist"], track["title"])
        songs.append(
            {"artist": track["artist"], "title": track["title"], "lyrics": lyrics}
        )
    return songs

