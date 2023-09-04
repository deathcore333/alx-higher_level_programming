#!/bin/bash
# sendas a DELETE request to the URL passed as the first argument, displays the body of the response
curl -sX DELETE "$1"
