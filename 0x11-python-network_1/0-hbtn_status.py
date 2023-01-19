#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
and displays status information
"""
import urllib.request


if __name__ == "__main__":
    """
    This script fetches a URL with an urllib
    and displays info of the status
    """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        statusInfo = response.read()

    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(statusInfo), statusInfo, str(statusInfo)[2:-1]))
