#!/bin/bash
# takes URL, sends request to URL, displays the body size of response
curl -sI "$!" | grep Content-Length | cut -d " " -f2
