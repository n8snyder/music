from query_libs import get_random_songs


def combine_songs(songs):
    all_lyrics = [song["lyrics"].split("\n") for song in songs]
    min_len = min([len(lyrics) for lyrics in all_lyrics])
    all_lyrics = [lyrics[:min_len] for lyrics in all_lyrics]
    combined_song = []
    song_index = 0
    for line_index in range(min_len):
        combined_song.append(all_lyrics[song_index][line_index])
        song_index += 1
        song_index = song_index % len(all_lyrics)

    combined_song = "\n".join(combined_song)
    return combined_song


if __name__ == "__main__":
    tag = "pop"
    songs = get_random_songs(tag)
    lyrics = combine_songs(songs)

