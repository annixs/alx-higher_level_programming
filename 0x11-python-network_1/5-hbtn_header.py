#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
<<<<<<< HEAD
=======

>>>>>>> ea1d434252a592ebf357e65388dd9b33ff0ffe48
