#!/bin/bash
# takes URL, sends request to URL, displays the body size of response
curl -s "$!" | wc -c
