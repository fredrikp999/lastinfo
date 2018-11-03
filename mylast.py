# coding: utf-8

import os
import sys

import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account for Last.fm

try:
    LASTFM_API_KEY = os.environ["LASTFM_API_KEY"]
    LASTFM_API_SECRET = os.environ["LASTFM_API_SECRET"]
except KeyError:
    print("Keys not in environment variables, please fix")
    API_KEY = "Add a key here if you do not want to use environame variables"
    API_SECRET = "Add a secret here if you do not want to use environame variables"

try:
    lastfm_username = os.environ["LASTFM_USERNAME"]
    lastfm_password_hash = os.environ["LASTFM_PASSWORD_HASH"]
except KeyError:
    # In order to perform a write operation you need to authenticate yourself
    lastfm_username = "Add a user here if you do not want to use environame variables"
    # You can use either use the password, or find the hash once and use that
    lastfm_password_hash = "Add a md5-hash or the password here if you do not want to use environame variables"
    #print(lastfm_password_hash)
    print("Key error. Username and hash not in environment variables")

lastfm_network = pylast.LastFMNetwork(
    api_key=LASTFM_API_KEY,
    api_secret=LASTFM_API_SECRET,
    username=lastfm_username,
    password_hash=lastfm_password_hash,
)

def track_and_timestamp(track):
    return f"{track.playback_date}\t{track.track}"


def print_track(track):
    print(track_and_timestamp(track))


TRACK_SEPARATOR = " - "


def split_artist_track(artist_track):
    artist_track = artist_track.replace(" – ", " - ")
    artist_track = artist_track.replace("“", '"')
    artist_track = artist_track.replace("”", '"')

    (artist, track) = artist_track.split(TRACK_SEPARATOR)
    artist = artist.strip()
    track = track.strip()
    print("Artist:\t\t'" + artist + "'")
    print("Track:\t\t'" + track + "'")

    # Validate
    if len(artist) is 0 and len(track) is 0:
        sys.exit("Error: Artist and track are blank")
    if len(artist) is 0:
        sys.exit("Error: Artist is blank")
    if len(track) is 0:
        sys.exit("Error: Track is blank")

    return (artist, track)


# End of file