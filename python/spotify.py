#!/usr/bin/env python3
# coding: utf-8


"""Get Spotify Music and Artist"""


import sys
import dbus


def get_spot_song_info():

    """main function"""

    if len(sys.argv) == 1:
        trunclen = 25
    else:
        trunclen = int(sys.argv[1])

    try:
        session_bus = dbus.SessionBus()
        spotify_bus = session_bus.get_object(
            "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
        spotify_properties = dbus.Interface(
            spotify_bus, "org.freedesktop.DBus.Properties")
        metadata = spotify_properties.Get(
            "org.mpris.MediaPlayer2.Player", "Metadata")
        artist = metadata['xesam:artist'][0]
        song = metadata['xesam:title']

        if len(song) > trunclen:
            song = song[0:trunclen]
            song += '...'
        if ('(' in song) and (')' not in song):
            song += ')'
        output = artist + ': ' + song
        print(output)

    except RuntimeError:
        print("")


if __name__ == "__main__":
    get_spot_song_info()
