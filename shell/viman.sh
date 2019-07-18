#!/bin/bash

MAN1=$1
MAN2=$2

nvim -c "Man $MAN1 $MAN2" -c "silent only"
