#!/bin/sh

surf http://google.com &

PID=$!

while [ "$WID" == "" ]; do
    WID=$(wmctrl -lp | grep $PID | cut "-d " -f1)
done

wmctrl -i -r $WID -e 0,50,50,700,700
