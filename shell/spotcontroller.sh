#!/bin/sh

eval $(xdotool getmouselocation --shell)

ORDER=$(printf 'Next\nPlay/Pause\nPrev\n' | rofi -dmenu -theme /home/ab/rofi_themes/spotcontroller.rasi -location 1 -yoffset 40 -xoffset $X)

if [ "$ORDER" = "Next" ]; then
    dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next
    exit 0
fi

if [ "$ORDER" = "Play/Pause" ]; then
    dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause
    exit 0
fi

if [ "$ORDER" = "Prev" ]; then
    dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous
    exit 0
fi
