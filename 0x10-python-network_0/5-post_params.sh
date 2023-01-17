#!/bin/bash
# sends a POST request with two variables and values
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
