#!/bin/bash
# takes an URL (uniform resource locator) and displays all HTTP methods the server supports
curl -sI "$1" | grep Allow | cut -d' ' -f2-
