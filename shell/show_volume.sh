#!/bin/bash

VOLVL=$(amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }')

dunstify -a "changeVolume" -u low -i volume-level-high-pink -r "2" $VOLVL "● ○"
