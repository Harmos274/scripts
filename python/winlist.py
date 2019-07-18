#!/usr/bin/env python3


"""Get a list of opened window in current workspace"""


import os
import sys


def get_winlist():

    """main function"""

    winlist_cmd = "wmctrl -l | cut -d' ' -f3,5-"
    currentws_cmd = "wmctrl -d | grep \"*\" | cut -d' ' -f1"

    raw_winlist = os.popen(winlist_cmd).read()
    currentws = os.popen(currentws_cmd).read()

    ws_winlist = get_ws_winlist(raw_winlist, currentws)
    winlist_printer(ws_winlist)


def get_ws_winlist(raw_wl, curr_ws):

    """Get window occurences between ws nbr and winlist"""

    ls_raw_wl = raw_wl.splitlines()
    len_ls_raw_wl = len(ls_raw_wl)
    ws_winlist = []

    for i in range(0, len_ls_raw_wl):
        if int(ls_raw_wl[i].split(' ', 1)[0]) == int(curr_ws):
            ws_winlist.append(ls_raw_wl[i].split(' ', 1)[1])
    return ws_winlist


def winlist_printer(ws_winlist):

    """Print winlist"""

    if "-h" in sys.argv:
        print("winlist.py:\nThis script display apps oppened in your current"
              " workspace.\n\nFLAGS:\n\t-h\tDisplay this message.\n\t-l\t"
              "Display windows in list.")
    elif "-l" in sys.argv:
        len_ws_winlist = len(ws_winlist)
        for i in range(0, len_ws_winlist):
            print(ws_winlist[i])
    else:
        len_ws_winlist = len(ws_winlist)
        for i in range(0, len_ws_winlist):
            if i != len_ws_winlist - 1:
                print(ws_winlist[i], end="")
                print(" ", end="")
            else:
                print(ws_winlist[i])


if __name__ == "__main__":
    get_winlist()
