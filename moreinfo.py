#!/usr/bin/env python3
import argparse
import os
import shlex
import time
from mylast import (
    TRACK_SEPARATOR,
    lastfm_network,
    lastfm_username,
    print_track,
    split_artist_track,
    track_and_timestamp,
)

# Show my now playing song, or that of a given username
# Prerequisites: mylast.py, pyLast


def say(thing):
    cmd = "say {}".format(shlex.quote(str(thing)))
    os.system(cmd)

def printTrackinfo(track_to_check, info_size):
    if (info_size=="All"):
        print("The song playing: " + str(track_to_check))
        print("The URL for the song:")
        print(track_to_check.get_url())
        print("------------")
        print("Wiki Summary")
        #print(now_playing.get_wiki("summary"))
        print(track_to_check.get_wiki_summary())
        print("------------")
        print("Wiki Content")
        #print(now_playing.get_wiki("content"))
        print(track_to_check.get_wiki_content())
        print("------------")
    elif (info_size=="New"):
        artist = track_to_check.get_artist()
        album = track_to_check.get_album()
        tags= track_to_check.get_top_tags()
        print("Tags:")
        print(tags[0])
        print("Artist:" + str(artist))
        print("Album:" + str(album))

def get_recent_tracks(username, number):
    recent_tracks = lastfm_network.get_user(username).get_recent_tracks(limit=number)
    for i, track in enumerate(recent_tracks):
        printable = track_and_timestamp(track)
        print(str(i + 1) + " " + printable)
    return recent_tracks


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Show some info on now playing song",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "variant",
        nargs="?",
        default="standard",
        help="Choose variant on what to display",
    )
    parser.add_argument(
        "username",
        nargs="?",
        default=lastfm_username,
        help="Show now playing of this username",
    )
    parser.add_argument(
        "-n",
        "--number",
        default=20,
        type=int,
        help="Number of tracks to show (when no artist given)",
    )
    parser.add_argument("--loop", action="store_true", help="Loop until Ctrl-C")
    parser.add_argument("--say", action="store_true", help="Announcertron 4000")
    args = parser.parse_args()

    if args.variant == "standard":
        print("Standard version coming up")
        now_playing_track = lastfm_network.get_user(args.username).get_now_playing()
        example_track = lastfm_network.get_track("Dire Straits", "Sultans of swing")
        track_to_check = example_track
        info_size = "New"
        printTrackinfo(track_to_check, info_size)

    elif args.variant == "test1":
        get_recent_tracks(args.username, args.number)

    else:
        print("No variant choosen")