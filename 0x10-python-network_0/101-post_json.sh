#!/bin/bash
# Sends a JSON POST request to URL passed as the first argument and displays response body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
